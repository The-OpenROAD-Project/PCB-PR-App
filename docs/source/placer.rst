API for PCB Simulated Annealing Placer
======================================

.. cpp:class:: GridBasedPlacer()

  This is the placer class. You will need to instantiate an instance of this class to run a placement job.

.. cpp:function:: void GridBasedPlacer::test_hplacer_flow()

        This is the main function that runs placement.

Getters
^^^^^^^
.. cpp:function:: double GridBasedPlacer::get_total_cost()

  Gets the total weighted cost (badness) of the current placement.

.. cpp:function:: double GridBasedPlacer::get_wirelength_cost()

  Gets the total weighted cost of the wire length.

.. cpp:function:: double GridBasedPlacer::get_overlap_cost()

  Gets the total weighted cost of overlap.

.. cpp:function:: double GridBasedPlacer::get_temperature()

  Gets the current temperature.

Setters
^^^^^^^
.. cpp:function:: void GridBasedPlacer::set_base_lam(double _lam)
.. cpp:function:: void GridBasedPlacer::set_bb_ec(bool _bb)

.. cpp:function:: void GridBasedPlacer::set_wirelength_weight(double _cst)
.. cpp:function:: void GridBasedPlacer::set_lambda_schedule(double _lsched)
.. cpp:function:: void GridBasedPlacer::set_two_sided(bool _2sided)
.. cpp:function:: void GridBasedPlacer::set_initial_move_radius(double _eps)

  Sets the starting move radius. The move radius decreases automatically during placement.

.. cpp:function:: void GridBasedPlacer::set_rtree(bool _rt)

  Sets the usage of rtree data structure for detecting overlap. This can provide faster performance on large designs.

.. cpp:function:: void GridBasedPlacer::set_lam(bool _lam)
.. cpp:function:: void GridBasedPlacer::set_lamtemp_update(double _coef)
.. cpp:function:: void GridBasedPlacer::set_num_iterations(int iter)

  Sets the number of annealing iterations (temperature updates).

.. cpp:function:: void GridBasedPlacer::set_iterations_moves(int iter)

  Sets the number of moves per component during annealing. The total moves per temperature update will be this number times the number of components.

.. cpp:function:: void GridBasedPlacer::set_initial_temperature(double tmp)