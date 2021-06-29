#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.actions import RegisterEventHandler
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir

from launch_ros.actions import Node

def generate_launch_description():
    pause_node = Node(
            name='pause',
            package='launch_bug',
            executable='pause_node',
        )

    included_launch_description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/empty.launch.py']),
    )

    launch_description = LaunchDescription(
        [
            pause_node,
        ],
    )

    register_event_handler_for_exit_pause = RegisterEventHandler(
        OnProcessExit(
            target_action=pause_node,
            on_exit=included_launch_description,
        )
    )

    launch_description.add_action(register_event_handler_for_exit_pause)
    return launch_description
