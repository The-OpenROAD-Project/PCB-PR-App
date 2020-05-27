
rm bm*.log output.bm*.kicad_pcb

time python3 run_layout.py PCBBenchmarks/bm1/bm1.routed.kicad_pcb > bm1.log &
time python3 run_layout.py PCBBenchmarks/bm2/bm2.routed.kicad_pcb > bm2.log &
time python3 run_layout.py PCBBenchmarks/bm3/bm3.routed.kicad_pcb > bm3.log &
time python3 run_layout.py PCBBenchmarks/bm4/bm4.routed.kicad_pcb > bm4.log &
time python3 run_layout.py PCBBenchmarks/bm5/bm5.routed.kicad_pcb > bm5.log &
time python3 run_layout.py PCBBenchmarks/bm6/bm6.routed.kicad_pcb > bm6.log &
time python3 run_layout.py PCBBenchmarks/bm7/bm7.routed.kicad_pcb > bm7.log &
time python3 run_layout.py PCBBenchmarks/bm8/bm8.routed.kicad_pcb > bm8.log &
time python3 run_layout.py PCBBenchmarks/bm9/bm9.routed.kicad_pcb > bm9.log &
time python3 run_layout.py PCBBenchmarks/bm10/bm10.routed.kicad_pcb > bm10.log &
time python3 run_layout.py PCBBenchmarks/bm11/bm11.routed.kicad_pcb > bm11.log &
time python3 run_layout.py PCBBenchmarks/bm11/bm12.routed.kicad_pcb > bm12.log &
time python3 run_layout.py PCBBenchmarks/bm11/bm13.routed.kicad_pcb > bm13.log &

