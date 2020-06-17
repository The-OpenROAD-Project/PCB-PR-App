Quick Start
===========

This is the quick start guide for Ubuntu 18.04. 
Ubuntu 20.04 is likely the same, but has not been tested.
Ubuntu 16.04 is not compatible because it is difficult to get the latest version of Python 3.

Installation
^^^^^^^^^^^^

Clone the repo recursively.

``git clone --recurse-submodules https://github.com/The-OpenROAD-Project/PCB-PR-App.git``

``cd`` into the repo.

``cd PCB-PR-App``

Install basic dependencies as root.

``sudo ./basic_dependencies.sh``

Build the tools.

``./ubuntu_install.sh``


Test Installation
^^^^^^^^^^^^^^^^^

Run the regression tests.

``./tests/regression-py.sh``

The output should end with the string ``Success``.


Run the Tools
^^^^^^^^^^^^^

Things to note when running the tools:

1. You must have a board outline in the ``Edge.Cuts`` layer.

#. You must have component outlines in the ``CrtYd.F`` layer at minimum. For through-hole components you also need a ``CrtYd.B`` outline.

#. The default values in ``run_layout.py`` give a quick result for testing. Most designs need many more iterations to achieve anything like an acceptable result.

#. For large designs (hundreds of components) expect run times greater than 10 hours. BeagleBone Black has over 400 components and takes around 12 hours to get a DRV-free result.

#. Placement is harder than routing. The router is generally very good if the placement is workable. For best results, run several layout jobs in parallel, with different placement parameters for tuning.

#. DRC is experimental. The KiCad DRC is more mature.


To run a layout use the Python script ``run_layout.py``.

``python3 run_layout.py <your kicad_pcb file>``

The result will be in a file with the same filename prefixed with ``output.``.

Playing with ``run_layout.py``'s options can yield significantly better results.

See the options with ``run_layout.py --help``.


Make Your Own Tools
^^^^^^^^^^^^^^^^^^^

The API calls in this documentation work in Python.

Examine ``run_layout.py`` as an example of how to call the placer, router, and so on, in Python.

Each sub-module repository (the placer, router, and database) can be used as an example for how to integrate a new C++ tool. 
Generally you can copy the CMake files. Just make sure to update the ``.i`` files for the function calls you want to use in Python.

