###range1をdefの外に定義したら、
#JSでonload配列の計算 配列range1を作成
#スライダの値に対応する配列の要素を抽出


#-*- coding:utf-8-*-
import webiopi
import time
import pigpio
import subprocess as proc
import datetime

webiopi.setDebug()
pi=pigpio.pi()

#ピン指定
SV_1 = 12  #STEERING
SV_2 = 19  #THROTTLE
SV_3 = 21  #STOP IMMEDIATELY
value11=[]

#これ無くていい
# def setup():
#  pi.set_mode(SV_1, pigpio.OUTPUT) #STEERING
#  pi.set_mode(SV_2, pigpio.OUTPUT) #THROTTLE
#  pi.set_mode(SV_3, pigpio.OUTPUT) #STOP


#*******neutral.html***STEERING********************
path = "/home/pi/Desktop/TeamB/"  #適当なパスを指定
filename11 = "mini.txt" #最小値
filename12 = "neut.txt" #中立値
filename13 = "maxi.txt" #最大値
#*****************************
range11 = []
range12 = []

@webiopi.macro
def TIMEOUT():
    get15 = range12[0]   #もともとget12だったけどget15に変更
    pi.set_servo_pulsewidth(SV_2,get15)
    webiopi.debug(get15)




@webiopi.macro
def main11():
    f = open(path+filename11, "r")
    mini = int(f.read())
    f.close()
    f = open(path+filename12, "r")
    neutral = int(f.read())
    f.close()
    f = open(path+filename13, "r")
    maxi = int(f.read())
    f.close()

    a = neutral - mini
    b = maxi - neutral
    c = float(a/100)
    d = float(b/100)

    for i in range(0,201):
        if i <=100:
            range11.append(int(i*c+mini))
        else:
            range11.append(int((i-100)*d+neutral))

#*******neutral.html***THROTTLE********************
filename21 = "mini_thro.txt" #最小値
filename22 = "maxi_thro.txt" #最大値
filename23 = "x_thro.txt" #傾き変わる点(x)
filename24 = "y_thro.txt" #傾き変わる点(y)
#*****************************
@webiopi.macro
def main12():
    f = open(path+filename21, "r")
    mini21 = int(f.read())
    f.close()
    f = open(path+filename22, "r")
    maxi21 = int(f.read())
    f.close()
    f = open(path+filename23, "r")
    x21 = int(f.read())
    f.close()
    f = open(path+filename24, "r")
    y21 = int(f.read())
    f.close()

    a21 = y21-mini21
    b21 = maxi21-y21
    c21 = float(a21/x21)
    d21 = float(b21/(200-x21))
    e21 = int(maxi21-d21*200)
    for i in range(0,201):
        if i <=x21:
            range12.append(int(c21*i+mini21))
        else:
            range12.append(int(d21*i+e21))

#***********************************

#サーボ動作
#****************controller.html***************************
#STEERING
@webiopi.macro
def GET1(val):
    val11 = int(val) + 100
    get11 = range11[val11]
    pi.set_servo_pulsewidth(SV_1,get11)
    webiopi.debug(get11)


#THROTTLE
@webiopi.macro
def GET2(val):
    val12 = int(val)
    get12 = range12[val12]
    pi.set_servo_pulsewidth(SV_2,get12)
    webiopi.debug(get12)

#STOP
@webiopi.macro
def BRAKE(val):
 webiopi.debug(val)
 pi.set_servo_pulsewidth(SV_3, int(val))
#***************************************************




#******ページに表示するadjustment_steering.html******************
@webiopi.macro
def Load11(val):
    f = open(path+filename11, "r")
    value = int(f.read())
    f.close()
    return "%d"%(value)

@webiopi.macro
def Load12(val):
    f = open(path+filename12, "r")
    value = int(f.read())
    f.close()
    return "%d"%(value)

@webiopi.macro
def Load13(val):
    f = open(path+filename13, "r")
    value = int(f.read())
    f.close()
    return "%d"%(value)

@webiopi.macro
def Send21(val):
    f = open(path+filename11, "w")
    f.write(val)
    f.close()

@webiopi.macro
def Send22(val):
    f = open(path+filename12, "w")
    f.write(val)
    f.close()

@webiopi.macro
def Send23(val):
    f = open(path+filename13, "w")
    f.write(val)
    f.close()

#**************************************
#******ページに表示するadjustment_throttle.html******************
# filename21 = "mini_thro.txt" #最小値
# filename22 = "maxi_thro.txt" #最大値
# filename23 = "x_thro.txt" #傾き変わる点(x)
# filename24 = "y_thro.txt" #傾き変わる点(y)

@webiopi.macro
def Load31(val):
    f = open(path+filename21, "r")
    value = int(f.read())
    f.close()
    return "%d"%(value)

@webiopi.macro
def Load32(val):
    f = open(path+filename22, "r")
    value = int(f.read())
    f.close()
    return "%d"%(value)

@webiopi.macro
def Load33(val):
    f = open(path+filename23, "r")
    value = int(f.read())
    f.close()
    return "%d"%(value)

@webiopi.macro
def Load34(val):
    f = open(path+filename24, "r")
    value = int(f.read())
    f.close()
    return "%d"%(value)

@webiopi.macro
def Send31(val):
    f = open(path+filename21, "w")
    f.write(val)
    f.close()

@webiopi.macro
def Send32(val):
    f = open(path+filename22, "w")
    f.write(val)
    f.close()

@webiopi.macro
def Send33(val):
    f = open(path+filename23, "w")
    f.write(val)
    f.close()

@webiopi.macro
def Send34(val):
    f = open(path+filename24, "w")
    f.write(val)
    f.close()

#**************************************

#***************************************************



#********************power.html********************
#シャットダウン実行関数
@webiopi.macro
def ShutCmd():
    proc.call("sudo killall sudo", shell=True)
    proc.call("sudo /sbin/shutdown -h now", shell=True)

#再起動実行関数
@webiopi.macro
def RebootCmd():
    #webiopi.debug("再起動するよ")
    proc.call("sudo killall sudo", shell=True)
    proc.call("sudo /sbin/shutdown -r now", shell=True)
#*****************************************************



