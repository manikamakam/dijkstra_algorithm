import matplotlib.pyplot as plt
import numpy as np

plot_x = []
plot_y =[]
obs_map = np.zeros((300,200))
for x in range (0,300):    
    for y in range(0,200):
        #l1= 13*x - y - 140
        #l2= y - 185
        #l3= 7*x + 5*y - 1450
        #l4= 6*x - 5*y + 150
        #l5= 6*x + 5*y - 1050
        #l6= x - y +100
        l1= 13*x - y - 140
        l2= 7*x +5*y - 1110
        l3= x - y + 100
        l4 = 7*x - 5*y + 400
        l5 = 7*x + 5*y - 1450
        l6 = 6*x - 5*y + 150
        l7 = 6*x + 5*y - 1050
        l8 = y-185
        l9 = x -25
        l10 = x - 75
        l11 = y -150

        c = (x - 225)**2 + (y - 150)**2 - (25)**2
        e = 400*((x - 150)**2) + 1600*(y - 100)**2 - 640000
        
        rh1 = 3*x - 5*y -475
        rh2 = 3*x + 5*y -875
        rh3 = 3*x -5*y -625
        rh4 = 3*x + 5*y -725

        #rec1 = 8.66*x - 5*y +77.267
        rec1 = 1.732*x -y + 15.46
        #rec2 = x +2*y -177.37
        rec2 = 0.57*x + y - 96.13
        #rec3 = 8.66*x - 5*y -672.7
        rec3 = 1.732*x -y - 134.54
        rec4 = 0.57*x + y -84.15

        if (l1 >=0 and l2<=0 and l3<=0) or (l4>=0 and l5<=0 and l6<=0 and l7>=0) or (l8<=0 and l9>=0 and l10<=0 and l11>=0) or c<=0 or e<=0 or (rh1>=0 and rh2<=0 and rh3<=0 and rh4>=0) or (rec1>=0 and rec2<=0 and rec3<=0 and rec4>=0):
        #if (l1 >=0 and l2<=0 and l3<=0 and l4<=0 and l5>=0 and l6<=0):
            # print("x:", x)=
            # print("y:", y)
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
