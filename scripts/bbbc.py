from ucsdpcb import PcbPlacer, PcbDB
import subprocess
from tqdm import tqdm

lamrates = [0.03,0.05,0.07,0.09,0.11,0.13,0.15,0.17,0.19,0.12, 0.14, 0.16, 0.18]
toremove = ['micro_accept_probs','micro_dcongestion','micro_dcost','micro_dhpwl','micro_doverlap','micro_movement','micro_window_coef_history','nodes.nodes',]
for lam in tqdm(lamrates):
    db = PcbDB.kicadPcbDataBase('./module/BBBC2.kicad_pcb')
    placer = PcbPlacer.GridBasedPlacer(db)
    placer.set_rtree(True)
    placer.set_two_sided(True)
    placer.set_base_lam(lam)
    placer.test_placer_flow()
    db.printKiCad("./cache")
    #subprocess.call('python3 plot.py',shell=True,cwd='/home/orange3xchicken/Documents/PCB-PR-App/util')
    #subprocess.call('rm ./cache/*.pl',shell=True)
    #subprocess.call('rm ./cache/*.rad',shell=True)
    #subprocess.call('rm -rf ./cache/img',shell=True)
    #subprocess.call('rm ./cache/*_history',shell=True)
    #for fm in toremove:
    #    subprocess.call('rm ./cache/'+fm,shell=True)
    subprocess.call('mv ./cache ./lam_'+str(lam),shell=True)
    subprocess.call('mkdir ./cache',shell=True)
    subprocess.call('mkdir ./cache/img',shell=True)
