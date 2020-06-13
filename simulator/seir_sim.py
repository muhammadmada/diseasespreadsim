from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

#Model params
c = float(3.6)
beta = float(6.93*10^-11)
deltaI = float(0.13)
deltaQ = float(0.13)
gammaI = float(0.003)
gammaH = float(0.009)
Q = float(9*10^-7)
alpha = float(0.0001)
theta = float(0.6)
lamda = float(1/14)
T = float(40)
t = float(0.1)
NN = float(T/t)
#Initial value below
S = int(13.95*10^8)
E = int(4007)
I = int(776)
Sq = int(8420)
Eq = int(3000)
H = Eq + I
R = int(34)
De = int(25)
AA = [S, E , I , Sq, Eq, H, R]

if ii == 1/NN:
    sigma = float((1/7 - 1/3)/(1 + exp((ii*t-4)/ii*(t/0.2))+1/3)
    dS = int(-(beta*c + c*q*(1-beta)*S*(I+theta+E)+ lamda*Sq)
    dE =  int(beta*c*(1-q)*S*(I+theta*E)-sigma*E)
    dI =  int(sigma*E-(deltaI+alpha+gammaI)*I)
    dSq = int(1-beta)*c*q*S*(I+theta*E)-lamda*Sq)
    dEq = int(beta*c*q*S*(I+theta*E)-deltaQ*Eq)
    dH =  int(deltaI*I+deltaQ*Eq-(alpha+gama_H)*H)
    dR =  int(gammaI*I+gama_H*H)
    dDe = alpha*(I+H);
    #Euler integration algorithm
    S =S+dS*t
    E = E+dE*t
    I = I+dI*t
    Sq = Sq+dSq*t
    Eq = Eq+dEq*t
    H = H+dH*t
    R = R+dR*t
    AA=[AA; S E I Sq Eq H R]
    #Plotting algos below
