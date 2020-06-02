API for PCB Router
==================

.. cpp:class:: GridBasedRouter

.. cpp:function:: GridBasedRouter::GridBasedRouter(kicadPcbDataBase &db)


.. cpp:function:: void GridBasedRouter::initialization()

  :func:`initialization` must be called before :func:`route`.

.. cpp:function:: void GridBasedRouter::route()

  Initiates an autorouting job.


Setters
^^^^^^^

.. cpp:function:: void GridBasedRouter::set_grid_scale(const int _iS)
.. cpp:function:: void GridBasedRouter::set_num_iterations(const int _numRRI)
.. cpp:function:: void GridBasedRouter::set_enlarge_boundary(const int _eB)

.. cpp:function:: void GridBasedRouter::set_wirelength_weight(const double _ww) 
.. cpp:function:: void GridBasedRouter::set_diagonal_wirelength_weight(const double _dww) 
.. cpp:function:: void GridBasedRouter::set_layer_change_weight(const double _lCC)

.. cpp:function:: void GridBasedRouter::set_track_obstacle_weight(const double _toc)
.. cpp:function:: void GridBasedRouter::set_via_obstacle_weight(const double _voc) 
.. cpp:function:: void GridBasedRouter::set_pad_obstacle_weight(const double _poc) 

.. cpp:function:: void GridBasedRouter::set_track_obstacle_step_size(const double _tocss) 
.. cpp:function:: void GridBasedRouter::set_via_obstacle_step_size(const double _vocss)

.. cpp:function:: void GridBasedRouter::set_net_layer_pref_weight(const int _netId, const std::string &_layerName, const int _weight)
.. cpp:function:: void GridBasedRouter::set_net_all_layers_pref_weights(const int _netId, const int _weight)

Getters
^^^^^^^

.. cpp:function:: unsigned int GridBasedRouter::get_grid_scale()
.. cpp:function:: unsigned int GridBasedRouter::get_num_iterations() 
.. cpp:function:: unsigned int GridBasedRouter::get_enlarge_boundary() 

.. cpp:function:: double GridBasedRouter::get_wirelength_weight() 
.. cpp:function:: double GridBasedRouter::get_diagonal_wirelength_weight() 
.. cpp:function:: double GridBasedRouter::get_layer_change_weight()

.. cpp:function:: double GridBasedRouter::get_track_obstacle_weight()
.. cpp:function:: double GridBasedRouter::get_via_obstacle_weight()
.. cpp:function:: double GridBasedRouter::get_pad_obstacle_weight()
.. cpp:function:: double GridBasedRouter::get_track_obstacle_step_size() 
.. cpp:function:: double GridBasedRouter::get_via_obstacle_step_size()

.. cpp:function:: double GridBasedRouter::get_total_cost()
.. cpp:function:: double GridBasedRouter::get_routed_wirelength()
.. cpp:function:: double GridBasedRouter::get_routed_wirelength(std::vector<MultipinRoute> &mpr)
.. cpp:function:: int GridBasedRouter::get_routed_num_vias()
.. cpp:function:: int GridBasedRouter::get_routed_num_vias(std::vector<MultipinRoute> &mpr)
.. cpp:function:: int GridBasedRouter::get_routed_num_bends()
.. cpp:function:: int GridBasedRouter::get_routed_num_bends(std::vector<MultipinRoute> &mpr)