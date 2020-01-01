#!/bin/bash 
PCBPLACERPATH=./module/SA-PCB
PCBROUTERPATH=./module/PcbRouter
KICADDBPATH=./module/KicadParser
LIBDIR=./ucsdpcb
BUILDDIR=./build

rm -r ${BUILDDIR}/*
rm ${LIBDIR}/*

rm ${PCBPLACERPATH}/tmp/*
rm -r ${PCBPLACERPATH}/bin/*
rm -r ${PCBPLACERPATH}/build/*
rm ${PCBPLACERPATH}/src/pcbplacer-stamp/*
rm ${PCBPLACERPATH}/src/PcbPlacer_wrapper.cpp
rm ${PCBPLACERPATH}/src/PcbPlacer.py

rm ${PCBROUTERPATH}/tmp/*
rm -r ${PCBROUTERPATH}/bin/*
rm -r ${PCBROUTERPATH}/build/*
rm ${PCBROUTERPATH}/src/pcbrouter-stamp/*
rm ${PCBROUTERPATH}/src/PcbRouter_wrapper.cpp
rm ${PCBROUTERPATH}/src/PcbRoute.py

rm ${KICADDBPATH}/tmp/*
rm -r ${KICADDBPATH}/bin/*
rm -r ${KICADDBPATH}/build/*
rm ${KICADDBPATH}/src/kicadparser-stamp/*
rm ${KICADDBPATH}/src/PcbDB_wrapper.cpp
rm ${KICADDBPATH}/src/PcbDB.py
