import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.pub = self.create_publisher(String, 'chatter', 10)
        self.count = 0
        self.create_timer(0.5, self.tick)  # 2 Hz

    def tick(self):
        msg = String()
        msg.data = f"Hello, ROS 2! #{self.count}"
        self.pub.publish(msg)
        self.get_logger().info(f"Published: {msg.data}")
        self.count += 1

def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
