import numpy as np
from ucsdpcb import PcbDB, PcbPlacer
import subprocess
import dlib
from tqdm import tqdm
import sys
import importlib

lamrates = [0.1,0.25]
temperatures = [0.88,0.95]
lambda_schedules = [0.95, 0.98]
is_integer_variable = [False, False, False]

fname = './module/PCBBenchmarks/'+sys.argv[1]+'/'+sys.argv[1]+'.routed.kicad_pcb'
db = PcbDB.kicadPcbDataBase(fname)
placer = PcbPlacer.GridBasedPlacer(db)

placer.set_rtree(False)
placer.set_two_sided(False)
placer.set_base_lam(0.1329209929630061)
placer.set_lamtemp_update(0.8853585421875213)
placer.set_lambda_schedule(0.9753893051539414)


def place():
    wl = placer.test_placer_flow()
    return wl

wls = []
for _ in range(10):
    wl = place()
    wls.append(wl)

print(np.std(wls))
