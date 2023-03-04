#!/usr/bin/env python3

import rospy
import cv2
import numpy as np
from geometry_msgs.msg import Pose2D
from std_msgs.msg import String

class main:
	def __init__(self):
		rospy.init_node('snapchat_contour', anonymous=True)
		print("hi")
		contourPub = rospy.Publisher('/contours', String, queue_size=10)
		# pub = rospy.Publisher('snap_cordinates', Pose2D, queue_size=10)
		# got = rospy.Subscriber('reached_snap', Pose2D, self.callback)
		# self.x_previous = self.x_present = 0
		while not rospy.is_shutdown():
			
			image = cv2.imread('/home/diksha/catkin_ws/src/eyrc22_HB_1257/snapchat.jpg')
			if image is None:
				continue
			image = cv2.resize(image, (500, 500), interpolation=cv2.INTER_LINEAR)
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			edged = cv2.Canny(gray, 30, 200)
			contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
			cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
			xList, yList, xListFinal, yListFinal = [], [], [], []
			for i in contours:
				xList.clear()
				yList.clear()
				for j in i:
					xList.append(int(j[0][0]))
					yList.append(int(j[0][1]))

				xListFinal.append(xList)
				yListFinal.append(yList)
			cData.data = str([xListFinal,yListFinal])
			contourPub.publish(cData)
			# print(cData)
			cv2.imshow('huh', image)
			cv2.waitKey(1)
		

if __name__ == "__main__":
	
	cData = String()
	main()
	try:
		if not rospy.is_shutdown():
			rospy.spin()
	except rospy.ROSInterruptException as e:
		print(e)