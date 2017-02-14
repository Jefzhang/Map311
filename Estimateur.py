import numpy as np
import matplotlib.pyplot as plt
import scipy.special as ss
import scipy.stats as sps


class Estimateur:
    @staticmethod
    def p_k(k,rho):     #calculer p(k)
        beta = ss.beta(k, rho+1)
        return rho*beta

    @staticmethod
    def p(rho,N):       #calculer la distribution de la densité de loi Yule
        pk = []
        for i in range(1,N,1):
            if i==1:
                pk.append(Estimateur.p_k(1,rho))
            else:
                pk.append((Estimateur.p_k(i,rho)+pk[i-2]))
        return pk

    @staticmethod      #selon la distribution de loi Yule, simulation de loi de Yule
    def Yuledis(rho,p_k,N):
        YuleD = []
        for i in range(1,N,1):
            k=0
            rand = np.random.rand()
            for j in range(len(p_k)):
                if rand <= p_k[j]:
                   k =j+1
                   break
            YuleD.append(k)
        return YuleD

    @staticmethod
    def derivenew(rho,artistes):        #Calculer la dérivée première de la vraisenmblance selon la définition de dérivée  f’ = f(x+delta)-f(x)/delta
        derive = 0.0
        delta = 0.005
        a = 1/delta
        term_sum1 = 0.0
        term_sum2 = 0.0
        for i in range(1,len(artistes),1):
            term1 = Estimateur.p_k(i,rho+delta)
            term2 = Estimateur.p_k(i,rho)
            term3 = (term1 - term2)/delta
            term_sum1 +=term3
            term_sum2 +=term2
            #term3 = ss.
            term4 = term3/term2
            #term5 = term_sum1 / (1 - term_sum2)
            derive +=artistes[i-1]*(term4 )
            #if i==len(artistes):
                #derive = derive - term5
        term5 = term_sum1 / (1 - term_sum2)
        derive -= artistes[len(artistes)-1]*term5
        return derive

    @staticmethod
    def derive2new(rho,artistes):      #Calculer la dérivée deuxième de la vraisenmblance selon la définition de dérivée
        derive = 0.0
        delta = 0.005
        derive = Estimateur.derivenew(rho+delta,artistes)-Estimateur.derivenew(rho,artistes)
        derive /= delta
        return derive


    @staticmethod
    def trouverRacineNew(precision,artiste):
        start = 1.5
        x1 = start-1
        x2 = start
        while abs(x2-x1)>precision:
            x1 = x2
            term = Estimateur.derivenew(x1,artiste)/Estimateur.derive2new(x1,artiste)
            x2 = x1-term
        return x1


'''
Les programs au-dessous correspondent les questions dans la partie Estimation, veuillez éffacer les signe de commentaire avant de “Run”
'''
'''******************************************************************************************************
   Question 2.1: Comaparer les données observées du tableau 1 avec les donées théoriques
'''
'''
rho = 1.0
N = 1377             #1377 artistes
MaxDis = 16          #maximum du nombre de disques d'or qu'on observe précisement
NomdeArt = [668,244,119,78,55,40,24,32,24,14,16,13,11,5,4,4]    #tableau 1
Nomtheo = []         #liste des données théoriques
for i in range(MaxDis):
    Nomtheo.append(N*Estimateur.p_k(i+1,rho))
plt.plot(np.arange(1,17,1),NomdeArt,color='r',label = 'Données observées')
plt.plot(np.arange(1,17,1),Nomtheo,color = 'b',label = 'Données théoriques')
plt.xlabel('Nombre de disques d\'or')
plt.ylabel('Nombre d\'atristes')
plt.legend(loc='best')
plt.show()
'''

'''*******************************************************************************************************
   Question 2.3: Calculer numériquement l'estimateur du maximum de vraisenmblance
'''
'''
NomdeArt = [668,244,119,78,55,40,24,32,24,14,16,13,11,5,4,4,26]   #tableau 1
precision = 0.001         #precision donée pour la résolution
rho_newton = []           #liste du resultat de chaque etape de la méthode de Newton
start = 1.5               #point de départ
x1 = start-1
x2 = start

while abs(x2-x1)>precision:       # algorithme de Newton
    x1 = x2
    rho_newton.append(x1)
    term = Estimateur.derivenew(x1,NomdeArt)/Estimateur.derive2new(x1,NomdeArt)
    x2 = x1-term                 # mise à jour

plt.plot(rho_newton,color ='g',label='La variation de l\'estimateur')
plt.legend(loc='best')
plt.show()
print ("Le resultat est %f" %(rho_newton[len(rho_newton)-1]))
'''



'''***************************************************************************************************************
   Question 2.4: simulation la convergence de l'estimateur du maximum vraisenmblance
'''
'''
rho = 1
NombreArtInit = 1000      #nombre d'artistes(nombre d'observations) au début
NombreArt = NombreArtInit  #variable utilisé dans la boucle
NombreSimu = 500           #nombre de fois d'augmentation du NombreArt
Step = 100                 #nombre d'augumentation chaque fois
MaxDis = 30                #maximum du nombre de disques d'or qu'on observe précisement
precision = 0.001

rho_estime = []            #liste pour déposer le resultat de l'estimateur correspondant un NombreArt spécifique
for j in range(NombreSimu):
    P_kk = Estimateur.p(rho, MaxDis)
    artistes = []
    NombreArt +=Step
    listArt = Estimateur.Yuledis(rho,P_kk,NombreArt)
    if j % 10==0:
        MaxDis +=1
    for i in range(1,MaxDis,1):
        artistes.append(listArt.count(i))
        if sum(artistes)==NombreArt:
            break
    artistes.append(NombreArt-sum(artistes))
    rho_estime.append(Estimateur.trouverRacineNew(precision,artistes))

plt.plot(np.arange(NombreArtInit,NombreArt,Step),rho_estime,color="r",label = 'valeur de l\'estimateur')
plt.axhline(y=rho, xmin=0, xmax=NombreArt, hold=None,label='valeur théorique')
plt.xlabel('Nombre d\'artistes')
plt.legend(loc='best')
plt.show()
'''



'''**************************************************************************************************************
   Question 2.5: Donner la précision de l'estimateur du maximum de vraisenmblance, simulation la loi
'''
'''
NombreArt = 2000      #nombre d'artistes
NombreObe = 2000      #fois de simulation
MaxDis = 40
rho = 1.0             #paramètre théorique
rho_norm = []
precision =  0.001

P_k = Estimateur.p(rho, MaxDis)
for i in range(NombreObe):           # loi proposée
    artistes = []
    listArt = Estimateur.Yuledis(rho,P_k,NombreArt)
    for i in range(1,MaxDis,1):
        artistes.append(listArt.count(i))
        if sum(artistes)==NombreArt:
            break
    artistes.append(NombreArt-sum(artistes))
    rho_estime = Estimateur.trouverRacineNew(precision, artistes)
    #    print(rho_estime)
    var_rho = -1*Estimateur.derive2new(rho_estime, artistes)      #variance
    var_rho = np.sqrt(var_rho)
    #    print(var_rho)
    rho_norm.append(var_rho*(rho_estime-rho))

x=np.linspace(-3,3,1000)
y=sps.norm.pdf(x)
plt.plot(x,y,color="r",label=r"Densité de $N(0,1)$")
plt.hist(rho_norm,bins=20,normed=1,range=(-3,3),label=r"$(-\frac{\partial^2\ln L(\rho)}{\partial \rho^2})_{\rho_t}^{\frac{1}{2}}(\rho^{\ast}_n - \rho_t)$")
plt.legend(loc='best')
plt.show()
'''
