#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

class Subscriber(object):
    def __init__(self):
        """
        Init method.
        """
        # Class variables

        #self.__sub = rospy.Subscriber("name_topic", msgtype, self.callback)
        self.__sub = rospy.Subscriber("example_topic", String, self.print) # Name of the topic: *****
                                                                                # Type of the msg: - rostopic info /name_topic --> rostopic info *****
                                                                                #                   It is a ******
                                                                                # Callback function = ******

        #Start the code of the node
        self.main()

    def main (self):

        rospy.loginfo(" Hello I'm a subscriber..." )

    def print(self, data):
        """
        Callback function
        @input data: String - It's the msg
        """
        msg = data.data
        rospy.loginfo(" Hello I'm the callback subscriber..." )
        rospy.loginfo(" The msg recived is %s", msg)





if __name__ == '__main__':
    try:
        # Initialize the node with a name, e.g., '*****'
        rospy.init_node('name_robot_subscriber')
        node = Subscriber()
        # Log an informational message
        rospy.loginfo("Node has started")

        # Keep the node running until it is shut down
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
        
        