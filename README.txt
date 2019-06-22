RPCL_k-mean.py
line8,n_samples是整个数据生成的个数 注意调整了n_sample的值之后，需要调整line93的min_point变量，一般调整为n_samples的15%。
运行程序后输出的数据(x,y,z)，(x,y)表示所有中心点在平面上的坐标，z表示每个中心点被分配到的点的数目。
依次输出的三张图表示初始的数据点，普通k-mean的聚类以及RPCL_k-mean的比较。

GMM.py内是比较不同的sample_size下三种模型的聚类效果。如果需要调整数据，只要在line12上修改n_samples的值，同时在line43，line46，line49上修改保存的图片的名称
draw.py是根据实验的数据画图

GMM2.py内是比较不同cluster数目下三种模型的聚类效果，如果需要调整数据，只要在line12上修改centers的值，同时在line43，line46，line49上修改保存的图片的名称
draw2.py是根据实验的数据画图

数据.csv文件中保存着实验的数据，注意，因为我的数据是随机生成的，所以每一次的实验数据可能会不同。

figures和figures2文件夹中保存着图片

机器学习hw1.pdf是这次作业的报告
