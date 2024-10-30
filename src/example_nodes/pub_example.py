#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
import time

from std_msgs.msg import String


class PublisherClass(object): # The name of the class is PublisherClass

    def __init__(self):
        """
        Init method.
        """
        # Class variables

        #self.__pub = rospy.Publisher("name_topic", msgtype, queue_size=10)
        self.__pub = rospy.Publisher("example_topic", String, queue_size=10) # Name of the topic: *****
                                                                                # Type of the msg: - rostopic info /name_topic --> rostopic info *****
                                                                                #                   It is a ******
                                                                                # Queue Size: **** 

        time.sleep(3)

        #Start the code of the node
        self.main()

    def main (self):

        rospy.loginfo(" Publisher..." )
        text = "Hello World" # String Variable
        self.__pub.publish(text) # Use this method to publish a msg in the topic "*****"
        rospy.loginfo(" I send the msg: %s" , text )


if __name__ == '__main__':
    try:
        # Initialize the node with a name, e.g., '******'
        name = "publish_node"
        rospy.init_node(name)

        # Create the class
        node = PublisherClass()

        # Log an informational message
        rospy.loginfo("Node %s has started", name)

        # Keep the node running until it is shut down
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
        