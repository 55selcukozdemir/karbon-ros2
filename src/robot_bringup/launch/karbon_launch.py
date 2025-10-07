from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package="control",
                executable="car_servo",
                name="car_control_test",
                output="screen"
            ),
            Node(
                package="sensor",
                executable="motor_speet",
                name="motor_speet_test",
                
            ),
             Node(
                package="rosbridge_server",
                executable="rosbridge_websocket",
                name="rosbridge_websocket",
                # parameters=[{"port": 8080}]
            )
        ]
    )