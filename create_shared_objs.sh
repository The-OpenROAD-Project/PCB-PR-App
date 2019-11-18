 #!/bin/bash 
PCBPLACERPATH=./module/SA-PCB/
PCBROUTERPATH=./module/PcbRouter/
KICADDBPATH=./module/KicadParser/

LIBDIR=./lib

gcc -shared ${PCBPLACERPATH}bin/CMakeFiles/PCBPLACERlib.dir/src/GridBasedPlacer.cpp.o ${PCBPLACERPATH}bin/CMakeFiles/PCBPLACERlib.dir/src/globalParam.cpp.o ${PCBPLACERPATH}bin/CMakeFiles/PCBPLACERlib.dir/src/readFiles.cpp.o ${PCBPLACERPATH}bin/CMakeFiles/PCBPLACERlib.dir/src/PcbPlacer_wrapper.cpp.o ${KICADDBPATH}lib/libkicadpcbparser.a -o ${LIBDIR}src/_PcbPlacer.so -lstdc++
