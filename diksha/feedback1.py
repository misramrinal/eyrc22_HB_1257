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
import argparse
# from cv2 import aruco
br_data = None

class main:
    def __init__(self):
        rospy.init_node('aruco_feedback_node')
        self.current_frame = None
        self.aruco_publisher = rospy.Publisher(
            'detected_aruco', Pose2D, queue_size=10)
        rospy.Subscriber(
            'usb_cam/image_rect', Image, self.callback)
        self.br = CvBridge()
        print("yo")
        while not rospy.is_shutdown():
            global br_data
            x_centre1=x_centreC=y_centreC=x_centre2=y_centre1=y_centre2=inv_m1=inv_mC=inv_m2=inv_mv3=inv_m4=x_centre3=x_centre4=y_centre3=y_centre4=0
            centre1=centre2 =centre3= centre4=centreC=centre=(0,0)
        ##      **Aruco detection for boundary**    
            marker_dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
            param_markers = cv2.aruco.DetectorParameters_create()
            
            marker_corners, marker_IDs, reject = cv2.aruco.detectMarkers(self.current_frame, marker_dict, parameters=param_markers)

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
                    if(self.ids==4):
                    
                        x_centre1 = int((self.corners[1][0] + self.corners[3][0])/2)
                        y_centre1 = int((self.corners[1][1] + self.corners[3][1])/2)
                        centre1 = (x_centre1, y_centre1)
                        cv2.circle(self.current_frame, centre1, 2, (0, 0, 255), -1)
                        x_horizontal = int((self.corners[1][0] + self.corners[2][0])/2)
                        y_horizontal = int((self.corners[1][1] + self.corners[2][1])/2)

                        horizontal = (x_horizontal, y_horizontal)

                        cv2.line(self.current_frame, centre1, horizontal, (0, 255, 0), 2)

                        inv_m1 = math.atan2((y_horizontal - y_centre1),
                                            (x_horizontal - x_centre1))
                        
                        #print(x_centre1,y_centre1,inv_m1)
                    if(self.ids==8):
                    
                        x_centre2 = int((self.corners[1][0] + self.corners[3][0])/2)
                        y_centre2 = int((self.corners[1][1] + self.corners[3][1])/2)
                        centre2 = (x_centre2, y_centre2)
                        cv2.circle(self.current_frame, centre1, 2, (0, 0, 255), -1)
                        x_horizontal = int((self.corners[1][0] + self.corners[2][0])/2)
                        y_horizontal = int((self.corners[1][1] + self.corners[2][1])/2)

                        horizontal = (x_horizontal, y_horizontal)

                        cv2.line(self.current_frame, centre2, horizontal, (0, 255, 0), 2)

                        inv_m2 = math.atan2((y_horizontal - y_centre2),
                                            (x_horizontal - x_centre2))
                        
                        #print(x_centre2,y_centre2,inv_m1)
                    if(ids==10):
                    
                        x_centre3 = int((corners[1][0] + corners[3][0])/2)
                        y_centre3 = int((corners[1][1] + corners[3][1])/2)
                        centre3 = (x_centre3, y_centre3)
                        cv2.circle(self.current_frame, centre3, 2, (0, 0, 255), -1)
                        x_horizontal = int((corners[1][0] + corners[2][0])/2)
                        y_horizontal = int((corners[1][1] + corners[2][1])/2)

                        horizontal = (x_horizontal, y_horizontal)

                        cv2.line(self.current_frame, centre3,   horizontal, (0, 255, 0), 2)

                        inv_m3 = math.atan2((y_horizontal - y_centre3),
                                            (x_horizontal - x_centre3))
                        
                        #print(x_centre3,y_centre3,inv_m1)
                    
                    if(ids==12):
                        x_centre4 = int((corners[1][0] + corners[3][0])/2)
                        y_centre4 = int((corners[1][1] + corners[3][1])/2)
                        centre4 = (x_centre4, y_centre4)
                        cv2.circle(self.current_frame, centre4, 2, (0, 0, 255), -1)
                        x_horizontal = int((corners[1][0] + corners[2][0])/2)
                        y_horizontal = int((corners[1][1] + corners[2][1])/2)

                        horizontal = (x_horizontal, y_horizontal)

                        cv2.line(self.current_frame, centre4, horizontal, (0, 255, 0), 2)

                        inv_m4 = math.atan2((y_horizontal - y_centre4),
                                            (x_horizontal - x_centre4))
                    
                        #print(x_centre4,y_centre4,inv_m1)

                    x_centre =(x_centre1+x_centre2+x_centre3+x_centre4)/4
                    y_centre =(y_centre1+y_centre2+y_centre3+y_centre4)/4
                
                    M = cv2.getPerspectiveTransform(np.float32([centre1, centre2, centre3, centre4]),np.float32([(0,500),(0,0),(500,0),(500,500)]))
                    self.dst = cv2.warpPerspective(self.current_frame, M, (500,500))
                   
                    cv2.line(self.current_frame, (x_centre1, y_centre1), (x_centre2, y_centre2), (255, 0, 0), 2)
                    cv2.line(self.current_frame, (x_centre2, y_centre2), (x_centre3, y_centre3), (255, 0, 0), 2)
                    cv2.line(self.current_frame, (x_centre3, y_centre3), (x_centre4, y_centre4), (255, 0, 0), 2)
                    cv2.line(self.current_frame, (x_centre4, y_centre4), (x_centre1, y_centre1), (255, 0, 0), 2)
            ##    **ARUCO DETECTION FOR HOLA BOT**
                marker_corners, marker_IDs, reject = cv2.aruco.detectMarkers(
                self.dst, self.marker_dict, parameters=self.param_markers)
                if self.marker_corners:
                    for ids, corners in zip(self.marker_IDs, self.marker_corners):
                        cv2.polylines(
                            self.dst, [corners.astype(
                                np.int32)], True, (0, 0, 255), 4, cv2.LINE_AA
                        )
                        corners = corners.reshape(4, 2)
                        corners = corners.astype(int)
                        top_right = corners[1].ravel()
                        cv2.putText(
                            self.dst,
                            f"id: {ids[0]}",
                            top_right,
                            cv2.FONT_HERSHEY_PLAIN,
                            1.3,
                            (200, 100, 0),
                            2,
                            cv2.LINE_AA,
                        )
                        if(ids==15):
                            x_centreC = int((corners[1][0] + corners[3][0])/2)
                            y_centreC = int((corners[1][1] + corners[3][1])/2)
                            centreC = (x_centreC, y_centreC)
                            cv2.circle(self.dst, centreC, 2, (0, 0, 255), -1)
                            x_horizontal = int((corners[1][0] + corners[2][0])/2)
                            y_horizontal = int((corners[1][1] + corners[2][1])/2)

                            horizontal = (x_horizontal, y_horizontal)

                            cv2.line(self.dst, centreC, horizontal, (0, 255, 0), 2)

                            inv_mC = math.atan2((y_horizontal - y_centreC),
                                                (x_horizontal - x_centreC))
                        
                            print(x_centreC,y_centreC,inv_mC)
                        
                        aruco_msg.x = x_centreC
                        aruco_msg.y = y_centreC
                        aruco_msg.theta = inv_mC
                            
                        self.aruco_publisher.publish(aruco_msg)

                cv2.imshow("frame1", self.current_frame)
                cv2.imshow("frame", self.dst)
                cv2.waitKey(1)
    def callback(self, data):
        
        self.br_frame = self.br.imgmsg_to_cv2(data, "rgb8")
        self.current_frame = cv2.resize(self.br_frame, (500, 500), interpolation=cv2.INTER_LINEAR)    
if __name__ == '__main__':
    aruco_msg = Pose2D()
    af = main()
    try:
        if not rospy.is_shutdown():
            rospy.spin()
    except rospy.ROSInterruptException as e:
        print(e)
