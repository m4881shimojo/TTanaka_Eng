#　クランク軸のねじり振動 
# 機械回路p310
# 20241124 shimojo
# いろいろと不備があります。
import numpy as np #数値計算（Numerical Python）
import matplotlib.pyplot as plt #PLOT
import numpy.linalg as LA #線形代数（今回不要）
import matplotlib.ticker as ticker #補助目盛線

#横軸分割数
knum=200  
#表示範囲（目盛の間隔はPLOTでのstepで調整してください）
x_min=0;x_max=180
y_min=0;y_max=1400 

a=0 #alpha [degree]
d=np.pi/knum #刻み幅
X=np.zeros(knum)
Y=np.zeros(knum)

#  f(α) (10.59)式を使った計算
for i in range(0,knum):
    a=a+d
    yy=np.sin(a)
    xx=np.cos(a)-(1/(16-26.667*(1-np.cos(a))))
    atan=np.arctan2(yy,xx)
    fa=5*a+atan  #(10.59)
    X[i]=a*180/(np.pi)
    Y[i]=fa*180/(np.pi)
        
##############################################################
#                    PLOT                                    #
# pltメソッドとオブジェクト指向が混載で記述している　　　        #
# ←下条がよく理解していないため　　　　　　　　　　　　　　  　　 #
# https://www.yutaka-note.com/entry/matplotlib_axis          #
# https://qiita.com/bridgenail24/items/f2320d7bf5aaec2dc0ea  #
##############################################################
fig = plt.figure(figsize=(7,7)) # Figureの初期化
ax1 = plt.subplot()
ax1.plot(X,Y,'*--r')     #最終出力 

# タイトル
plt.title("図10-26クランク軸のねじり振動固有値決定", fontname="MS Gothic")
# 軸ラベルの設定
plt.xlabel("alfa", size = "large", color ="green")
plt.ylabel("f(a)", size = "large", color="blue")
# 軸の最大値・最小値の設定
plt.xlim(x_min,x_max)
plt.ylim(y_min,y_max)

# 目盛りの表示値を変更（stepの値を適切に変更可）
plt.xticks(np.arange(x_min, x_max+1, step=20))
plt.yticks(np.arange(y_min, y_max+1,step=200))
# 補助目盛を表示
plt.minorticks_on()

# 補助目盛線間隔の変更
ax1.xaxis.set_minor_locator(ticker.AutoMinorLocator(5))
ax1.yaxis.set_minor_locator(ticker.AutoMinorLocator(5))

plt.grid(which="major", color="black", alpha=0.5)
plt.grid(which="minor", color="gray", linestyle=":")
   
# 表示
plt.show() 