from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(package='my_minimal_pubsub', executable='talker', output='screen'),
        Node(package='my_minimal_pubsub', executable='listener', output='screen'),
    ])
