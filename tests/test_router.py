import sys
sys.path.append("../")
from ucsdpcb import PcbPlacer, PcbRouter, PcbDB

db = PcbDB.kicadPcbDataBase('./output.bm12.routed.kicad_pcb')
db.printNodes()
router = PcbRouter.GridBasedRouter(db)
router.set_grid_scale(20)
router.set_num_iterations(10)
router.set_enlarge_boundary(20)
router.set_layer_change_weight(1000)
router.route()
db.printKiCad()
