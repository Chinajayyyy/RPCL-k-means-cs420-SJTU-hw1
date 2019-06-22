import matplotlib.pyplot as plt
#plt.style.use('ggplot')

y1 = [12,12,10,10,4,4]
x1 = [3,10,15,20,50,100]

y2 = [12,8,4,3,4,4]
x2 = [3,10,15,20,50,100]

y3 = [2,3,3,4,4,4]
x3 = [3,10,15,20,50,100]

y4 = [15,0,0,0,0,0]
x4 = [0,0,15,20,50,150]

y5 = [4,4,4,4,4,4]
x5 = [0,5,10,15,50,150]

plt.plot(x5,y5,label='Really cluster',linewidth=3,color='black')
plt.plot(x1,y1,label='AIC',color='r',linewidth=3,marker='o',markerfacecolor='black',markersize=5)
plt.plot(x2,y2,label='BIC',color='y',linewidth=3,marker='o',markerfacecolor='black',markersize=5)
plt.plot(x3,y3,label='VBEM',color='green',linewidth=3,marker='o',markerfacecolor='black',markersize=5)
plt.plot(x4,y4)


plt.xlabel('sample_size')
plt.ylabel('div_size')
plt.title('AIC,BIC,VBEM compare')


plt.legend()
plt.show()
plt.savefig('sample_size_compare.png')
