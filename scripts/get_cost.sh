dir='/home/orange3xchicken/Documents/PCB-PR-App/module/PCBBenchmarks'

for bm in bm1 bm2 bm3 bm4 bm5 bm6 bm7 bm8 bm9 bm10 bm11 bm12 bm13
do
  python3 get_initial_cost.py ./exp_${bm}/*.kicad_pcb > ./${bm}_auto_result.txt
  python3 get_initial_cost.py ${dir}/${bm}/*.kicad_pcb > ./${bm}_manual_result.txt
done
