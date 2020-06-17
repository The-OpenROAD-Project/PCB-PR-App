from ucsdpcb import PcbPlacer, PcbDB

db = PcbDB.kicadPcbDataBase('./module/PCBBenchmarks/bm9/bm9.routed.kicad_pcb')
placer = PcbPlacer.GridBasedPlacer(db)
placer.set_rtree(False)
placer.test_placer_flow()

