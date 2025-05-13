# crt_ctag2f90c_gripper

This repository provides a complete ROS interface for the **ZHIXING Gripper**, featuring a **position controller based on force and torque**. This repo includes configuration files for MoveIt!, ROS communication interfaces, and a `minimalmodbus`-based hardware communication layer.

---

## 🧩 Features

- 🔧 **Force & Torque Based Position Control**  
  Intelligently adjusts gripper position based on sensor feedback.

- 🤖 **MoveIt! Integration**  
  Includes a complete `moveit_config` for easy motion planning and visualization.

- 🧠 **ROS Interface**  
  Provides ROS topics, services, and action servers for high-level control.

- 🔌 **MinimalModbus Interface**  
  Communicates with the gripper hardware over Modbus RTU protocol.

---

## 📦 Package Contents

| Folder / File           | Description                                 |
|-------------------------|---------------------------------------------|
| `moveit_config/`        | MoveIt! configuration package               |
| `zhixing_gripper_ros/`  | ROS node for gripper control                |
| `modbus_interface/`     | Python/C++ interface via minimalmodbus      |
| `launch/`               | Sample launch files                         |
| `config/`               | YAML configuration for parameters           |
| `urdf/`                 | Gripper robot description (URDF/Xacro)      |

---

## 🚀 Getting Started

### Prerequisites

- ROS Noetic with gazebo-11 (specify your ROS version)
- Python 3
- [minimalmodbus](https://github.com/pyhys/minimalmodbus)

Install dependencies:

```bash
sudo apt install ros-${ROS_DISTRO}-moveit
pip install minimalmodbus
git clone https://github.com/Hency-727/crt_ctag2f90c_gripper/
```

Run:

```bash
cd crt_ctag2f90c_gripper && catkin_make

roslaunch gripper_moveit_config demo_gazebo.launch # open gazebo model and check in the rviz
```

edit model in the file [urdf](https://github.com/Hency-727/crt_ctag2f90c_gripper/src/gazebo_crt_ctag2f90c_gripper_visualization.urdf)
