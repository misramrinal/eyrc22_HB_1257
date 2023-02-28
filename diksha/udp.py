#!/usr/bin/env python3

import rospy
import socket
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion
import numpy as np

UDP_IP = "192.168.171.178"
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
        # if(x<=2.2):
        	# x = 0
        y = msg.linear.y
        z = msg.angular.z
        # if(z<=1.2):
        	# z = 0
        #inverse kinematics equation
        A1 = (40)*([-0.12, 1, 0],[-0.12, -0.5, -0.866],[-0.12,  -0.5, 0.866])
        A2=([z, x, y])
        A3=np.dot(A1,A2)
        #assigning velocities to the motors
        v1 = A3[1]
        v1 = round(v1,2)
        v1 = v1.__str__()
        v2 = A3[2]
        v2 = round(v2,2)
        v2 = v2.__str__()
        v3 = A3[0]
        v3 = round(v3,2)
        v3 = v3.__str__()
        #passing velocities through udp
        MESSAGE = v1 + ',' + v2 + ',' + v3
        print(MESSAGE)
        self.sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

if __name__ == '__main__':
    main()
    try:
        if not rospy.is_shutdown():
            rospy.spin()
    except rospy.ROSInterruptException as e:
        print(e)
