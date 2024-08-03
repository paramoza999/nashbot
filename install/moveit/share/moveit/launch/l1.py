from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Get the share directory of the 'nashbot' package
    package_share_directory = get_package_share_directory('nashbot')

    # Path to the robot description (URDF or SDF)
    robot_description_file = os.path.join(package_share_directory, 'description', 'robot.urdf')

    if not os.path.exists(robot_description_file):
        raise FileNotFoundError(f"Robot description file not found: {robot_description_file}")

    with open(robot_description_file, 'r') as infp:
        robot_description = infp.read()

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description}]
        ),
    ])
