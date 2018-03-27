# coding: UTF-8
#  alpspython SpinIceMPI6.py
# 

import pyalps
import matplotlib.pyplot as plt
import pyalps.plot

#prepare the input parameters
parms = []
for l in [4]: 
    for t in [3.0, 2.5, 2.0, 1.5]:
        parms.append(
            { 
              'LATTICE_LIBRARY': "./lattices_pyrochlore_cubic.xml",
              'LATTICE'        : "pyrochlore_spin_ice cubic lattice",
              'T'              : t,
              'J'              : -1.0 ,
              'THERMALIZATION' : 50000,
              'SWEEPS'         : 100000,
              'UPDATE'         : "local",
              'MODEL'          : "Ising",
              'L'              : l
            }
    )
    for t in [1.4, 1.3, 1.2, 1.1, 1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.45, 0.4, 0.35, 0.3, 0.25, 0.2]:
        parms.append(
            { 
              'LATTICE_LIBRARY': "./lattices_pyrochlore_cubic.xml",
              'LATTICE'        : "pyrochlore_spin_ice cubic lattice",
              'T'              : t,
              'J'              : -1.0 ,
              'THERMALIZATION' : 50000,
              'SWEEPS'         : 100000,
              'UPDATE'         : "local",
              'MODEL'          : "Ising",
              'L'              : l
            }
    )

#write the input file and run the simulation
input_file = pyalps.writeInputFiles('parm_SI',parms)
# pyalps.runApplication('spinmc',input_file,Tmin=5,writexml=True)
# use the following instead if you have MPI
pyalps.runApplication('spinmc',input_file,Tmin=10,MPI=6)

pyalps.evaluateSpinMC(pyalps.getResultFiles(prefix='parm_SI'))

#load C and collect it as function of temperature T
data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parm_SI'),['Specific Heat'])
spec_heat = pyalps.collectXY(data,x='T',y='Specific Heat',foreach=['L'])

#make plots

plt.figure()
pyalps.plot.plot(spec_heat)
plt.xlabel('Temperature $T$')
plt.ylabel('Specific Heat $C_v$')
plt.title('NN Spin Ice model, J = 1, L = 4')
plt.savefig("C_SpinIce_L4.png")


