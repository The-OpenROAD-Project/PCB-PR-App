dir='/home/orange3xchicken/Documents/PCB-PR-App/'
for element in lamtemp_0.9 lamtemp_0.92 lamtemp_0.94 lamtemp_0.96 lamtemp_0.98 lamtemp_0.99 lamtemp_0.995
do
  python3 ${dir}util/plot.py ${dir}${element}/
done
