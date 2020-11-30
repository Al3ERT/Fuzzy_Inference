from Fuzzy_Model import *
import numpy as np
from matplotlib import pyplot
import random

poco = FuzzySet("Poco",ZFunction(0,40))
medio = FuzzySet("Medio",Gaussian(25,40,60,75))
lleno = FuzzySet("Lleno",SFunction(60,100))
tanque = Variable("Tanque",poco,medio,lleno)
cisterna = Variable("Cisterna",poco,medio,lleno)

pocoprob = FuzzySet("Poco",Bell(20,20))
prob = FuzzySet("Probable",Bell(50,30))
muyprob = FuzzySet("Muy",Bell(80,20))
probdeentr = Variable("Entrada",pocoprob,prob,muyprob)

gastoleve = FuzzySet("Leve",Triangular(0,20,40))
gastomoderado = FuzzySet("Moderado",Triangular(20,50,80))
gastoelev = FuzzySet("Elevado",Triangular(60,80,100))
gastotanque = Variable("Gasto",gastoleve,gastomoderado,gastoelev)

aguasembradio = FuzzyModel(entries=[tanque,cisterna,probdeentr],results = [gastotanque])
aguasembradio.add_rule(tanque["Lleno"]&cisterna["Lleno"],gastotanque["Elevado"])
aguasembradio.add_rule(tanque["Lleno"]&cisterna["Medio"],gastotanque["Moderado"])
aguasembradio.add_rule(tanque["Lleno"]&cisterna["Poco"]&probdeentr["Probable"]|probdeentr["Muy"],gastotanque["Moderado"])
aguasembradio.add_rule(tanque["Lleno"]&cisterna["Poco"]&probdeentr["Poco"],gastotanque["Leve"])
aguasembradio.add_rule(tanque["Medio"]|tanque["Poco"],gastotanque["Leve"])

probdeentr = [23,31,15,16,83]*10
tcoa = [100]
tboa = [100]
ccoa = [100]
cboa = [100]
aran = np.arange(1,52)
for proba in probdeentr:
    ran = random.random()*100
    viene = ran < proba

    tagua = tcoa[-1]
    cagua = ccoa[-1]
    mam = Mamdani(aguasembradio,tagua,cagua,proba)
    center = Center_of_area(mam[0],0,tagua)
    if center<cagua*2:
        tcoa.append(100)
    else:
        tcoa.append((tagua-(center-cagua*2)))
    if viene:
        ccoa.append(100)
    else:
        if cagua-(center/2) > 0:
            ccoa.append(cagua-(center/2))
        else:
            ccoa.append(0)
    
    
    tagua = tboa[-1]
    cagua = cboa[-1]
    lar = Larsen(aguasembradio,tagua,cagua,proba)
    bisector = Bisector_of_area(lar[0],0,tagua)
    if bisector<cagua*2:
        tboa.append(100)
    else:
        tboa.append((tagua-(bisector-cagua*2)))
    if viene:
        cboa.append(100)
    else:
        if cagua-(bisector/2) > 0:
            cboa.append(cagua-(bisector/2))
        else:
            cboa.append(0)

    

# pyplot.figure(1)
# x = np.arange(0,40,0.01)
# y = [poco.mem_func(i) for i in x]
# pyplot.plot(x,y,label = poco.name)
# x = np.arange(25,75,0.01)
# y = [medio.mem_func(i) for i in x]
# pyplot.plot(x,y,label = medio.name)
# x = np.arange(60,100,0.01)
# y = [lleno.mem_func(i) for i in x]
# pyplot.plot(x,y,label = lleno.name)
# pyplot.suptitle("Niveles en %")
# pyplot.legend()
# pyplot.show()

# pyplot.figure(2)
# x = np.arange(0,40,0.01)
# y = [pocoprob.mem_func(i) for i in x]
# pyplot.plot(x,y,label = pocoprob.name)
# x = np.arange(20,80,0.01)
# y = [prob.mem_func(i) for i in x]
# pyplot.plot(x,y,label = prob.name)
# x = np.arange(60,100,0.01)
# y = [muyprob.mem_func(i) for i in x]
# pyplot.plot(x,y,label = muyprob.name)
# pyplot.suptitle("Probabilidad de entrada de agua")
# pyplot.legend()
# pyplot.show()

# pyplot.figure(3)
# x = np.arange(0,40,0.01)
# y = [gastoleve.mem_func(i) for i in x]
# pyplot.plot(x,y,label = gastoleve.name)
# x = np.arange(20,80,0.01)
# y = [gastomoderado.mem_func(i) for i in x]
# pyplot.plot(x,y,label = gastomoderado.name)
# x = np.arange(60,100,0.01)
# y = [gastoelev.mem_func(i) for i in x]
# pyplot.plot(x,y,label = gastoelev.name)
# pyplot.suptitle("Gasto de agua del dia")
# pyplot.legend()
# pyplot.show()

pyplot.figure(4)
pyplot.plot(aran,tcoa,label = "Tanque con Mamdani + COA")
pyplot.plot(aran,tboa,label = "Tanque con Larsen + BOA")
pyplot.suptitle("Comportamiento de los niveles del tanque")
pyplot.xlabel("Días")
pyplot.ylabel("Niveles de agua")
pyplot.legend()
pyplot.show()

pyplot.figure(5)
pyplot.plot(aran,ccoa,label = "Cisterna con Mamdani + COA")
pyplot.plot(aran,cboa,label = "Cisterna con Larsen + BOA")
pyplot.suptitle("Comportamiento de los niveles de la cisterna")
pyplot.xlabel("Días")
pyplot.ylabel("Niveles de agua")
pyplot.legend()
pyplot.show()
