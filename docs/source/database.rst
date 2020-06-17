API for Database
================

.. cpp:class:: kicadPcbDataBase

.. cpp:function:: kicadPcbDataBase::kicadPcbDataBase(std::string fileName)

  The main database class for a design. The fileName parameter should be the filename of a .kicad_pcb file.


Initialization
^^^^^^^^^^^^^^
.. cpp:function:: bool kicadPcbDataBase::buildKicadPcb()
.. cpp:function:: void kicadPcbDataBase::removeRoutedSegmentsAndVias()

Removes all routing, in preparation for autorouting.


Print Helpers
^^^^^^^^^^^^^

These functions print information to stdout to aid in logging, reporting, and debugging.

.. cpp:function:: void kicadPcbDataBase::printLayer()
.. cpp:function:: void kicadPcbDataBase::printNet()
.. cpp:function:: void kicadPcbDataBase::printInst()
.. cpp:function:: void kicadPcbDataBase::printComp()
.. cpp:function:: void kicadPcbDataBase::printNetclass()
.. cpp:function:: void kicadPcbDataBase::printPcbRouterInfo()
.. cpp:function:: void kicadPcbDataBase::printFile()
.. cpp:function:: void kicadPcbDataBase::printSegment()
.. cpp:function:: void kicadPcbDataBase::printUnconnectedPins()
.. cpp:function:: void kicadPcbDataBase::printKiCad(const std::string folderName = "", const std::string fileNameStamp = "", const std::string fileName = "", const bool verbose = false)
.. cpp:function:: void kicadPcbDataBase::printNodes()
.. cpp:function:: void kicadPcbDataBase::printLockedInst()
.. cpp:function:: void kicadPcbDataBase::printDesignStatistics()
.. cpp:function:: void kicadPcbDataBase::printRoutedSegmentsWLAndNumVias()

Getters
^^^^^^^

.. cpp:function:: void getBoardBoundaryByEdgeCuts(double &minX, double &maxX, double &minY, double &maxY)
  
  Gets the board boundary using the Edge.Cuts layer. This is the prefered method over :func:`getBoardBoundaryByPinLocation`.

.. cpp:function:: void getBoardBoundaryByPinLocation(double &minX, double &maxX, double &minY, double &maxY)

  Gets the board boundary using the pins locations. Using Edge.Cuts is prefered (:func:`getBoardBoundaryByEdgeCuts`).


.. cpp:function:: bool kicadPcbDataBase::getPcbRouterInfo(std::vector<std::set<std::pair<double, double> > > *)
.. cpp:function:: bool kicadPcbDataBase::getPinPosition(const std::string &inst_name, const std::string &pin_name, point_2d *pos)
.. cpp:function:: bool kicadPcbDataBase::getPinPosition(const int inst_id, const int &pin_id, point_2d *pos)
.. cpp:function:: void kicadPcbDataBase::getPinPosition(const padstack &, const instance &, point_2d *pos)
.. cpp:function:: void kicadPcbDataBase::getPinShapeRelativeCoordsToModule(const padstack &pad, const instance &inst, const points_2d &coords, points_2d *coordsRe)
.. cpp:function:: bool kicadPcbDataBase::getPinPosition(const Pin &p, point_2d *pos)
.. cpp:function:: bool kicadPcbDataBase::getCompBBox(const int compId, point_2d *bBox)
.. cpp:function:: std::vector<int> kicadPcbDataBase::getPinLayer(const int &instId, const int &padStackId)

.. cpp:function:: void kicadPcbDataBase::getPadstackRotatedWidthAndHeight(const instance &inst, const padstack &pad, double &width, double &height)

  // TODO:: Move this to instance or overloaded this to Instance

.. cpp:function:: bool kicadPcbDataBase::getInstance(const std::string &, instance *&)
.. cpp:function:: bool kicadPcbDataBase::getComponent(const std::string &, component *&)
.. cpp:function:: bool kicadPcbDataBase::getNet(const std::string &, net *&)

.. cpp:function:: component &kicadPcbDataBase::getComponent(const int id)
.. cpp:function:: instance &kicadPcbDataBase::getInstance(const int id)
.. cpp:function:: net &kicadPcbDataBase::getNet(const int id)
.. cpp:function:: netclass &kicadPcbDataBase::getNetclass(const int id)

.. cpp:function:: std::string kicadPcbDataBase::getFileName()
.. cpp:function:: std::vector<instance> &kicadPcbDataBase::getInstances()
.. cpp:function:: std::vector<component> &kicadPcbDataBase::getComponents()
.. cpp:function:: std::vector<net> &kicadPcbDataBase::getNets()
.. cpp:function:: std::vector<Pin> &kicadPcbDataBase::getUnconnectedPins()
.. cpp:function:: std::vector<netclass> &kicadPcbDataBase::getNetclasses()

.. cpp:function:: int kicadPcbDataBase::getInstancesCount()
.. cpp:function:: int kicadPcbDataBase::getNumNets()
.. cpp:function:: double kicadPcbDataBase::getLargestClearance()

.. cpp:function:: int kicadPcbDataBase::getNumCopperLayers()

.. cpp:function:: int kicadPcbDataBase::getLayerId(const std::string &layerName)

.. cpp:function:: std::map<int, std::string> &kicadPcbDataBase::getCopperLayers()



Testers
^^^^^^^
.. cpp:function:: bool kicadPcbDataBase::isInstanceId(const int id)
.. cpp:function:: bool kicadPcbDataBase::isComponentId(const int id)
.. cpp:function:: bool kicadPcbDataBase::isNetId(const int id)
.. cpp:function:: bool kicadPcbDataBase::isNetclassId(const int id)

  // TODO: All layers are copper in the "layer_to_index_map" and "index_to_layer_map"

.. cpp:function:: std::string kicadPcbDataBase::getLayerName(const int layerId)
.. cpp:function:: bool kicadPcbDataBase::isCopperLayer(const int)
.. cpp:function:: bool kicadPcbDataBase::isCopperLayer(const std::string &)

  // TODO: Get design boundary based on rotated pin shape

.. cpp:function:: void kicadPcbDataBase::testInstAngle()

DRC
^^^
.. cpp:function:: void kicadPcbDataBase::printClearanceDrc()
