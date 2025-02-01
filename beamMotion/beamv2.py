# 弾性梁のモビリテイ 
# 機械回路p338 
# 20250118 shimojo
import numpy as np #数値計算（Numerical Python）
import matplotlib.pyplot as plt #PLOT
import numpy.linalg as LA #線形代数
import matplotlib.ticker as ticker #補助目盛線
#-----------------------------------------------------
#h=0.05cmでは薄いので、h=1cmとする 2025.0119 shimojo
# set parameters
l=400.0;h=0.05;E=2.0e6;ro=7.8e-3;g=980.0;q=0.1;Q=0.1

#h=0.5;h=0.8;
h=1 #変更してみた！
Q=0.2#変更してみた！
b_w=1 #beamの幅 cm
freq=2#;freq=10#hz

#calculate parameters
a=h*b_w;I=b_w*h**3/12.0 #断面積、断面二次モーメント
omega=2*np.pi*freq
EI=E*I
#
myu=np.power((ro*a*omega**2/(g*EI)),1/4)
ml=myu*l
#test
#ml=6;myu=ml/l
#　各種パラメータを印刷
print("弾性梁の変位")
print("\n各種パラメータを印刷")
print("  freq, omega, l, h, E, ro, g, q, Q, EI, a, I")
print("  ",freq,omega,l,h,E,ro,g,q,Q,EI,a,I)
print("  myu=",myu,"myu*l=",ml)
#print("ys0=",ro*a/EI*3/24*l**4)　#梁変位の静的成分最大値
#-----------------------------------------------------
#main 
knum=100 #区間をknum個に分割
tnum=6 #時間ショットを10個
# x=np.linspace(a,b,knum) [a,b]間をknum等分にした数列をｘとする
x=np.linspace(0,l,knum)
#
#弾性梁の変位(静的成分と動的成分)
ys=np.zeros(knum) #静的変位
yd=np.zeros((tnum,knum))#動的変位をtnum個記憶
y=np.zeros((tnum,knum)) #beamの振幅変化をtnum個記憶

#A,B,C,Dを求めて、(10.131)を用いる
W=2*(1+np.cosh(ml)*(np.cos(ml)))
A=(np.cosh(ml)*np.sin(ml)-np.sinh(ml)*np.cos(ml))*Q/(myu*W)
B=(np.cosh(ml)*np.cos(ml)-np.sinh(ml)*np.sin(ml)+1-2*(np.sin(ml))**2)*Q/(myu*W)
C=-A;D=Q/myu-B

#print("A=",A,"B=",B,"C=",C,"D=",D)

#beam 
for k in range(0,tnum):
    wt=2*np.pi*k/(tnum) #　2πをtnumに分割して、梁の時間変位を表示する
    
    for i in range(0,knum):
        ys[i]=-ro*a/(24*EI)*x[i]**4+ro*a*l/(6*EI)*x[i]**3-ro*a*l*l/(4*EI)*x[i]**2+q*x[i]
        #ys[i]=0 #検査用に入れた

        # Dynamic displacement of beams

        #動的変位成分
        yd[k,i]=(A*np.cosh(myu*x[i])+B*np.sinh(myu*x[i])+C*np.cos(myu*x[i])+D*np.sin(myu*x[i]))*np.cos(wt)
        #弾性梁の変位＝静的成分+動的成分   
        y[k,i]=ys[i]+yd[k,i]
        # 
print("\nEnd\n")
#########################################################
#　　　　　　　　　　　　　　　PLOT 　　　　　　　　　　　 #
#########################################################
############################################################
#                figure 1                                  #
############################################################
from matplotlib.gridspec import GridSpec
fig = plt.figure(figsize=(7,6.2)) # Figureの初期化(横、縦寸法)
#1つの図に様々な大きさのグラフを追加
# https://pystyle.info/matplotlib-grid-sepc/
#縦方向に3つ場所を用意して、2つをss１に、1つをss2用に使う
#
gs = GridSpec(2, 1)  # 縦方向に2つ、横方向に１つの場所を用意
#ss1--> 場所は(0,0)、縦1つ、横１つ、を使用
ss1 = gs.new_subplotspec((0, 0), rowspan=1,colspan=1)  # ax1 を配置する領域
#ss2--> 場所は(2,0)、縦１つ横１つ、を使用
ss2 = gs.new_subplotspec((1, 0), rowspan=1, colspan=1)  # ax2 を配置する領域
#

#####11111111111111111111########
# ax1　PLOT
#####11111111111111111111########
ax1 = plt.subplot(ss1)
#
for j in range(0,tnum):
    ax1.plot(x,y[j,:])

strg0="freqency={:.3g}[Hz]".format(freq)
plt.title("図10-56 弾性梁の振動変位 :"+strg0, fontname="MS Gothic")
#plt.ylim(Ymin,Ymax)
plt.ylabel("displacement [cm] ")

ax1.minorticks_on()
ax1.grid(which="major", color="gray", linestyle="solid")
ax1.grid(which="minor", color="lightgray", linestyle="dotted")

####222222222222222222222########
# ax2　PLOT
####222222222222222222222########
ax2 = plt.subplot(ss2)
plt.title(" 弾性梁の振動成分 :"+strg0, fontname="MS Gothic")

#ax2.plot(x,yd,drawstyle='steps-post',color='g', linestyle='dashed', marker='.',label="u(k)")
for j in range(0,tnum):
    ax2.plot(x,yd[j,:])

#ax2.plot(t,d,drawstyle='steps-post',color='b', linestyle='dashed', marker='*',label="d(k)")
plt.ylabel("vibration amplitude[cm]")
plt.xlabel("length [cm]")

ax2.minorticks_on()
#plt.legend(loc='lower right')
ax2.grid(which="major", color="gray", linestyle="solid")
ax2.grid(which="minor", color="lightgray", linestyle="dotted")
#
plt.tight_layout()#上のグラフのx軸のラベルと下のグラフのタイトルの重なりを解消する
plt.show()

