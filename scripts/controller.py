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
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:		[ HB_1257 ]
# Author List:		[ Mrinal Misra, Diksha Kumari]
# Filename:		controller.py
# Functions:	signal_handler, task2_goals_Cb, aruco_feedback_Cb, main
#			[ Comma separated list of functions in this file ]
# Nodes:		publishing node: front_wheel_force, right_wheel_force, left_wheel_force
#			    subscribing node: detected_aruco, task2_goals


################### IMPORT MODULES #######################

import rospy
import signal		# To handle Signals by OS/user
import sys		# To handle Signals by OS/user

from geometry_msgs.msg import Wrench 	# Message type used for publishing force vectors
from geometry_msgs.msg import PoseArray	# Message type used for receiving goals
from geometry_msgs.msg import Pose2D		# Message type used for receiving feedback

import time
from math import atan2	
import numpy as np 

from tf.transformations import euler_from_quaternion

PI = 3.14
x_goals = [50,350,50,250,250]
y_goals = [350,50,50,350,50]
theta_goals = [0.785, 2.335, -2.335, -0.785, 0]
right_wheel_pub = left_wheel_pub = front_wheel_pub = hola_x = hola_y = hola_theta = 0

def signal_handler(sig, frame):
	  
	# NOTE: This function is called when a program is terminated by "Ctr+C" i.e. SIGINT signal 	
	print('Clean-up !')
	sys.exit(0)

def task2_goals_Cb(msg):
	global x_goals, y_goals, theta_goals
	x_goals.clear()
	y_goals.clear()
	theta_goals.clear()

	for waypoint_pose in msg.poses:
		x_goals.append(waypoint_pose.position.x)
		y_goals.append(waypoint_pose.position.y)

		orientation_q = waypoint_pose.orientation
		orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
		theta_goal = euler_from_quaternion (orientation_list)[2]
		theta_goals.append(theta_goal)

def aruco_feedback_Cb(msg):
	global hola_x, hola_y, hola_theta
	hola_x = msg.x
	hola_y = msg.y
	hola_theta = msg.theta

def main():

	rospy.init_node('controller_node')

	signal.signal(signal.SIGINT, signal_handler)

	# NOTE: You are strictly NOT-ALLOWED to use "cmd_vel" or "odom" topics in this task
	#	Use the below given topics to generate motion for the robot.
	right_wheel_pub = rospy.Publisher('/right_wheel_force', Wrench, queue_size=10)
	front_wheel_pub = rospy.Publisher('/front_wheel_force', Wrench, queue_size=10)
	left_wheel_pub = rospy.Publisher('/left_wheel_force', Wrench, queue_size=10)
	

	rospy.Subscriber('detected_aruco',Pose2D,aruco_feedback_Cb)
	rospy.Subscriber('task2_goals',PoseArray,task2_goals_Cb)
	
	
	Kp = 10
	kp_z = 20
	while not rospy.is_shutdown():
		global hola_x, hola_y, hola_theta
		i=0
		while (i <len(theta_goals)):
			rate = rospy.Rate(10)
			error_x = x_goals[i] - hola_x
			error_y = y_goals[i] - hola_y
			error_z =hola_theta-theta_goals[i]
			# abs_angle_diff=abs(abs(hola_theta)-abs(theta_goals[i]))
			align_error = hola_theta - 0
			
			
			force_x = Kp*error_x 
			force_y = Kp*error_y 

			# if abs_angle_diff > 0.1:
			# 	if error_z> 3.14:
			# 		error_z = error_z-6.28
			# 	elif error_z < -3.14:
			# 		error_z = error_z+6.28
			# 	else:
			# 		error_z=error_z

			bal_ori = kp_z*error_z 
			align = 14*kp_z*align_error

			if(abs(hola_theta)> 0.1 and abs(error_x) > 2 and abs(error_y) > 2):
				A1=([0.667,0,-0.333],
				[-0.333,0.577,-0.333],
				[-0.333,-0.577,-0.333])
				A2=([0,0,align])
				A3=np.dot(A1,A2)

				force_x1=A3[0]
				force_y1=A3[1]
				bal_ori1=A3[2]
				print("1")
			else:
				if(abs(error_x) > 1 or abs(error_y) > 1):
					A1=([0.667,0,-0.333],
					[-0.333,0.577,-0.333],
					[-0.333,-0.577,-0.333])
					A2=([force_x,force_y,0])
					A3=np.dot(A1,A2)

					force_x1=A3[0]
					force_y1=A3[1]
					bal_ori1=A3[2]
					print("2")
	
			if(abs(error_x) <= 1 and abs(error_y) <=1):
				A1=([0.667,0,-0.333],
				[-0.333,0.577,-0.333],
				[-0.333,-0.577,-0.333])
				A2=([0,0,bal_ori])
				A3=np.dot(A1,A2)

				force_x1=A3[0]
				force_y1=A3[1]
				bal_ori1=A3[2]
				print("3")
				if(abs(error_z) <= 0.09):
					
					print("goal reached")
					i=i+1
					time.sleep(1.2)
			wrench.force.x = force_x1
		
			wrench1.force.x = force_y1
			
			wrench2.force.x = bal_ori1
			front_wheel_pub.publish(wrench)
			left_wheel_pub.publish(wrench2)
			right_wheel_pub.publish(wrench1)
			# w = -7*(hola_theta)
			# x = force_x
			# y = force_y
	
			# if(abs(hola_theta)> 0.0174 and abs(error_x) > 2 and abs(error_y) > 2):
			# # 	front_x = front_y = left_x = left_y = right_x = right_y = 0

			# 	torque_z = align

				# if(abs(hola_theta)> 0.0174 and abs(error_x) > 1 and abs(error_y) > 1):
			# 	front_x = -0.33*w
			# 	right_x = -0.33*w
			# 	left_x = -0.33*w
			# 	print("1")

			# else:
			# 	if(abs(error_x) > 1 and abs(error_y)> 1):
			# 		front_x = 0.667*x
			# 		right_x = -0.33*x + 0.577*y 
			# 		left_x = -0.33*x - 0.577*y
			# 		print("2A")

			# 	elif(abs(error_y) > 1 and abs(error_x)<= 1):
			# 		front_x = 0
			# 		right_x = 0.577*y
			# 		left_x = -0.577*y
			# 		print("2B")
			# 	elif(abs(error_x)> 1 and abs(error_y)<= 1):
			# 		front_x = 0.667*x 
			# 		right_x = -0.33*x 
			# 		left_x = -0.33*x 
			# 		print("2C")
			# 	else:
			# 		front_x = 0
			# 		right_x = 0
			# 		left_x = 0
			# 		print("2D")

			# if abs(error_x) < 1 and abs(error_y) < 1:
			# 	if(abs(error_z) > 0.0174):
			# 		front_x = -0.33*bal_ori
			# 		right_x = -0.33*bal_ori
			# 		left_x = -0.33*bal_ori
			# 		print("3A")

			# 	else:
			# 		front_x = 0
			# 		right_x = 0
			# 		left_x = 0
			# 		print("goal reached")
			# 		time.sleep(1)
			# 		i = i+1# if(abs(error_x) > 1 and abs(error_y) > 1 ):
					# front_x = -0.33*x + 0.58*y + 0.33*w
					# right_x = -0.33*x + -0.58*y + 0.33*w
					# left_x = 0.67*x + 0.33*w
				
			# if(abs(hola_theta)> 0.0174 and abs(error_x) > 1 and abs(error_y) > 1):
			# 	front_x = -0.33*w
			# 	right_x = -0.33*w
			# 	left_x = -0.33*w
			# 	print("1")

			# else:
			# 	if(abs(error_x) > 1 and abs(error_y)> 1):
			# 		front_x = 0.667*x
			# 		right_x = -0.33*x + 0.577*y 
			# 		left_x = -0.33*x - 0.577*y
			# 		print("2A")

			# 	elif(abs(error_y) > 1 and abs(error_x)<= 1):
			# 		front_x = 0
			# 		right_x = 0.577*y
			# 		left_x = -0.577*y
			# 		print("2B")
			# 	elif(abs(error_x)> 1 and abs(error_y)<= 1):
			# 		front_front_x = 0
			# 		right_x = 0
			# 		left_x = 0
			# 		print("goal reached")
			# 		time.sleep(1)

			# 		i = i+1
			# 		front_x = 0
			# 		right_x = 0
			# 		left_x = 0
			# 		print("2D")
			# wrench.force.x = force_x1
		
			# wrench.force.xfront_x = 0
			# 		right_x = 0
			# 		left_x = 0
			# 		print("goal reached")
			# 		time.sleep(1)
			# 		i = i+1")

			# 	else:
			# 		front_x = 0
			# 		right_x = 0
			# 		left_x = 0
			# 		print("goal reached")
			# 		time.sleep(1)
			# 		i = i+1
				

			
			

			rate.sleep()


if __name__ == "__main__":
	wrench = Wrench()
	wrench1 = Wrench()
	wrench2 = Wrench()
	main()
	try:
		if not rospy.is_shutdown():
			rospy.spin()
	except rospy.ROSInterruptException as e:
		print(e)

