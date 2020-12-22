# Auteurs : Matthieu Briet; Antoine Pagneux; Tanguy Colleville

import matplotlib.pyplot as plt 
import numpy as np
import scipy.integrate as spi
from mpl_toolkits import mplot3d
 
# u0=1# valeur initiale 
# v0=1
u0=100# valeur initiale 
v0=0.01
w0=0.16

#valeurs des paramètres du modèle
b1 = 0.01
k1 = 0.9
k2 = 0.05
a2 = 0.7
c1 = 0.06
c2 = 0.8
a1 = 0.5
q = 0.09
lmda = 0.5 # lambda
p = 0.5
c = 0.7
delta  = 0.03
m=0.9262
u_eq=c/(m*q*p)
v_eq=(a2/c2)*(k2+c/(m*q*p))
w_eq=(1/(m*q)*((a1*p*m*q-b1*c)/(p*m*q)-(c1*a2*(c+k2*p*m*q))/(c2*(c+k1*p*m*q))))

def F(Vector,t):# problème de Cauchy 
    result=[]
    result.append((a1-b1*Vector[0]-(c1*Vector[1])/(Vector[0]+k1))*Vector[0]-m*q*Vector[0]*Vector[2])
    result.append((a2-c2*Vector[1]/(Vector[0]+k2))*Vector[1])
    result.append(lmda*(p*m*q*Vector[0]-c)*Vector[2])
    return result
    
Y0=[u0,v0,w0]# Vecteur initiale
N=1000# Nombre de valeurs 
t_final = 100 # temps final
LT=np.linspace(0,t_final,N)
S=spi.odeint(F,Y0,LT)# résolution du problème de Cauchy 
solU=[S[i][0] for i in range(N)]
solV=[S[i][1] for i in range(N)]
solW=[S[i][2] for i in range(N)]
Sol=[solU,solV,solW]

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(solU, solV, solW, 'red')
plt.xlabel("Sardines")
plt.ylabel("Requins")
plt.title("Ligne de convergence Scipy")
plt.show()

plt.figure()
plt.plot(LT,solU,label="Population Sardine",color="blue")
plt.plot(LT,solV,label="Population Requin",color="r")
plt.plot(LT,solW,label="Effort de pêche",color="green")
plt.plot(LT,[u_eq]*N,label="U equi")
plt.plot(LT,[v_eq]*N,label="V equi")
plt.plot(LT,[w_eq]*N,label="W equi")
plt.title("Résolution avec Scipy")
plt.legend()
plt.show()


u_euler = [u0]
v_euler = [v0]
w_euler = [w0]
u_prim_euler = [0]
v_prim_euler = [0]
w_prim_euler = [0]
h = t_final/N
for i in range(len(LT)-1):
    u_euler.append(u_euler[i]  + h * ( (a1 - b1 * u_euler[i] - ((c1*v_euler[i]) / (u_euler[i]+k1))) * u_euler[i] - m*q * u_euler[i] * w_euler[i]) )
    v_euler.append(v_euler[i]+h*((a2-(c2*v_euler[i])/(u_euler[i]+k2))*v_euler[i]))
    w_euler.append(w_euler[i] + h * lmda*(p*m*q*u_euler[i]-c)*w_euler[i])
    u_prim_euler.append(( (a1 - b1 * u_euler[i] - ((c1*v_euler[i]) / (u_euler[i]+k1))) * u_euler[i] - m*q * u_euler[i] * w_euler[i]))
    v_prim_euler.append((a2-(c2*v_euler[i])/(u_euler[i]+k2))*v_euler[i])
    w_prim_euler.append( lmda*(p*m*q*u_euler[i]-c)*w_euler[i] )


plt.figure()
plt.plot(LT,u_euler,label="Sardines euler")
plt.plot(LT,v_euler,label="Requins euler")
plt.plot(LT,w_euler,label="Efforts de pêche euler")
plt.plot(LT,[u_eq]*N,label="U equi")
plt.plot(LT,[v_eq]*N,label="V equi")
plt.plot(LT,[w_eq]*N,label="W equi")
plt.legend()
plt.title("Résolution avec Euler")
plt.show()

plt.figure()
plt.plot(LT,u_euler,label="Sardines euler")
plt.plot(LT,v_euler,label="Requins euler")
plt.plot(LT,w_euler,label="Efforts de pêche euler")
plt.plot(LT,solU,label="Sardines scipy")
plt.plot(LT,solV,label="Requins scipy")
plt.plot(LT,solW,label="Efforts de pêche scipy")
plt.legend()
plt.title("Euler VS Scipy ")
plt.show()

plt.figure()
plt.plot(u_euler,v_euler,label="Sardines et Requins")
plt.legend()
plt.title("Sardines et requins ")
plt.show()


plt.figure()
plt.plot(u_euler,u_prim_euler,label="Portrait phase sardines")
plt.legend()
plt.title("Portrait de phase pour u, population de sardines")
plt.show()

plt.figure()
plt.plot(v_euler,v_prim_euler,label="Portrait phase requins")
plt.legend()
plt.title("Portrait de phase pour v, population de requin")
plt.show()

plt.figure()
plt.plot(w_euler,w_prim_euler,label="Portrait phase intensité de pêche")
plt.legend()
plt.title("Portrait de phase pour w, intensité de la pêche")
plt.show()

# plt.figure()
# u_euler=np.array(u_euler)
# v_euler=np.array(v_euler)
# w_euler=np.array(w_euler)

# u_prim_euler=np.array(u_prim_euler)
# v_prim_euler=np.array(v_prim_euler)
# LTarray=np.array(LT)

# print(len(LTarray))
# print(len(u_prim_euler))
# print(len(v_prim_euler))
# plt.streamplot(LTarray,LTarray,u_prim_euler,v_prim_euler)
# plt.legend()
# plt.title("PLt contour ")
# plt.show()

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot3D(u_euler, v_euler, w_euler, 'red')
plt.xlabel("Sardines")
plt.ylabel("Requins")
plt.title("Euler convergence vers le point d'équilibre")
plt.show()