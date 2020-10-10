import matplotlib.pyplot as plt
import subprocess as proc

path0 = "/home/pi/Desktop/TeamB/"
path = path0 + "parameter/" 
graphfile1 = "graph1.png"
graphfile2 = "graph2.png"
filename21 = "mini_thro.txt" #最小値
filename22 = "maxi_thro.txt" #最大値
filename23 = "x_thro.txt" #傾き変わる点(x)
filename24 = "y_thro.txt" #傾き変わる点(y)



def makeGraph():
    range12=[]
    x = []
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

    for i in range(0,201):
        x.append(i)

    #fig = plt.figure()  #新規のグラフを描画
    plt.xlim([0,200])
    plt.ylim([1000,2000])
    plt.plot(x, range12)
    
    plt.savefig(path0+graphfile1)
    plt.close("all")

def main():
    makeGraph()
    aaa=path0+graphfile1
    bbb=path0+graphfile2
    ccc = "sudo cp "+aaa+" "+bbb
    #proc.call("sudo cp "+path+graphfile1 path+graphfile2, shell=True)
    proc.call(ccc, shell=True)


if __name__ =='__main__':
    main()