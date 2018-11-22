import numpy as np
import math
from numpy import *


#读取文件
file_2015_1_path="D://sf1.csv"
#下载文件
t1 = np.loadtxt(file_2015_1_path, delimiter=",", dtype="float")

file_2015_2_path="D://sf2.csv"
t2 = np.loadtxt(file_2015_2_path, delimiter=",", dtype="float")
#取出t1和t2的权重生成一个新的权重

#行数多的为u1
if(t1.shape[0]>t2.shape[0]):
    u1=t1
    u2=t2
    flag = 1
else:
    u1=t2
    u2=t1
    flag = 0

for i in u1:
    for j in u2:
        if(i[1]==j[1] and i[0]==j[0]):
            {
               #计算权重
                if (flag==1) :
                    i[2]=(i[2]*0.6+j[2]*0.4)

                #把这一行写到一个新的文件里

            }
        else:pass
            #如果找不到这个j匹配，把这一行本身写下来





#难题：列和列数值个数不一样
#w = 0.6*w0+0.4*w1


