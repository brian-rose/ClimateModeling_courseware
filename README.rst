================
Climate Modeling Courseware
================
----------
 A collection of interactive lecture notes and assignments for a graduate level climate modeling course
----------

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
You will need a scientific Python distribution. Anaconda Python is strongly recommended and will get you almost everything you need all at once.

The complete list of packages used in these notes includes:

- numpy
- scipy
- matplotlib
- IPython
- netCDF4
- sympy

which are all available through ``conda``.

Additionally these notes rely heavily on the custom climlab_ package (a computational engine for process-oriented climate modeling). See the documentation_ or the `github page`_ for installation instructions.

Optional:

- The ``version_information`` extension (to display details about package versions used in each notebook). Install via ``pip install version_information``


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
