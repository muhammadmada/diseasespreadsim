from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

#Plotting
def modseirplot(t, S, Sq, E, Eq, I, H, R, L=None, D=None, R0=None, Alpha=None, CFR=None):
  f, ax = plt.subplots(1,1, figsize=(10,4))
  ax.plot(t, S, 'b', alpha=0.7, linewidth=2, label= 'Susceptible')
  ax.plot(t, Sq, '', alpha=0.7, linewidth=2, label= 'Quarantined Susceptible')
  ax.plot(t, E, 'y', alpha=0.7, linewidth=2, label= 'Exposed')
  ax.plot(t, Eq, '', alpha=0.7, linewidth=2, label= 'Quarantined Exposed')
  ax.plot(t, I, 'r', alpha=0.7, linewidth=2, label= 'Infected')
  ax.plot(t, H, '', alpha=0.7, linewidth=2, label= 'Hospitalized')
  ax.plot(t, R, 'g', alpha=0.7, linewidth=2, label= 'Recovered')
  if D is not None:
      ax.plot(t, D, 'k', alpha=0.7, linewidth=2, label='Dead')
      ax.plot(t, S+Sq+E+Eq+I+H+R+D, 'c--', alpha=0.7, linewidth=2, label='Total')
  else:
       ax.plot(t, S+Sq+E+Eq+I+H+R+D, 'c--', alpha=0.7, linewidth=2, label='Total')
    
  ax.set_xlabel('Time (days)')
  ax.yaxis.set_tick_params(length=0)
  ax.xaxis.set_tick_params(length=0)
  ax.grid(b=True, which='major', c='w', lw=2, ls='-')
  legend = ax.legend(borderpad=2.0)
  legend.get_frame().set_alpha(0.5)
  for spine in ('top','right', 'bottom', 'left'):
      ax.spines[spine].set_visible(False)
  if L is not None:
     plt.title("Lockdown after {} days".format(L))
  plt.show()
#Model params
c = float(3.6)
Beta = float(6.93*10^-11)
DeltaI = float(0.13)
DeltaQ = float(0.13)
GammaI = float(0.003)
GammaH = float(0.009)
Q = float(9*10^-7)
Alpha = float(0.0001)
Theta = float(0.6)
Lambda = float(1/14)
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
D = int(25)
AA = [S, E , I , Sq, Eq, H, R]

if ii == 1/NN:
    Sigma = float((1/7 - 1/3)/(1 + exp((ii*t-4)/ii*(t/0.2))+1/3)
    dS = int(-(Beta*c + c*q*(1-Beta)*S*(I+Theta+E)+ Lambda*Sq)
    dE =  int(Beta*c*(1-q)*S*(I+Theta*E)-Sigma*E)
    dI =  int(Sigma*E-(deltaI+Alpha+GammaI)*I)
    dSq = int(1-Beta)*c*q*S*(I+Theta*E)-Lambda*Sq)
    dEq = int(Beta*c*q*S*(I+Theta*E)-DeltaQ*Eq)
    dH =  int(deltaI*I+DeltaQ*Eq-(Alpha+GammaH)*H)
    dR =  int(GammaI*I+GammaH*H)
    dD = alpha*(I+H);
    #Euler integration algorithm
    S =S+dS*t
    E = E+dE*t
    I = I+dI*t
    Sq = Sq+dSq*t
    Eq = Eq+dEq*t
    H = H+dH*t
    R = R+dR*t
    AA=[AA; S E I Sq Eq H R]

