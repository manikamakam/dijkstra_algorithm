import matplotlib.pyplot as plt
import numpy as np

plot_x = []
plot_y =[]
obs_map = np.zeros((300,200))
for x in range (0,300):    
    for y in range(0,200):

    	#l1 = y - 13*x + 140
    	#l2 = y - x -100
    	#l3 = 5*y + 6*x - 1050
    	#l4 = 5*y - 6*x - 150
    	#l5 = 5*y + 7*x - 1450
    	#l6 = y - 185
	#l1= 13*x - y - 140
	#l2= y - 185
	#l3= 7*x + 5*y - 1450
	#l4= 6*x - 5*y + 150
	#l5= 6*x + 5*y + 1050
	#l6= x - y +100
	
	l1= 13*x - y - 140
	l2= 7*x +5*y - 1110
	l3= x - y + 100
	
	l4 = y - 185
	l5 = 7*x - 5*y + 400
	
	
	#l6 = 7*x + 5*y - 1450
	#l7 = 6*x - 5*y + 150
	#l8 = 6*x + 5*y - 1050
	
	 
        if (l1 >=0 and l2<=0 and l3<=0) or (l3>=0 and l4<=0 and l5<=0): #and l7<=0 and l8>=0):
            print("x:", x)
            print("y:", y)
            obs_map[x][y] = 1
            plot_x.append(x)
            plot_y.append(y) 

for i in range(300):
        plot_x.append(i)
        plot_y.append(0)
        obs_map[i][0] = 1
for i in range(300):
        plot_x.append(i)
        plot_y.append(200)
        obs_map[i][199] = 1
for i in range(200):
        plot_x.append(0)
        plot_y.append(i)
        obs_map[0][i] = 1
for i in range(200):
        plot_x.append(300)
        plot_y.append(i)
        obs_map[299][i] = 1

plt.plot(plot_x,plot_y,".k")
plt.ylim((0,200))
plt.xlim((0,300))
plt.show()
