#!/usr/bin/env python3

import rospy
    
if __name__ == '__main__':
    try:
        # Initialize the node with a name, e.g., 'name_robot'
        rospy.init_node('name_robot')

        # Log an informational message
        rospy.loginfo("Node has started")

        # Keep the node running until it is shut down
        rospy.spin()
    except rospy.ROSInterruptException:
        pass