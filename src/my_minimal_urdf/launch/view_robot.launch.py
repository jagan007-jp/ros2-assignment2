from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg = get_package_share_directory('my_minimal_urdf')
    urdf = PathJoinSubstitution([pkg, 'urdf', 'two_link.urdf'])

    return LaunchDescription([
        Node(package='robot_state_publisher',
             executable='robot_state_publisher',
             parameters=[{'robot_description': Command(['xacro ', urdf])}],
             output='screen'),

        Node(package='joint_state_publisher_gui',
             executable='joint_state_publisher_gui',
             output='screen'),

        Node(package='rviz2', executable='rviz2', output='screen'),
    ])
