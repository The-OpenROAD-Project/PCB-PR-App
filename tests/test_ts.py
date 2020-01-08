import sys
sys.path.append("../")
from ucsdpcb import PcbPlacer, PcbRouter, PcbDB, check_output

db = PcbDB.kicadPcbDataBase('bm15.routed.kicad_pcb')
db.printNodes()
placer = PcbPlacer.GridBasedPlacer(db)
placer.set_num_iterations(2501)
placer.set_iterations_moves(30)
placer.set_two_sided(True)
placer.set_rtree(False)
placer.test_placer_flow()
db.printKiCad()
check_output.check_output('output.bm15.routed.kicad_pcb')
