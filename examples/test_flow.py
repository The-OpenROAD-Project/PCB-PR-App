from ucsdpcb import PcbPlacer, PcbRouter, PcbDB

db = PcbDB.kicadPcbDataBase('../module/PCBBenchmarks/bm9/bm9.routed.kicad_pcb')
db.printNodes()
placer = PcbPlacer.GridBasedPlacer(db)
placer.set_inner_iter(1)
placer.set_outer_iter(2)
placer.test_placer_flow()
db.printNodes()
router = PcbRouter.GridBasedRouter(db)
router.set_num_ripup_reroute_iteration(1)
router.route_all_net_with_ripup_and_reroute()
db.printKiCad()
