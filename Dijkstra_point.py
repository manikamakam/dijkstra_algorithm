

import matplotlib.pyplot as plt
import numpy as np
import heapq
import math
import time
import argparse


def ObstacleMap():
    plot_x = []
    plot_y =[]
    obs_map = np.zeros((200,100))
    for x in range (0,200):    
        for y in range(0,100):
            l1 = x - 90
            l2 = -x+ 110
            l3 = y - 40
            l4 = 60 - y

            c1 = (x - 160)**2 + (y - 50)**2 - (15)**2   

            if (l1 >=0 and l2>=0 and l3>=0 and l4>=0) or (c1 <=0):
                obs_map[x][y] = 1
                plot_x.append(x)
                plot_y.append(y) 

    for i in range(200):
            plot_x.append(i)
            plot_y.append(0)
            obs_map[i][0] = 1
    for i in range(200):
            plot_x.append(i)
            plot_y.append(100)
            obs_map[i][99] = 1
    for i in range(100):
            plot_x.append(0)
            plot_y.append(i)
            obs_map[0][i] = 1
    for i in range(100):
            plot_x.append(200)
            plot_y.append(i)
            obs_map[199][i] = 1

    plt.plot(plot_x,plot_y,".k")
    plt.ylim((0,100))
    plt.xlim((0,200))
    #plt.show()
    return plot_x, plot_y, obs_map



# Defining actions along with their cost
def ActionModel():                
    actions = [[1,0,1], [0,1,1], [-1,0,1], [0,-1,1],
             [1,1,math.sqrt(2)], [1,-1,math.sqrt(2)],
             [-1,-1,math.sqrt(2)], [-1,1,math.sqrt(2)]]
    return actions


def DijkstraAlg(start_node,goal_node, obs_map,animation):
    start = (0,start_node,None)       # cost, node, parent node
    goal = (0,goal_node,None)
    actions = ActionModel()
    print(animation)
    
    nodes = []
    path_nodes = []
    heapq.heappush(nodes,(start))
    obs_map[start[1][0]][start[1][1]] = 1
    x_explored=[]
    y_explored=[]

    while len(nodes)>0:
       
        # print(nodes)
        current_node = heapq.heappop(nodes)
        heapq.heappush(path_nodes,current_node)
        x_explored.append(current_node[1][0])
        y_explored.append(current_node[1][1])
        # print("current node")
        # print(current_node)
        # print(path_nodes)

        #x_explored.append(current_node[1][0])
        #y_explored.append(current_node[1][1])

        for new_pos in actions:
            
            node = (current_node[1][0] + new_pos[0],
                             current_node[1][1] + new_pos[1])
            node_cost = current_node[0] + new_pos[2]
            
            
            node_parent = current_node[1]
            
            # Check within range
            #if node[0] > (len(obs_map) - 1) or node[0] < 0 or node[1] > (len(obs_map[0]) -1) or node[1] < 0:
                #continue
        
            if obs_map[node[0]][node[1]] != 0:
                continue
            
            obs_map[node[0]][node[1]] = 1
    
            new_node = (node_cost,node,node_parent)                
            heapq.heappush(nodes,(new_node))


        if current_node[1] == goal[1]:
            print('Goal reached')
            path = []
            #print(path_nodes)
            length = len(path_nodes)
            path.append(path_nodes[length-1][1])
            #print(path)
            parent = path_nodes[length-1][2]
            #print(parent)
            while parent != None: 
                for i in range(length):
                    X = path_nodes[i]
                    #print("xxxxxxxxxxxxxxxxxxxxxxx")
                    #print(X[1])
                    if X[1] == parent:
                        parent = X[2]
                        #print("yyyyyyyyyyyy")
                        #print(parent)
                        path.append(X[1])
            return path

        if (len(x_explored))%500 == 0:
            #print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            #print(animation)
            if animation:
                #print("YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
                plt.plot(x_explored,y_explored, "3c")
                plt.pause(0.00001)
    

def main():
    Parser = argparse.ArgumentParser()
    Parser.add_argument('--input')
    Parser.add_argument('--animation')
    
    Args = Parser.parse_args()
    animation = Args.animation
    input=Args.input
    if input ==1:
        start_x = int(input('Enter the x-coordinate of start point: '))        
        start_y = int(input('Enter the y-coordinate of start point: '))        
        goal_x = int(input('Enter the x-coordinate of goal point: '))        
        goal_y = int(input('Enter the y-coordinate of goal point: '))        
    else: 
        start_x = 10
        start_y = 20
        goal_x = 170
        goal_y = 90
    #start_time = time.time()
    start_node = (start_x, start_y)
    goal_node = (goal_x, goal_y)

    plot_x, plot_y,obs_map = ObstacleMap()

    if start_node in zip(plot_x,plot_y):
        print('Start node is in obstacle space. Please give a different node')
    elif goal_node in zip(plot_x,plot_y) :    
        print('Goal node is in obstacle space. Please give a different node')
    else:
        rev_path = DijkstraAlg(start_node,goal_node, obs_map,animation)  
        path = rev_path[::-1]
        #print(path)

        x_path = [path[i][0] for i in range(len(path))]
        y_path = [path[i][1] for i in range(len(path))]
        
        plt.plot(start_node[0], start_node[1], "Dw")
        plt.plot(goal_node[0], goal_node[1], "Dg")        
        
        plt.plot(x_path,y_path,"-r")
        plt.show()
        






if __name__ == '__main__':
    main()

