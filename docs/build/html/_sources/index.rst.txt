.. PCB-PR-App documentation master file, created by
   sphinx-quickstart on Tue Jun  2 20:30:43 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PCB-PR-App's documentation!
======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


.. cpp:class:: GridBasedPlacer

.. cpp:function:: void test_hplacer_flow()

        This is the main function that runs placement.

Getters
^^^^^^^
.. cpp:function:: double get_total_cost()

        Gets the total weighted cost (badness) of the current placement.

.. cpp:function:: double get_wirelength_cost()

        Gets the total weighted cost of the wirelength.

.. cpp:function:: double get_overlap_cost()

        Gets the total weighted cost of overlap.

.. cpp:function:: double get_temperature()

        Gets the current temperature.

Setters
^^^^^^^
.. cpp:function:: void set_base_lam(double _lam)
.. cpp:function:: void set_bb_ec(bool _bb)

.. cpp:function:: void set_wirelength_weight(double _cst)
.. cpp:function:: void set_lambda_schedule(double _lsched)
.. cpp:function:: void set_two_sided(bool _2sided)
.. cpp:function:: void set_initial_move_radius(double _eps)

        Sets the starting move radius. The move radius decreases automatically during placement.

.. cpp:function:: void set_rtree(bool _rt)

        Sets the usage of rtree data structure for detecting overlap. This can provide faster performance on large designs.

.. cpp:function:: void set_lam(bool _lam)
.. cpp:function:: void set_lamtemp_update(double _coef)
.. cpp:function:: void set_num_iterations(int iter)

        Sets the number of annealing iterations (temperature updates).

.. cpp:function:: void set_iterations_moves(int iter)

        Sets the number of moves per component during annealing. The total moves per temerature update will be this number times the number of components.

.. cpp:function:: void set_initial_temperature(double tmp)


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
