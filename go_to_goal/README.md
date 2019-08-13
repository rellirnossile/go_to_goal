# Go to goal

This project has as its objetive to implement a control strategy to a differential robot, making it to go to a desired position.  

### Prerequisites

Firstly make sure that you already haved to maked the ros tutorials it can be find at [ROS Tutorials](http://wiki.ros.org/pt_BR/ROS/Tutorials)

## Getting Started

1. Copy the contents of the src folder into your catkin workspace 'src' folder. Make sure the permissions are set to o+rw on your files and directories.

2. in yout catkin_ws ($CATKIN) folder, execute
    ```sh
    $ catkin_make
    ```
3. Source the environment for each terminal you work in. If necessary, add the line to your .bashrc 
    ```sh
    $ . $CATKIN/devel/setup.bash
4. Inside the 'launch' folder you can find the file *launch.launch*

5. To run the node
    ```sh
    $ roslaunch go_to_goal launch.launch    
    ``` 
# Running the service
This service that use to insert the target coordinates.
1. Open a new terminal
    ```
    $ rosservice call /goal_coordinates
    ```
        
    >As a tip use tab for autocomplet
    
    ```
    $ rosservice call /goal_coordinates "x: 0.0 y: 0.0 tolerance: 0.0"
    ```
