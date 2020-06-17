from ucsdpcb import PcbPlacer, PcbDB,  PcbRouter

db = PcbDB.kicadPcbDataBase('./module/PCBBenchmarks/bm9/bm9.routed.kicad_pcb')
db.printNodes()
placer = PcbPlacer.GridBasedPlacer(db)
placer.set_iterations_moves(1)
placer.set_num_iterations(1)
placer.test_placer_flow()
db.printNodes()
router = PcbRouter.GridBasedRouter(db)
router.set_num_ripup_reroute_iteration(1)
router.route_all_net_with_ripup_and_reroute()
db.printKiCad()
