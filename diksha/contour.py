#!/usr/bin/env python3

import rospy
import cv2
import numpy as np
from geometry_msgs.msg import Pose2D

class main:
	def __init__(self):
		rospy.init_node('snapchat_contour', anonymous=True)
		print("hi")
		pub = rospy.Publisher('snap_cordinates', Pose2D, queue_size=10)
		got = rospy.Subscriber('reached_snap', Pose2D, self.callback)
		self.x_previous = self.x_present = 0
		while not rospy.is_shutdown():
			
			image = cv2.imread('/home/diksha/catkin_ws/src/eyrc22_HB_1257/snapchat.jpg')
			if image is None:
				continue
			image = cv2.resize(image, (500, 500), interpolation=cv2.INTER_LINEAR)
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			edged = cv2.Canny(gray, 30, 200)
			contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
			cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
			
			for cnt in contours:
				approx = cv2.approxPolyDP(cnt, 0.0006 * cv2.arcLength(cnt, True), True) 
				n = approx.ravel() 
				i = 0
				for j in n : 
					if(i % 2 == 0):
						x = n[i]
						y = n[i+1]
						string = str(x)+" "+str(y)
						cv2.putText(image, string, (x, y), cv2.FONT_HERSHEY_SIMPLEX , 0.5, (255, 0, 0))
					i=i+1
				i = 0
				for j in n:
					if(i%2==0):
						x = n[i]
						y = n[i+1]
						string = str(x)+" "+str(y)
						cv2.putText(image, string, (x, y), cv2.FONT_HERSHEY_SIMPLEX , 0.5, (0, 0, 255))
						pose.x = x
						pose.y = y
						pub.publish(pose)
					if(self.x_present > self.x_previous):
						i=i+1
						self.x_previous = self.x_present
					
			cv2.imshow('huh', image)
				
			cv2.waitKey(1)
	def callback(self,msg):
		self.x_present = msg.x
		

if __name__ == "__main__":
	
	pose = Pose2D()
	main()
	try:
		if not rospy.is_shutdown():
			rospy.spin()
	except rospy.ROSInterruptException as e:
		print(e)