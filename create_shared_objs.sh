#!/bin/bash 
PCBPLACERPATH=./module/SA-PCB/
PCBROUTERPATH=./module/PcbRouter/
KICADDBPATH=./module/KicadParser/

LIBDIR=./ucsdpcb/

gcc -shared ${PCBPLACERPATH}bin/CMakeFiles/PCBPLACERlib.dir/src/GridBasedPlacer.cpp.o ${PCBPLACERPATH}bin/CMakeFiles/PCBPLACERlib.dir/src/globalParam.cpp.o ${PCBPLACERPATH}bin/CMakeFiles/PCBPLACERlib.dir/src/readFiles.cpp.o ${PCBPLACERPATH}bin/CMakeFiles/PCBPLACERlib.dir/src/PcbPlacer_wrapper.cpp.o ${KICADDBPATH}lib/libkicadpcbparser.a -o ${LIBDIR}_PcbPlacer.so -lstdc++

gcc -shared ${PCBROUTERPATH}bin/CMakeFiles/pcbrouterlib.dir/src/BoardGrid.cpp.o ${PCBROUTERPATH}bin/CMakeFiles/pcbrouterlib.dir/src/GridBasedRouter.cpp.o ${PCBROUTERPATH}bin/CMakeFiles/pcbrouterlib.dir/src/globalParam.cpp.o ${PCBROUTERPATH}bin/CMakeFiles/pcbrouterlib.dir/src/GridNetclass.cpp.o ${PCBROUTERPATH}bin/CMakeFiles/pcbrouterlib.dir/src/PcbRouter_wrapper.cpp.o ${KICADDBPATH}lib/libkicadpcbparser.a -o ${LIBDIR}_PcbRouter.so -lstdc++

gcc -shared ${KICADDBPATH}bin/CMakeFiles/kicadpcbparserlib.dir/src/kicadPcbDataBase.cpp.o ${KICADDBPATH}bin/CMakeFiles/kicadpcbparserlib.dir/src/kicadParser.cpp.o ${KICADDBPATH}bin/CMakeFiles/kicadpcbparserlib.dir/src/shape.cpp.o ${KICADDBPATH}bin/CMakeFiles/kicadpcbparserlib.dir/src/util.cpp.o ${KICADDBPATH}bin/CMakeFiles/kicadpcbparserlib.dir/src/PcbDB_wrapper.cpp.o ${KICADDBPATH}lib/libkicadpcbparser.a -o ${LIBDIR}_PcbDB.so -lstdc++

cp ${PCBPLACERPATH}src/PcbPlacer.py ./ucsdpcb
cp ${PCBROUTERPATH}src/PcbRouter.py ./ucsdpcb
cp ${KICADDBPATH}src/PcbDB.py ./ucsdpcb
