import matplotlib.pyplot as plt
#plt.style.use('ggplot')

y1 = [5,7,8,8,9,10]
x1 = [5,6,7,8,9,10]

y2 = [5,5,5,7,7,8]
x2 = [5,6,7,8,9,10]

y3 = [4,5,7,9,9,9]
x3 = [5,6,7,8,9,10]

y4 = [15,0,0,0,0,0]
x4 = [0,0,7,8,9,10]

y5 = [5,6,7,8,9,15]
x5 = [5,6,7,8,9,15]

plt.plot(x5,y5,label='Really cluster',linewidth=3,color='black')
plt.plot(x1,y1,label='AIC',color='r',linewidth=3,marker='o',markerfacecolor='black',markersize=5)
plt.plot(x2,y2,label='BIC',color='y',linewidth=3,marker='o',markerfacecolor='black',markersize=5)
plt.plot(x3,y3,label='VBEM',color='green',linewidth=3,marker='o',markerfacecolor='black',markersize=5)
plt.plot(x4,y4)


plt.xlabel('clusters_num')
plt.ylabel('div_size')
plt.title('AIC,BIC,VBEM compare')


plt.legend()
plt.show()
#plt.savefig('sample_size_compare.png')
