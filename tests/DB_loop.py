import sys
sys.path.append("../")
from ucsdpcb import PcbPlacer, PcbRouter, PcbDB
from difflib import SequenceMatcher

db = PcbDB.kicadPcbDataBase('../module/PCBBenchmarks/bm9/bm9.routed.kicad_pcb')
db.printKiCad(folderName='./cache', fileNameStamp="0")
postfix = "bm9.routed.kicad_pcb"
for i in range(1,250):
  prefix = "./cache/output." + str(i-1) + "."
  fname = prefix + postfix
  db = PcbDB.kicadPcbDataBase(fname)
  db.printKiCad(folderName='./cache', fileNameStamp=str(i))
  if i > 100:
      prevprefix = "./cache/output." + str(i-2) +"."
      prevfname = prevprefix + postfix
      text1 = open(fname).read()
      text2 = open(prevfname).read()  
      m = SequenceMatcher(None, text1, text2)
      print(m.ratio())
      assert m.ratio() == 1.0
