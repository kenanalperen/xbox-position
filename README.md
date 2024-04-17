# xbox-position
 In this project, the main idea is to take input from the xbox gamepad from the joysticks/buttons using ROS2 and map them to the movement of the manipulator of the MOCA robot which uses ROS1.

 First, check ROS1-ROS2 bridging:
[ROS1-ROS2 Bridge](https://github.com/kenanalperen/ros1-2)

# Geting input from xbox

# Sending position to the arm
MOCA arm takes input from ROS1 by following topics

```bash
/franka_a/cartesian_impedance_controller/equilibrium_pose
/franka_a/robot_state
```
The first one is the position and rotation
```bash
rostopic info /franka_a/cartesian_impedance_controller/equilibrium_pose
Type: geometry_msgs/PoseStamped
```
```bash
rosmsg show geometry_msgs/PoseStamped
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
geometry_msgs/Pose pose
  geometry_msgs/Point position
    float64 x
    float64 y
    float64 z
  geometry_msgs/Quaternion orientation
    float64 x
    float64 y
    float64 z
    float64 w
```
Be careful following RobotState is a custom message, probably robot will not activate without it. Ask Hamidreza

```bash
rostopic info /franka_a/robot_state
Type: hrii_robot_msgs/RobotState
```

After you create python node, source

As an example, let's send an input as
```bash
ros2 topic pub /user_input_position geometry_msgs/msg/Point '{x: 1.0, y: 1.0, z: 1.0}'
```
run the converter node

```bash
ros2 run position_control pos 
```
Check topic list in ros2
```bash
ros2 topic list 
```

ros1 roscore
```bash
noetic
roscore
```

bridge ros1-ros2
```bash
noetic
foxy
ros2 run ros1_bridge dynamic_bridge --bridge-all-topics
```

echo in ros1 environment
```bash
noetic
rostopic echo /franka_a/cartesian_impedance_controller/equilibrium_pose
```
