#!/usr/bin/ python3
# -*- coding: UTF-8 -*-
import minimalmodbus
import serial
import threading
import rospy
import time
from sensor_msgs.msg import JointState

# 寄存器地址
ENABLE = 0x0100 
POSITION_HIGH_8 = 0x0102  # 位置寄存器高八位
POSITION_LOW_8 = 0x0103  # 位置寄存器低八位
SPEED = 0x0104
FORCE = 0x0105
ACCELERATION = 0x0106
DEACCELERATION = 0x0107
MOTION_TRIGGER = 0x0108
RETURN_ZERO = 0x0402
PORT = '/dev/ttyUSB0'  # 修改为您的COM口号
BAUD = 115200

instrument = minimalmodbus.Instrument(PORT, 1)
instrument.serial.baudrate = BAUD
instrument.serial.timeout = 1

lock = threading.Lock()

def enable(instrument):
    with lock:
        instrument.write_register(ENABLE, 1, functioncode=6)

# 写入高八位位置
def write_position_high8(instrument, value):
    with lock:
        instrument.write_register(POSITION_HIGH_8, value, functioncode=6)

# 写入低八位位置
def write_position_low8(instrument, value):
    with lock:
        instrument.write_register(POSITION_LOW_8, value, functioncode=6)

# 写入位置
def write_position(instrument, value):
    with lock:
        instrument.write_long(POSITION_HIGH_8, value)

# 写入速度
def write_speed(instrument, speed):
    with lock:
        instrument.write_register(SPEED, speed, functioncode=6)

# 写输入
def write_force(instrument, force):
    with lock:
        instrument.write_register(FORCE, force, functioncode=6)

# 触发运动
def trigger_motion(instrument):
    with lock:
        instrument.write_register(MOTION_TRIGGER, 1, functioncode=6)

def acceleration(instrument,acc):
    with lock:
        instrument.write_register(ACCELERATION, acc, functioncode=6)

def deacceleration(instrument,deacc):
    with lock:
        instrument.write_register(DEACCELERATION, deacc, functioncode=6)

def return_zero(instrument):
    with lock:
        instrument.write_register(RETURN_ZERO, 1, functioncode=6)


l1 = [0 for i in range(5)]
l2 = [1001]
def callback(data):
    rate = rospy.Rate(50)
    # print(data.position[2])
    p = int( (1-(data.position[2])) * 9000) 
    # p = int( (data.position[2]) * 100) 
    # write_position_high8(instrument,0x0)
    # write_position_low8(instrument,0xbbbb)
    # write_position(instrument, p)
    # trigger_motion(instrument)
    global l1,l2
    l1.append(p)
    l1.pop(0)

    # if l1.count(p) >=3:
    #     print(p)
    #     write_position(instrument, p)
    #     trigger_motion(instrument)


    if l1.count(p) >=3:
        l2.append(p)
        # print("l1:",l1)
        if l2[-1] != l2[-2]:
            # print(p)
            write_position(instrument, p)
            trigger_motion(instrument)
            # print("l2:",l2)
        l2.pop(0)

    rate.sleep()

if __name__ == '__main__':


    enable(instrument)
    #return_zero(instrument)
    # 写入速度
    write_speed(instrument, 100)

    # 写输入
    write_force(instrument, 100)

    acceleration(instrument,100)
    deacceleration(instrument,100)
    # 触发运动
    # trigger_motion(instrument)

    print("程序开始")
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("joint_states", JointState, callback)
    time.sleep(1)
    rospy.spin()
