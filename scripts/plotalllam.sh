dir='/home/orange3xchicken/Documents/PCB-PR-App/'
for element in lambsched_0.98_lamrate_0.13312905995684007_lam_*
do
  python3 ${dir}util/plot.py ${dir}${element}/ &
done
