# クランク軸ねじり振動p311 
#　例題：6シリンダ・エンジンにプロペラ軸
# 20241124 shimojo
# 20250130 shimojo 改変

import numpy as np #数値計算（Numerical Python）
import matplotlib.pyplot as plt #PLOT
#import numpy.linalg as LA #線形代数


#　共振数波数におけるねじりトルクの分布状態
#クランク軸のねじり振動(例題)の解　f(α)= mπ
#振動モード6次までの解αp[degree]のデータ p310.py
apa=np.array([29.6,57.5,67.6,90.8,120.3,150.2])

#　パラメータ：重力単位系です
I=300 # 慣性モーメント　cm.kg.s^2
c=6.0e-9 #捩じれコンプライアンス　rad.cm^(-1).kg^(-1)#
#
print("\nクランク軸ねじり振動の共振振動数(6次まで)")
for i in range(0,6):
    fp=1/(2*np.pi)*np.sqrt((2/(I*c))*(1-np.cos(apa[i]*np.pi/180.0)))
    print("  mode=", i+1,"alpha=",apa[i],"fp=",fp)
#
print("\nクランク軸ねじり振動のトルク分布")
n=6 # フライホイール数
# 振動モード、１，２・・６での、クランク軸トルクの計算
# パラメータ[16,26.667]は,例題クランク軸の慣性モーメント、ねじり剛性から計算したもの
# ap:alpha, xn:軸トルクのｘ番目、tx:軸トルク

# (10.61)式を実行　apは解の振動数、xnはx番目の軸
for l in range(0,6): #6次までの振動モード
    nMode=l;print("mode=",nMode+1) # 
    for k in range(0,n): #
        xn=k+1 #共振モードを1次から
        ap=apa[nMode]*np.pi/180
        yy=np.sin(ap*n)-(np.sin((n-1)*ap)/(16-26.667*(1-np.cos(ap))))
        xx=np.cos(ap*n)-(np.cos((n-1)*ap)/(16-26.667*(1-np.cos(ap))))
        tx=np.sin(ap*xn)-yy/xx        
        print("  x=",xn,"torque=",tx)#

print("\nおわり\n")#
# 各振動モードでの軸トルクの表示はエクセルなどで行ってください