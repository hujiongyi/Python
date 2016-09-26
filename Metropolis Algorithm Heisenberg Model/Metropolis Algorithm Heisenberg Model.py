import math
import datetime
import random

#物理用常数
N=20
kb=1.38e-23
J=1   #自旋耦合系数
Mu=1  #磁场耦合系数

#初始状态（随机状态)
stheta=[[[0.0 for k in range(N)] for j in range(N)] for i in range(N)]
for i in range(N):
  for j in range(N):
    for k in range(N):
      stheta[i][j][k] =random.randint(0,180)/180.0*math.pi
     
sphi=[[[0.0 for k in range(N)] for j in range(N)] for i in range(N)]
for i in range(N):
  for j in range(N):
    for k in range(N):
      sphi[i][j][k] = random.randint(0,360)/360.0*2*math.pi

#重新初始化
def initialize():
  stheta=[[[0.0 for k in range(N)] for j in range(N)] for i in range(N)]
  for i in range(N):
    for j in range(N):
      for k in range(N):
        stheta[i][j][k] =random.randint(0,180)/180.0*math.pi
  sphi=[[[0.0 for k in range(N)] for j in range(N)] for i in range(N)]
  for i in range(N):
    for j in range(N):
      for k in range(N):
        sphi[i][j][k] = random.randint(0,360)/360.0*2*math.pi
   
#显示初始化状态
def printstart():
  print "初始状态"
  for k in range(N):
    for j in range(N):
      for i in range(N):
        print [format(stheta[i][j][k],'0.2f'),format(sphi[i][j][k],'0.2f')] ,
      print ""
    print
  print ""
  
#显示最终状态
def printfinal():
  print "最终状态"
  for k in range(N):
    for j in range(N):
      for i in range(N):
        print [format(stheta[i][j][k],'0.2f'),format(sphi[i][j][k],'0.2f')] ,
      print ""
    print
  print ""
  
#蒙特卡洛循环
def Metropolis(MC):
  for Z in range(MC):
    ii =random.randint(0,N-1)
    jj =random.randint(0,N-1)
    kk =random.randint(0,N-1)
    oldphi=sphi[ii][jj][kk]
    oldtheta=stheta[ii][jj][kk]
    newtheta=random.randint(0,180)/180.0*math.pi
    newphi=random.randint(0,360)/360.0*2*math.pi
    Sum1 = 0
    Sum2 =0
    iii=ii+1
    if iii>= N:
      iii = iii - N
    Sum1 = Sum1 + math.sin(stheta[iii][jj][kk])*math.cos(sphi[iii][jj][kk])*math.sin(oldtheta)*math.cos(oldphi)+ math.sin(stheta[iii][jj][kk])*math.sin(sphi[iii][jj][kk])*math.sin(oldtheta)*math.sin(oldphi)+math.cos(stheta[iii][jj][kk])*math.cos(oldtheta)
    Sum2 = Sum2 + math.sin(stheta[iii][jj][kk])*math.cos(sphi[iii][jj][kk])*math.sin(newtheta)*math.cos(newphi)+ math.sin(stheta[iii][jj][kk])*math.sin(sphi[iii][jj][kk])*math.sin(newtheta)*math.sin(newphi)+math.cos(stheta[iii][jj][kk])*math.cos(newtheta)
    iii=ii-1
    if iii< 0:
      iii = iii + N
    Sum1 = Sum1 + math.sin(stheta[iii][jj][kk])*math.cos(sphi[iii][jj][kk])*math.sin(oldtheta)*math.cos(oldphi)+ math.sin(stheta[iii][jj][kk])*math.sin(sphi[iii][jj][kk])*math.sin(oldtheta)*math.sin(oldphi)+math.cos(stheta[iii][jj][kk])*math.cos(oldtheta)
    Sum2 = Sum2 + math.sin(stheta[iii][jj][kk])*math.cos(sphi[iii][jj][kk])*math.sin(newtheta)*math.cos(newphi)+ math.sin(stheta[iii][jj][kk])*math.sin(sphi[iii][jj][kk])*math.sin(newtheta)*math.sin(newphi)+math.cos(stheta[iii][jj][kk])*math.cos(newtheta)
    jjj=jj+1
    if jjj>= N:
      jjj = jjj - N
    Sum1 = Sum1 + math.sin(stheta[ii][jjj][kk])*math.cos(sphi[ii][jjj][kk])*math.sin(oldtheta)*math.cos(oldphi)+ math.sin(stheta[ii][jjj][kk])*math.sin(sphi[ii][jjj][kk])*math.sin(oldtheta)*math.sin(oldphi)+math.cos(stheta[ii][jjj][kk])*math.cos(oldtheta)
    Sum2 = Sum2 + math.sin(stheta[ii][jjj][kk])*math.cos(sphi[ii][jjj][kk])*math.sin(newtheta)*math.cos(newphi)+ math.sin(stheta[ii][jjj][kk])*math.sin(sphi[ii][jjj][kk])*math.sin(newtheta)*math.sin(newphi)+math.cos(stheta[ii][jjj][kk])*math.cos(newtheta)  
    jjj=jj-1
    if jjj < 0:
      jjj = jjj + N
    Sum1 = Sum1 + math.sin(stheta[ii][jjj][kk])*math.cos(sphi[ii][jjj][kk])*math.sin(oldtheta)*math.cos(oldphi)+ math.sin(stheta[ii][jjj][kk])*math.sin(sphi[ii][jjj][kk])*math.sin(oldtheta)*math.sin(oldphi)+math.cos(stheta[ii][jjj][kk])*math.cos(oldtheta)
    Sum2 = Sum2 + math.sin(stheta[ii][jjj][kk])*math.cos(sphi[ii][jjj][kk])*math.sin(newtheta)*math.cos(newphi)+ math.sin(stheta[ii][jjj][kk])*math.sin(sphi[ii][jjj][kk])*math.sin(newtheta)*math.sin(newphi)+math.cos(stheta[ii][jjj][kk])*math.cos(newtheta)  
    kkk=kk+1
    if kkk>= N:
      kkk= kkk - N
    Sum1 = Sum1 + math.sin(stheta[ii][jj][kkk])*math.cos(sphi[ii][jj][kkk])*math.sin(oldtheta)*math.cos(oldphi)+ math.sin(stheta[ii][jj][kkk])*math.sin(sphi[ii][jj][kkk])*math.sin(oldtheta)*math.sin(oldphi)+math.cos(stheta[ii][jj][kkk])*math.cos(oldtheta)
    Sum2 = Sum2 + math.sin(stheta[ii][jj][kkk])*math.cos(sphi[ii][jj][kkk])*math.sin(newtheta)*math.cos(newphi)+ math.sin(stheta[ii][jj][kkk])*math.sin(sphi[ii][jj][kkk])*math.sin(newtheta)*math.sin(newphi)+math.cos(stheta[ii][jj][kkk])*math.cos(newtheta)  
    kkk=kk-1
    if kkk < 0:
      kkk = kkk + N
    Sum1 = Sum1 + math.sin(stheta[ii][jj][kkk])*math.cos(sphi[ii][jj][kkk])*math.sin(oldtheta)*math.cos(oldphi)+ math.sin(stheta[ii][jj][kkk])*math.sin(sphi[ii][jj][kkk])*math.sin(oldtheta)*math.sin(oldphi)+math.cos(stheta[ii][jj][kkk])*math.cos(oldtheta)
    Sum2 = Sum2 + math.sin(stheta[ii][jj][kkk])*math.cos(sphi[ii][jj][kkk])*math.sin(newtheta)*math.cos(newphi)+ math.sin(stheta[ii][jj][kkk])*math.sin(sphi[ii][jj][kkk])*math.sin(newtheta)*math.sin(newphi)+math.cos(stheta[ii][jj][kkk])*math.cos(newtheta)  
    delta = Sum2-Sum1
    if delta <= 0:
      sphi[ii][jj][kk] = newphi
      stheta[ii][jj][kk] = newtheta
    elif random.random() < float(math.exp(-J*beta*delta)):
      sphi[ii][jj][kk] = newphi
      stheta[ii][jj][kk] = newtheta

#计算能量
def energy():
   energy=0.0
   for kk in range(N):
     for jj in range(N):
       for ii in range(N):
         Sum=0
         iii=ii+1
         if iii>= N:
           iii = iii - N
         Sum = Sum + math.sin(stheta[iii][jj][kk])*math.cos(sphi[iii][jj][kk])*math.sin(stheta[ii][jj][kk])*math.cos(sphi[ii][jj][kk])+ math.sin(stheta[iii][jj][kk])*math.sin(sphi[iii][jj][kk])*math.sin(stheta[ii][jj][kk])*math.sin(sphi[ii][jj][kk])+math.cos(stheta[iii][jj][kk])*math.cos(stheta[ii][jj][kk])
         iii=ii-1
         if iii< 0:
           iii = iii + N
         Sum = Sum + math.sin(stheta[iii][jj][kk])*math.cos(sphi[iii][jj][kk])*math.sin(stheta[ii][jj][kk])*math.cos(sphi[ii][jj][kk])+ math.sin(stheta[iii][jj][kk])*math.sin(sphi[iii][jj][kk])*math.sin(stheta[ii][jj][kk])*math.sin(sphi[ii][jj][kk])+math.cos(stheta[iii][jj][kk])*math.cos(stheta[ii][jj][kk])
         jjj=jj+1
         if jjj>= N:
           jjj = jjj - N
         Sum = Sum + math.sin(stheta[ii][jjj][kk])*math.cos(sphi[ii][jjj][kk])*math.sin(stheta[ii][jj][kk])*math.cos(sphi[ii][jj][kk])+ math.sin(stheta[ii][jjj][kk])*math.sin(sphi[ii][jjj][kk])*math.sin(stheta[ii][jj][kk])*math.sin(sphi[ii][jj][kk])+math.cos(stheta[ii][jjj][kk])*math.cos(stheta[ii][jj][kk])
         jjj=jj-1
         if jjj < 0:
           jjj = jjj + N
         Sum = Sum + math.sin(stheta[ii][jjj][kk])*math.cos(sphi[ii][jjj][kk])*math.sin(stheta[ii][jj][kk])*math.cos(sphi[ii][jj][kk])+ math.sin(stheta[ii][jjj][kk])*math.sin(sphi[ii][jjj][kk])*math.sin(stheta[ii][jj][kk])*math.sin(sphi[ii][jj][kk])+math.cos(stheta[ii][jjj][kk])*math.cos(stheta[ii][jj][kk])
         kkk=kk+1
         if kkk>= N:
           kkk= kkk - N
         Sum = Sum + math.sin(stheta[ii][jj][kkk])*math.cos(sphi[ii][jj][kkk])*math.sin(stheta[ii][jj][kk])*math.cos(sphi[ii][jj][kk])+ math.sin(stheta[ii][jj][kkk])*math.sin(sphi[ii][jj][kkk])*math.sin(stheta[ii][jj][kk])*math.sin(sphi[ii][jj][kk])+math.cos(stheta[ii][jj][kkk])*math.cos(stheta[ii][jj][kk])
         kkk=kk-1
         if kkk < 0:
           kkk = kkk + N
         Sum = Sum + math.sin(stheta[ii][jj][kkk])*math.cos(sphi[ii][jj][kkk])*math.sin(stheta[ii][jj][kk])*math.cos(sphi[ii][jj][kk])+ math.sin(stheta[ii][jj][kkk])*math.sin(sphi[ii][jj][kkk])*math.sin(stheta[ii][jj][kk])*math.sin(sphi[ii][jj][kk])+math.cos(stheta[ii][jj][kkk])*math.cos(stheta[ii][jj][kk])
         energy=energy+J*Sum
   energy=energy/2.0
   return energy

#计算磁化强度
def magneticx():
  magneticx=0
  for k in range(N):
    for j in range(N):
      for i in range(N):
        magneticx=magneticx+Mu*math.sin(stheta[i][j][k])*math.cos(sphi[i][j][k])
  magneticx=magneticx/N**3
  return magneticx

def magneticy():
  magneticy=0
  for k in range(N):
    for j in range(N):
      for i in range(N):
        magneticy=magneticy+Mu*math.sin(stheta[i][j][k])*math.sin(sphi[i][j][k])
  magneticy=magneticy/N**3
  return magneticy

def magneticz():
  magneticz=0
  for k in range(N):
    for j in range(N):
      for i in range(N):
        magneticz=magneticz+Mu*math.sin(stheta[i][j][k])*math.sin(sphi[i][j][k])
  magneticz=magneticz/N**3
  return magneticz

#主程序
#设置蒙特卡洛步数
MC=20*20*20 #一个蒙特卡洛循环平均每个粒子翻转一次
#抽样次数
sampling=1000
#蒙特卡洛循环
#设置特征温度梯度
beta=0  #特征温度为J/kbT,J*beta
#“预热”工程达到均衡状态
for Z in range(1,101,1):
  initialize()
  Energy=0
  Energy2=0
  Magneticx=0
  Magneticy=0
  Magneticz=0
  Magnetic=0
  Magnetic2=0
  for Z in range(1,401,1):
    Metropolis(MC)
  for Z in range(1,sampling+1,1):
    Metropolis(MC)
    Energy=energy()+Energy
    Energy2=energy()**2+Energy2
    Magneticx=magneticx()+Magneticx
    Magneticy=magneticy()+Magneticy
    Magneticz=magneticz()+Magneticz
    Magnetic2=magneticx()**2+magneticy()**2+magneticz()**2+Magnetic2
  AverageEnergy=Energy/sampling
  AverageEnergy2=Energy2/sampling
  VarianceEnergy=AverageEnergy2-AverageEnergy**2
  c=beta**2*VarianceEnergy/N**3
  AverageMagneticx=Magneticx/sampling
  AverageMagneticy=Magneticy/sampling
  AverageMagneticz=Magneticz/sampling
  AverageMagnetic2=Magnetic2/sampling
  VarianceMagnetic=AverageMagnetic2-(AverageMagneticx**2+AverageMagneticy**2+AverageMagneticz**2)
  X=beta*VarianceMagnetic
  print "J/kbT=",J*beta,
  print "Energy=",AverageEnergy,
  print "c=",c,
  print "M=(",AverageMagneticx,AverageMagneticy,AverageMagneticz,")",
  print "X=",X
  beta=beta+0.02

