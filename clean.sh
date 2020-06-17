#!/bin/bash 
PCBPLACERPATH=./module/SA-PCB
PCBROUTERPATH=./module/PcbRouter
KICADDBPATH=./module/KicadParser
LIBDIR=./ucsdpcb
BUILDDIR=./build

rm -r ${BUILDDIR}/*
rm ${LIBDIR}/*

while [ $# -ne 0 ]
do
    arg="$1"
    case "$arg" in
        placer)
            plcr=true
            ;;
        router)
            rtr=true
            ;;
        parser)
            db=true
            ;;
        *)
            all="true"
            ;;
    esac
    shift
done

if [ "$plcr" = true ] || [ "$all" = true ]; then
	rm ${PCBPLACERPATH}/tmp/*
	rm -r ${PCBPLACERPATH}/bin/*
	rm -r ${PCBPLACERPATH}/build/*
	rm ${PCBPLACERPATH}/src/pcbplacer-stamp/*
	rm ${PCBPLACERPATH}/src/PcbPlacer_wrapper.cpp
	rm ${PCBPLACERPATH}/src/PcbPlacer.py
fi
if [ "$rtr" = true ] || [ "$all" = true ]; then
	rm ${PCBROUTERPATH}/tmp/*
	rm -r ${PCBROUTERPATH}/bin/*
	rm -r ${PCBROUTERPATH}/build/*
	rm ${PCBROUTERPATH}/src/pcbrouter-stamp/*
	rm ${PCBROUTERPATH}/src/PcbRouter_wrapper.cpp
	rm ${PCBROUTERPATH}/src/PcbRouter.py
fi
if [ "$db" = true ] || [ "$all" = true ]; then
	rm ${KICADDBPATH}/tmp/*
	rm -r ${KICADDBPATH}/bin/*
	rm -r ${KICADDBPATH}/build/*
	rm ${KICADDBPATH}/src/kicadparser-stamp/*
	rm ${KICADDBPATH}/src/PcbDB_wrapper.cpp
	rm ${KICADDBPATH}/src/PcbDB.py
fi
