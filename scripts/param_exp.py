from ucsdpcb import PcbPlacer, PcbDB
import subprocess
from tqdm import tqdm

#lamtemprates = [0.9, 0.92, 0.94, 0.96, 0.98, 0.99, 0.995]
#lamtemprates = [0.8, 0.85, 0.88, 0.89, 0.91]
lamtemprates = [0.25, 0.2, 0.18, 0.17, 0.15, 0.13, 0.11]
lambda_schedules = [0.975011, 0.973063, 0.971118]
wl_schedules = []
toremove = ['micro_accept_probs','micro_dcongestion','micro_dcost','micro_dhpwl','micro_doverlap','micro_movement','micro_window_coef_history','nodes.nodes',]
for lamb in tqdm(lambda_schedules):
    for lamtemp in lamtemprates:
        db = PcbDB.kicadPcbDataBase('./module/BBBC_testcase_with_temp_back_courtyards.kicad_pcb')
        placer = PcbPlacer.GridBasedPlacer(db)
        placer.set_rtree(True)
        placer.set_two_sided(True)
        placer.set_base_lam(lamtemp)
        placer.set_lamtemp_update(0.91)
        placer.set_lambda_schedule(lamb)
        placer.test_placer_flow()
        db.printKiCad("./cache")
        #subprocess.call('python3 plot.py',shell=True,cwd='/home/orange3xchicken/Documents/PCB-PR-App/util')
        #subprocess.call('rm ./cache/*.pl',shell=True)
        #subprocess.call('rm ./cache/*.rad',shell=True)
        #subprocess.call('rm -rf ./cache/img',shell=True)
        #subprocess.call('rm ./cache/*_history',shell=True)
        #for fm in toremove:
        #    subprocess.call('rm ./cache/'+fm,shell=True)
        subprocess.call('mv ./cache ./lambsched_'+str(lamb)+'_lamrate_'+str(lamtemp),shell=True)
        subprocess.call('mkdir ./cache',shell=True)
        subprocess.call('mkdir ./cache/img',shell=True)
