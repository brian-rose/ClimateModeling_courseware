================
Climate Modeling Courseware
================
----------
 A collection of interactive lecture notes and assignments for a graduate level climate modeling course
----------

|binder|

Quickstart
--------------
Just click on the Binder badge above to run these notebooks interactively in the cloud!

Or clone the repo and run on your own machine (details below).

Author
--------------
| **Brian E. J. Rose**
| Department of Atmospheric and Environmental Sciences
| University at Albany
| brose@albany.edu


About
--------------
ATM 623 Climate Modeling
is an advanced graduate course on climate dynamics and climate modeling. The focus of the course is on the hands-on use of both simple and complex climate models to build understanding of the processes that control the planetary energy budget.

The course makes extensive use of Python code and the Jupyter notebook for reproducible, self-describing calculations and figures. This repository contains a collection of linked Jupyter notebooks with lecture notes, examples and assignments. All notebooks are self-describing.

Requirements
---------------
You will need a scientific Python distribution. Anaconda Python is strongly recommended and will get you everything you need all at once.

The complete list of packages used in these notes includes:

- Python (compatible with both Python 2 and 3)
- numpy
- scipy
- matplotlib
- sympy
- xarray
- climlab (climate modeling engine)
- ffmpeg (video conversion tool used under-the-hood for interactive animations)
- version_information (display information about package versions)

which are all available through ``conda`` on the ``conda-forge`` channel.

These notes rely heavily on the custom climlab_ package (a computational engine for process-oriented climate modeling). See the documentation_ or the `github page`_ for installation instructions.

The following commands will create a self-contained conda environment with everything you need to run these notebooks (Mac, Linux and Windows).
From within the ``ClimateModeling_courseware`` directory, do this::

    conda env create --name atm623 --file environment.yml

Usage
------------------
From the main courseware directory, just enter

``jupyter notebook``

or

``jupyter notebook index.ipynb``

from your favorite terminal.

License
---------------
The notes and code are freely available under the MIT license.
See the accompanying LICENSE file.
Comments by email are always appreciated.

.. _climlab: https://github.com/brian-rose/climlab
.. _documentation: http://climlab.readthedocs.io
.. _`github page`: https://github.com/brian-rose/climlab

.. |binder| image:: https://mybinder.org/badge.svg
  :target: https://mybinder.org/v2/gh/brian-rose/ClimateModeling_courseware/master
