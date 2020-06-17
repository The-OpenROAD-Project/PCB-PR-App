from ucsdpcb import PcbPlacer, PcbDB
import subprocess
import dlib
from tqdm import tqdm
import sys

lamrates = [0.1,0.25]
temperatures = [0.88,0.95]
lambda_schedules = [0.95, 0.98]
is_integer_variable = [False, False, False]
fname ='BBBC'
kpfile = './module/BBBC_testcase_with_temp_back_courtyards.kicad_pcb'
#fname = './module/PCBBenchmarks/'+sys.argv[1]+'/'+sys.argv[1]+'.routed.kicad_pcb'

def place(lamrate, lam_temperature_update, lambda_schedule):
    lamb = lambda_schedule
    lamtemp = lamrate
    db = PcbDB.kicadPcbDataBase(kpfile)
    placer = PcbPlacer.GridBasedPlacer(db)
    placer.set_bb_ec(False)
    placer.set_rtree(True)
    placer.set_two_sided(True)
    placer.set_base_lam(lamtemp)
    placer.set_lamtemp_update(lam_temperature_update)
    placer.set_lambda_schedule(lamb)
    wl = placer.test_placer_flow()
    db.printKiCad("./cache")
    subprocess.call('mv ./cache ./'+fname+'_lambsched_'+str(lamb)+'_lamrate_'+str(lamtemp)+'_lam_temp_'+str(lam_temperature_update),shell=True)
    subprocess.call('mkdir ./cache',shell=True)
    subprocess.call('mkdir ./cache/img',shell=True)
    out = (str(lamb), str(lamtemp), str(lam_temperature_update), str(wl))

    with open('./'+fname+'_log.txt','a+') as f:
        f.write(out[0] + ',' + out[1] + ',' + out[2] + ',' + out[3] + '\n')
    return wl

x,wl = dlib.find_min_global(place, [lamrates[0], temperatures[0], lambda_schedules[0]],
    [lamrates[1], temperatures[1], lambda_schedules[1]],
    is_integer_variable, 100)

print('params',x)
print('wl',wl)
