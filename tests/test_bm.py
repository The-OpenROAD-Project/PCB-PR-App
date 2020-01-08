import sys
sys.path.append("../")
from ucsdpcb import PcbPlacer, PcbRouter, PcbDB

db = PcbDB.kicadPcbDataBase('./')
db.printNodes()
placer = PcbPlacer.GridBasedPlacer(db)
placer.set_num_iterations(601)
placer.set_iterations_moves(28)
placer.set_two_sided(False)
placer.set_rtree(False)
placer.test_placer_flow()
db.printKiCad()
