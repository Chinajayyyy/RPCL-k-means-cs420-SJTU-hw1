import numpy as np
import matplotlib.pyplot as plt
import random
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

#create datasets
data,label = make_blobs(n_samples=100,n_features=2,centers=3)

#init center position
random_center = []
final_center = []

#RPCL confirm n
num_RPCL = 0


#calculate distance between two points
def distance(p1,p2):
    dis = ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
    return dis

class center(object):
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y
        self.cnt = 0

def create_center():
    for i in range(5):
        random_center.append(center(x=random.randint(-9,9),y=random.randint(-9,9)))
        
def print_center():
    for i in range(len(random_center)):
        print (random_center[i].x,random_center[i].y,random_center[i].cnt)

def add_num():
    global num_RPCL
    num_RPCL += 1

def RPCL(data_input):
    scale = 0.05
    cnt = 1000
    #ran_data = data_input
    #random.shuffle(data_input)
    while (cnt>0):
 #       cnt += 1
        for index,i in enumerate(data_input):
            distances = []
            for c in random_center:
                distances.append(distance(i,(c.x,c.y)))
                

            #print distances
            winner_index = distances.index(max(distances))
            #print winner_index
            dlt_x = scale * (i[0] - random_center[winner_index].x)
            dlt_y = scale * (i[1] - random_center[winner_index].y)
            #print dlt_x,dlt_y
            random_center[winner_index].x += dlt_x
            random_center[winner_index].y += dlt_y
            distances[winner_index] = -1
            

            rival_index = distances.index(max(distances))
            dlt_x = scale * (i[0] - random_center[rival_index].x)
            dlt_y = scale * (i[1] - random_center[rival_index].y)
            random_center[rival_index].x -= dlt_x
            random_center[rival_index].y -= dlt_y

            #print winner_index,rival_index
            

            #print_center()

        #if(abs(dlt_x) + abs(dlt_y)) < 0.1:
            #break
        cnt = cnt - 1
    #print cnt

    for i in data_input:
        tmp_dis = 1000
        pos = None
        for index,c in enumerate(random_center):
            if distance(i,(c.x,c.y)) < tmp_dis:
                tmp_dis = distance(i,(c.x,c.y))
                pos = index
        random_center[pos].cnt += 1

    #for i in random_center:
#        print i.cnt

    min_point = 15
    get_list = []
    for index,c in enumerate(random_center):
        if c.cnt > min_point:
            get_list.append(index)
            add_num()
            final_center.append((c.x,c.y))

    #for i in get_list:
        #print i

    

#plt.scatter(data[:,0],data[:,1],c=label)
#plt.show()








def main():
    create_center()
    print_center()

    RPCL(data)
    arr1 = np.array(final_center)

    y_pre_withoutRPCL = KMeans(n_clusters=3).fit_predict(data)
    y_pre_withRPCL = KMeans(n_clusters=num_RPCL,init=arr1).fit_predict(data)


    plt.figure()
    plt.scatter(data[:,0],data[:,1],c=label)
    plt.show()
    plt.scatter(data[:,0],data[:,1],c=y_pre_withoutRPCL)
    plt.show()
    plt.scatter(data[:,0],data[:,1],c=y_pre_withRPCL)
    plt.show()

    print_center()

main()    

#RPCL(data)
#print_center()
#print data
