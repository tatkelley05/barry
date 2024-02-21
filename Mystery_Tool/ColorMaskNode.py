import rclpy
from rclpy.node import Node

import cv2

from sensor_msgs.msg import Image

from Mystery_Tool.ColorMask import ColorMask

class ColorMaskNode(Node):

    def _init_(self):
        super().__init__('Jerry')
        self.publisher_ = self.create_publisher(Image, 'camera_stream', 10)
        self.i = 0
        self.cap = cv2.VideoCapture(0)
        self.timer = self.create_timer(0.01, self.broadcast)

    def broadcast(self):
        ret, frame = self.cap.read()
        mask_tool = ColorMask(ret, frame)
        msg = Image()
        msg.data = mask_tool
        msg.height = len(mask_tool)
        msg.width = len(mask_tool[0])
        self.publisher_.publish(msg)

def main():
    rclpy.init()
    camera_publisher = ColorMaskNode('Jerry')
    rclpy.spin(camera_publisher)
    rclpy.shutdown()
