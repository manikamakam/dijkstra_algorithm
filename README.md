# dijkstra_algorithm
Implementation of Dijkstra's algorithm in python

## Authors

 1. Sri Manika Makam
 2. Sai Praveen Bhamidipati

## Overview

 Implemented the Dijkstra algorithm for a point robot and rigid robot.

## Dependencies

 1. numpy library
 2. matplotlib library
 3. headpq library
 4. math library
 5. time library
 6. argparse library
 7. Python 2.7
 8. ubuntu 16.04
 
## Instructions to run

1. For point robot, the inputs are coordinates of start node and goal node taken in int. 

Go to the directory where code is present and run the following command for point robot

```
python Dijkstra_point.py --user_input 1 --animation 0
```
If user_input is 1, then user is allowed to give inputs of his wish. If user_input is 0, it takes start node as (5,5) and goal node is (295,195). 

If animation is 0, animation of exploration nodes is not shown. If 1, animation is shown. 

2. 1. For rigid robot, the inputs are coordinates of start node and goal node taken as int; robot radius and clearance taken as float. 

Go to the directory where code is present and run the following command for rigid robot

```
python Dijkstra_rigid.py --user_input 1 --animation 0
```
If user_input is 1, then user is allowed to give inputs of his wish. If user_input is 0, it takes start node as (5,5), goal node is (295,195), robot radius as 2 and clearance as 2.  

If animation is 0, animation of exploration nodes is not shown. If 1, animation is shown. 

## Output

The time taken to find the path for point robot is 1.39 seconds. 
The time taken to find the path for point robot is 1.54 seconds. 


## Note

The optimal path is found just in seconds as displayed in the console, but the visualization of explored nodes takes much longer time. So, to view only the path, give argument 'animation' as 0 and run the scripts. 

