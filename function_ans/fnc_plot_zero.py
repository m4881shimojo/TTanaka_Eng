import numpy as np #数値計算（Numerical Python）
import matplotlib.pyplot as plt #PLOT
import numpy.linalg as LA #線形代数
import matplotlib.ticker as ticker #補助目盛線

def f(x):
    r_val=np.cosh(x)*np.cos(x)+1 #解を求める関数
    return r_val

#main 
knum=1000 #区間をknum個に分割
# x=np.linspace(a,b,knum) [a,b]間をknum等分にした数列をｘとする
x=np.linspace(0,21,knum)
# yは数値列。 [a,b]間をknum等分にした数列をｘに対する関数値
y=f(x)

# plot
fig,ax = plt.subplots(facecolor="w")
ax.plot(x,y)
ax.minorticks_on()
ax.grid(which="major", color="gray", linestyle="solid")
ax.grid(which="minor", color="red", linestyle="dotted")

ax.set_ylim(-40, 40)
#
plt.show()

