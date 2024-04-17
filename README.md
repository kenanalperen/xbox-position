# xbox-position
 In this project, the main idea is to take input from the xbox gamepad from the joysticks/buttons using ROS2 and map them to the movement of the manipulator of the MOCA robot which uses ROS1.

 First, check ROS1-ROS2 bridging:
[ROS1-ROS2 Bridge](https://github.com/kenanalperen/ros1-2)

# Geting input from xbox

go to workspace and install joy
```bash
cd ~/ros2_ws/
sudo apt install ros-foxy-joy
```

Source the ws
```bash
colcon build
source install/setup.bash
```

run the joy node
```bash
ros2 run joy joy_node
```
check the topics and echo the positions using

```bash
ros2 topic echo /joy
```
information about the message
```bash
ros2 topic info /joy
Type: sensor_msgs/msg/Joy
ros2 interface show sensor_msgs/msg/Joy
# Reports the state of a joystick's axes and buttons.

# The timestamp is the time at which data is received from the joystick.
std_msgs/Header header

# The axes measurements from a joystick.
float32[] axes

# The buttons measurements from a joystick.
int32[] buttons
```

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
