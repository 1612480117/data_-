import numpy as np
import math
from numpy import *
#想办法把下面的封装为一个函数

#定义simoid函数，将权重计算
def sigmoid(filename,sfname):
    filename1=filename
    sfname1=sfname
    #读取文件
    file_2015_1_path="./"+filename1

    t1 = np.loadtxt(file_2015_1_path,delimiter=",",dtype="float")
    #抽取特殊的列或者行形成的文件
    t2=t1[:,2:]

    #对权重进行sigmoid
    #不知道为什么math.exp()在这里会报错
    #a=1/(math.exp(-t2)+1)
    f1 = -t2
    a=1/((e**f1)+1)


    t3=t1[:,:2]
    #将t3,t2拼接到一起  这里用的是水平拼接
    t4=np.hstack((t3,a))  #里面一定用元组的形式

    #print(t4)
    #%.2f0.8之类的会自动进位为1
    np.savetxt("D://"+sfname1,t4,fmt='%.6f',delimiter=",");     #fmt='%2.f 可以保存为浮点型，保存一个文件到D盘

sigmoid("edge2015_1.csv","sf1.csv");
sigmoid("edge2015_2.csv","sf2.csv");
sigmoid("edge2016_1.csv","sf3.csv");
sigmoid("edge2016_2.csv","sf4.csv");
sigmoid("edge2017_1.csv","sf5.csv");
sigmoid("edge2017_2.csv","sf6.csv");
sigmoid("edge2018_1.csv","sf7.csv");
#假设平滑公式为 w=0.6*w0+0.4*w1




