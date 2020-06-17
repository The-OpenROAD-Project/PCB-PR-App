from ucsdpcb import PcbPlacer, PcbDB


#db = PcbDB.kicadPcbDataBase('./module/BBBC_ctyd.kicad_pcb')
#db = PcbDB.kicadPcbDataBase('./module/BBBC_0507.kicad_pcb')
#db = PcbDB.kicadPcbDataBase('./module/BBBC_testcase.kicad_pcb')
db = PcbDB.kicadPcbDataBase('./module/BBBC_testcase_with_temp_back_courtyards.kicad_pcb')
#db = PcbDB.kicadPcbDataBase('./module/PCBBenchmarks/bm2/bm2.routed.kicad_pcb')
#db = PcbDB.kicadPcbDataBase('./module/PCBBenchmarks/bm7/bm7.routed.kicad_pcb')


placer = PcbPlacer.GridBasedPlacer(db)
placer.set_rtree(True)
placer.set_two_sided(False)
placer.set_bb_ec(False)
placer.set_base_lam(0.1329209929630061)
placer.set_lambda_schedule(0.9753893051539414) 
placer.set_lamtemp_update(0.8853585421875213)
placer.set_num_iterations(2001)
placer.set_iterations_moves(25)
#placer.set_overlap_weight(0)
placer.test_placer_flow()
db.printKiCad("./cache")

