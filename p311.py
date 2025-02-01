#　クランク軸のねじり振動 
# 機械回路p311 Torque 
# 20241124 shimojo
# いろいろと不備があります。信用しないように
#
import numpy as np #数値計算（Numerical Python）
import matplotlib.pyplot as plt #PLOT
import numpy.linalg as LA #線形代数

# クランク軸ねじり振動p311
#　例題：６シリンダ・エンジンにプロペラ軸
#　共振数波数におけるねじりトルクの分布状態

#クランク軸のねじり振動(例題)の解　f(α)= mπ
#P=6 までの解αp[degree]のarray
apa=np.array([29.6,57.5,67.6,90.8,120.3,150.2])

#　パラメータ：重力単位系です
n=6 # フライホイール数
I=300# 慣性モーメント　cm.kg.s^2
c=6.0e-9#捩じれコンプライアンス　rad.cm^(-1).kg^(-1)#
#
print("\nクランク軸ねじり振動の共振振動数")
for i in range(0,6):
    fp=1/(2*np.pi)*np.sqrt((2/(I*c))*(1-np.cos(apa[i]*np.pi/180.0)))
    print("alpha=",apa[i],"fp=",fp)
#
print("\nクランク軸ねじり振動のトルク分布")
# 振動モード、１，２・・６での、クランク軸トルクの計算
#パラメータ[16,26.667]は,例題クランク軸の慣性モーメント、ねじり剛性から計算したもの


for l in range(0,6):
    num=l;print()
    for k in range(0,n):
        p=k+1;ap=apa[num]*np.pi/180
        yy=np.sin(ap*n)-(np.sin((n-1)*ap)/(16-26.667*(1-np.cos(ap))))
        xx=np.cos(ap*n)-(np.cos((n-1)*ap)/(16-26.667*(1-np.cos(ap))))
        tx=np.sin(ap*p)-yy/xx
        #print("共振NO.=",num,", p=", p," , tx=",tx)
        print("mode=",num,"=",p,tx)