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
for i in t1:
    i[2]=i[2]+2
    print(i[2])