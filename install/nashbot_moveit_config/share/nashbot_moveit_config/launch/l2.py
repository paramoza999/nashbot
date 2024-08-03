import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node

def generate_launch_description():
    # Paths to necessary files
    robot_description_path = os.path.join(get_package_share_directory('nashbot'), 'description', 'robot.urdf')
    rviz_config_path = os.path.join(get_package_share_directory('nb_moveit'), 'config', 'moveit.rviz')
    srdf_path = os.path.join(get_package_share_directory('nb_moveit'), 'config', 'nashbot.srdf')

    # Declare launch arguments
    declared_arguments = [
        DeclareLaunchArgument('rviz_config', default_value=rviz_config_path, description='Path to RViz config file'),
        DeclareLaunchArgument('robot_description', default_value=robot_description_path, description='Path to robot URDF file'),
    ]

    # Launch configuration variables
    robot_description = LaunchConfiguration('robot_description')
    rviz_config = LaunchConfiguration('rviz_config')

    # Robot state publisher
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': Command(['xacro ', robot_description])}]
    )

    # RViz node
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        output='screen',
        arguments=['-d', rviz_config]
    )

    # MoveIt2 node
    move_group_node = Node(
        package='moveit_ros_move_group',
        executable='move_group',
        output='screen',
        parameters=[
            {'robot_description': Command(['xacro ', robot_description])},
            {'robot_description_semantic': Command(['xacro ', srdf_path])},
        ]
    )

    return LaunchDescription(declared_arguments + [
        robot_state_publisher_node,
        rviz_node,
        move_group_node
    ])

