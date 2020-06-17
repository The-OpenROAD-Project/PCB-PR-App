from ucsdpcb import PcbPlacer, PcbDB, PcbRouter
import sys

db = PcbDB.kicadPcbDataBase(sys.argv[1])
router = PcbRouter.GridBasedRouter(db)
router.set_grid_scale(20)
router.set_num_iterations(20)
router.set_track_obstacle_weight(30)
router.route()
