import sys
sys.path.append("../")
from ucsdpcb import PcbPlacer, PcbRouter, PcbDB

db = PcbDB.kicadPcbDataBase('../module/PCBBenchmarks/bm9/bm9.routed.kicad_pcb')
db.printNodes()
placer = PcbPlacer.GridBasedPlacer(db)
placer.set_num_iterations(1)
placer.set_iterations_moves(1)
placer.set_initial_temperature(99999999999)

cost = 0
cost_hist = [cost]
for i in range(0,10):
  placer.test_placer_flow()
  cost = placer.get_accept_ratio()
  assert accept_ratio > -.99
