#!/usr/bin/env python3

import rospy
import socket
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion
import numpy as np

UDP_IP = "192.168.250.179"
UDP_PORT = 4210

class main():
    def __init__(self):
        
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("/cmd_vel", Twist, self.callback)
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        print("UDP target IP: %s" % UDP_IP)
        print("UDP target port: %s" % UDP_PORT)

    def callback(self,msg):
        x = msg.linear.x
        if(x<=2.2):
        	x = 0
        y = msg.linear.y
        z = msg.angular.z
        if(z<=1.2):
        	z = 0
        #inverse kinematics equation
        A1=([0.667,0,-0.333],
            [-0.333,0.577,-0.333],
            [-0.333,-0.577,-0.333])
        A2=([x,y,z])
        A3=np.dot(A1,A2)
        #assigning velocities to the motors
        x = A3[0]
        x = round(x,1)
        x = x.__str__()
        y = A3[1]
        y = round(y,1)
        y = y.__str__()
        z = A3[2]
        z = round(z,1)
        z = z.__str__()
        #passing velocities through udp
        MESSAGE = x + ',' + y + ',' + z
        print(MESSAGE)
        self.sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

if __name__ == '__main__':
    main()
    try:
        if not rospy.is_shutdown():
            rospy.spin()
    except rospy.ROSInterruptException as e:
        print(e)
