import PcbPlacer, PcbRouter, PcbDB

db = PcbDB.kicadPcbDataBase('../module/PCBBenchmarks/bm9/bm9.routed.kicad_pcb')

placer = PcbPlacer.GridBasedPlacer(db)

placer.test_placer_flow()
