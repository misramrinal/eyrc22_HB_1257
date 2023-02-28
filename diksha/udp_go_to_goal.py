#!/usr/bin/env python3

import rospy
import socket
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion
import numpy as np
from geometry_msgs.msg import Wrench 

UDP_IP = "192.168.250.179"
UDP_PORT = 4210

class main():
    def __init__(self):

        self.right_x = self.front_x = self.left_x = 0
        
        rospy.init_node('listener', anonymous=True)

        rospy.Subscriber('/right_wheel_force', Wrench, self.callback_right)
        rospy.Subscriber('/front_wheel_force', Wrench, self.callback_front)
        rospy.Subscriber('/left_wheel_force', Wrench, self.callback_left)
	    # rospy.Subscriber('/front_wheel_force', Wrench, self.callback_front)
	    # rospy.Subscriber('/left_wheel_force', Wrench, self.callback_left)
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        print("UDP target IP: %s" % UDP_IP)
        print("UDP target port: %s" % UDP_PORT)

        while not rospy.is_shutdown():
            right = round(self.right_x,1)
            right = right.__str__()

            front = round(self.front_x,1)
            front = front.__str__()

            left = round(self.left_x,1)
            left = left.__str__()

            MESSAGE = right + ',' + left + ',' + front
            print(MESSAGE)
            self.sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

    def callback_right(self,msg1):
        self.right_x = msg1.force.x

    def callback_front(self,msg2):
        self.front_x = msg2.force.x

    def callback_left(self,msg3):
        self.left_x = msg3.force.x

if __name__ == '__main__':
    main()
    try:
        if not rospy.is_shutdown():
            rospy.spin()
    except rospy.ROSInterruptException as e:
        print(e)
