import numpy as np #数値計算（Numerical Python）
import matplotlib.pyplot as plt #PLOT
import numpy.linalg as LA #線形代数
import matplotlib.ticker as ticker #補助目盛線
# 非線形方程式の解法（はさみうち法）を利用して解を求める
# http://fornext1119.web.fc2.com/NumericOperation/vol_05/Text/09_02_06.xhtml

def f(x):
    r_val=np.tanh(x)-np.tan(x) #解を求める関数
    return r_val
# はさみうち法
def solution(a, b):
    while True:
        # 点$ (a,f(a)) $ と 点 $ (b,f(b)) $ を結ぶ直線と $ x $ 軸の交点
        c  = (a * f(b) - b * f(a)) / (f(b) - f(a))           
        fc = f(c)
        if (abs(fc) < 0.00001): #解の精度
            break
        if (fc < 0):
            # f(c) < 0 であれば, 解は区間 (c, b) の中に存在
            a = c
        else:
            # f(c) > 0 であれば, 解は区間 (a, c) の中に存在
            b = c
    return c
# 解はa,bの間にある。関数のplotを行い、大まかな解の範囲[a,b]を求めておく
a = 19;b = 20
#
print("\n非線形方程式の解（はさみうち法）")
print ("  解=",solution(a, b),"区間[",a,b,"]\n")