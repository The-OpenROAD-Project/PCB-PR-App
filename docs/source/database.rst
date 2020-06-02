API for PCB Design Database
===========================

.. cpp:class:: kicadPcbDataBase

.. cpp:function:: kicadPcbDataBase(std::string fileName)

  The main database class for a design. The fileName parameter should be the filename of a .kicad_pcb file.


Initialization
^^^^^^^^^^^^^^
.. cpp:function:: bool buildKicadPcb()
.. cpp:function:: void removeRoutedSegmentsAndVias()

Removes all routing, in preparation for autorouting.


Print Helpers
^^^^^^^^^^^^^

These functions print information to stdout to aid in logging, reporting, and debugging.

.. cpp:function:: void printLayer()
.. cpp:function:: void printNet()
.. cpp:function:: void printInst()
.. cpp:function:: void printComp()
.. cpp:function:: void printNetclass()
.. cpp:function:: void printPcbRouterInfo()
.. cpp:function:: void printFile()
.. cpp:function:: void printSegment()
.. cpp:function:: void printUnconnectedPins()
.. cpp:function:: void printKiCad(const std::string folderName = "", const std::string fileNameStamp = "", const std::string fileName = "", const bool verbose = false)
.. cpp:function:: void printNodes()
.. cpp:function:: void printLockedInst()
.. cpp:function:: void printDesignStatistics()
.. cpp:function:: void printRoutedSegmentsWLAndNumVias()

Getters
^^^^^^^

.. cpp:function:: void getBoardBoundaryByEdgeCuts(double &minX, double &maxX, double &minY, double &maxY)
  
  Gets the board boundary using the Edge.Cuts layer. This is the prefered method over :func:`getBoardBoundaryByPinLocation`.

.. cpp:function:: void getBoardBoundaryByPinLocation(double &minX, double &maxX, double &minY, double &maxY)

  Gets the board boundary using the pins locations. Using Edge.Cuts is prefered (:func:`getBoardBoundaryByEdgeCuts`).


.. cpp:function:: bool getPcbRouterInfo(std::vector<std::set<std::pair<double, double> > > *)
.. cpp:function:: bool getPinPosition(const std::string &inst_name, const std::string &pin_name, point_2d *pos)
.. cpp:function:: bool getPinPosition(const int inst_id, const int &pin_id, point_2d *pos)
.. cpp:function:: void getPinPosition(const padstack &, const instance &, point_2d *pos)
.. cpp:function:: void getPinShapeRelativeCoordsToModule(const padstack &pad, const instance &inst, const points_2d &coords, points_2d *coordsRe)
.. cpp:function:: bool getPinPosition(const Pin &p, point_2d *pos)
.. cpp:function:: bool getCompBBox(const int compId, point_2d *bBox)
.. cpp:function:: std::vector<int> getPinLayer(const int &instId, const int &padStackId)

.. cpp:function:: void getPadstackRotatedWidthAndHeight(const instance &inst, const padstack &pad, double &width, double &height)

  // TODO:: Move this to instance or overloaded this to Instance

.. cpp:function:: bool getInstance(const std::string &, instance *&)
.. cpp:function:: bool getComponent(const std::string &, component *&)
.. cpp:function:: bool getNet(const std::string &, net *&)

.. cpp:function:: component &getComponent(const int id)
.. cpp:function:: instance &getInstance(const int id)
.. cpp:function:: net &getNet(const int id)
.. cpp:function:: netclass &getNetclass(const int id)

.. cpp:function:: std::string getFileName()
.. cpp:function:: std::vector<instance> &getInstances()
.. cpp:function:: std::vector<component> &getComponents()
.. cpp:function:: std::vector<net> &getNets()
.. cpp:function:: std::vector<Pin> &getUnconnectedPins()
.. cpp:function:: std::vector<netclass> &getNetclasses()

.. cpp:function:: int getInstancesCount()
.. cpp:function:: int getNumNets()
.. cpp:function:: double getLargestClearance()

.. cpp:function:: int getNumCopperLayers()

.. cpp:function:: int getLayerId(const std::string &layerName)

.. cpp:function:: std::map<int, std::string> &getCopperLayers()



Testers
^^^^^^^
.. cpp:function:: bool isInstanceId(const int id)
.. cpp:function:: bool isComponentId(const int id)
.. cpp:function:: bool isNetId(const int id)
.. cpp:function:: bool isNetclassId(const int id)

  // TODO: All layers are copper in the "layer_to_index_map" and "index_to_layer_map"

.. cpp:function:: std::string getLayerName(const int layerId)
.. cpp:function:: bool isCopperLayer(const int)
.. cpp:function:: bool isCopperLayer(const std::string &)

  // TODO: Get design boundary based on rotated pin shape

.. cpp:function:: void testInstAngle()

DRC
^^^
.. cpp:function:: void printClearanceDrc()
