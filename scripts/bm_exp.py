from ucsdpcb import PcbPlacer, PcbDB
import subprocess
import os, sys

path = '/home/orange3xchicken/Documents/PCB-PR-App/module/PCBBenchmarks'

for subdir, dirs, files in os.walk(path):
    for f in files:
        if '.kicad_pcb' not in f or sys.argv[1] not in f:
            continue

        ec = True
        db = PcbDB.kicadPcbDataBase(os.path.join(subdir, f))
        placer = PcbPlacer.GridBasedPlacer(db)
        placer.set_rtree(True)
        placer.set_two_sided(False)
        placer.set_base_lam(0.1329209929630061)
        placer.set_lambda_schedule(0.9753893051539414) 
        placer.set_lamtemp_update(0.8853585421875213)
        placer.set_num_iterations(2001)
        placer.set_iterations_moves(25)
        placer.set_bb_ec(ec)
        placer.test_placer_flow()
       
        db.printKiCad("./cache")
        subprocess.call('mv ./cache ./exp_'+f.split('.')[0], shell=True)
        subprocess.call('mkdir ./cache',shell=True)
        subprocess.call('mkdir ./cache/img',shell=True)
