import matplotlib.pyplot as plt
import numpy as np

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
plt.show()
