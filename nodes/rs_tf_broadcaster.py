#!/usr/bin/env python
__author__ = 'mandeep'

import roslib
roslib.load_manifest('realsense_tf')
import rospy

import tf


def broadcast():
    # values relative to robot
    xx = 0.0
    yy = 0.0
    zz = 0.0
    ex = 0.0
    ey = 0.0
    ez = 0.0

    br = tf.TransformBroadcaster()
    br.sendTransform((xx, yy, zz),
                     tf.transformations.quaternion_from_euler(ex, ey, ez),
                     rospy.Time.now(),
                     "realsense",
                     "world")  #world should be replaced by robot


if __name__ == '__main__':
    rospy.init_node('rs_tf_broadcaster')
    dur = rospy.Rate(10)
    while (not rospy.is_shutdown()):
        broadcast()
        dur.sleep()