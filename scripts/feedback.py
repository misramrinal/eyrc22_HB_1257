#!/usr/bin/env python3

'''
*****************************************************************************************
*
*        		===============================================
*           		    HolA Bot (HB) Theme (eYRC 2022-23)
*        		===============================================
*
*  This script should be used to implement Task 0 of HolA Bot (HB) Theme (eYRC 2022-23).
*
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified fromruco.Dictruco.Dictionary 0x7f6a02339570>ionary 0x7f6a02339570>****
'''

# Team ID:		[ HB_1257]
# Author List:		[ Mrinal Misra, Diksha Kumari]
# Filename:		feedback.py
# Functions:    __init__, callback
#			[ Comma separated list of functions in this file ]
# Nodes:		publisher: detected_aruco, subscriber: overhead_cam/image_raw


from tkinter import E
import numpy as np
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import math
from geometry_msgs.msg import Pose2D
from tkinter import E
import numpy as np
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import math
from geometry_msgs.msg import Pose2D
# from cv2 import aruco


class main:
    def __init__(self):
        rospy.init_node('aruco_feedback_node')
        self.current_frame = None
        self.aruco_publisher = rospy.Publisher(
            'detected_aruco', Pose2D, queue_size=10)
        self.image_sub = rospy.Subscriber(
            'overhead_cam/image_raw', Image, self.callback)
        self.br = CvBridge()
        print("yo")
        # while not rospy.is_shutdown():
        # 	# pass
        # 	# print("repeat")
        # 	self.detect()

    def callback(self, data):
        br_frame = self.br.imgmsg_to_cv2(data, "mono8")
        
        self.current_frame = cv2.resize(br_frame, (500, 500), interpolation=cv2.INTER_LINEAR)

        marker_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
        param_markers = cv2.aruco.DetectorParameters_create()
		
        marker_corners, marker_IDs, reject = cv2.aruco.detectMarkers(
            self.current_frame, marker_dict, parameters=param_markers
        )

        if marker_corners:
            for ids, corners in zip(marker_IDs, marker_corners):
                cv2.polylines(
                    self.current_frame, [corners.astype(
                        np.int32)], True, (0, 0, 255), 4, cv2.LINE_AA
                )
                corners = corners.reshape(4, 2)
                corners = corners.astype(int)
                top_right = corners[1].ravel()
                cv2.putText(
                    self.current_frame,
                    f"id: {ids[0]}",
                    top_right,
                    cv2.FONT_HERSHEY_PLAIN,
                    1.3,
                    (200, 100, 0),
                    2,
                    cv2.LINE_AA,
                )
                x_centre = int((corners[1][0] + corners[3][0])/2)
                y_centre = int((corners[1][1] + corners[3][1])/2)
                centre = (x_centre, y_centre)
                cv2.circle(self.current_frame, centre, 2, (0, 0, 255), -1)
                x_horizontal = int((corners[1][0] + corners[2][0])/2)
                y_horizontal = int((corners[1][1] + corners[2][1])/2)

                horizontal = (x_horizontal, y_horizontal)

                cv2.line(self.current_frame, centre,
                         horizontal, (0, 255, 0), 2)

                inv_m1 = math.atan2((y_horizontal - y_centre),
                                    (x_horizontal - x_centre))
            
                aruco_msg.x = x_centre
                aruco_msg.y = y_centre
                aruco_msg.theta = inv_m1
                
                print(x_centre,y_centre,inv_m1)

                self.aruco_publisher.publish(aruco_msg)

        cv2.imshow("frame", self.current_frame)
        cv2.waitKey(10)


if __name__ == '__main__':
    aruco_msg = Pose2D()
    af = main()
    try:
        if not rospy.is_shutdown():
            rospy.spin()
    except rospy.ROSInterruptException as e:
        print(e)
