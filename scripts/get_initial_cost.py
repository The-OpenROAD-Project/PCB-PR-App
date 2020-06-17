from ucsdpcb import PcbPlacer, PcbDB
import sys

db = PcbDB.kicadPcbDataBase(sys.argv[1])
placer = PcbPlacer.GridBasedPlacer(db)
placer.set_bb_ec(False)
placer.set_rtree(True)
placer.set_two_sided(True)
placer.set_num_iterations(1)
placer.set_iterations_moves(1)
placer.test_placer_flow()
