import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

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
        parameters=[{'robot_description': ParameterValue(Command(['xacro ', robot_description]), value_type=str)}]
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
            {'robot_description': ParameterValue(Command(['xacro ', robot_description]), value_type=str)},
            {'robot_description_semantic': ParameterValue(Command(['xacro ', srdf_path]), value_type=str)},
        ]
    )

    return LaunchDescription(declared_arguments + [
        robot_state_publisher_node,
        rviz_node,
        move_group_node
    ])
