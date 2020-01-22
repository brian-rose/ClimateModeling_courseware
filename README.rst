================
Climate Modeling Courseware
================
----------
 A collection of interactive lecture notes and assignments for a graduate level climate modeling course
----------

|binder|


**PLEASE NOTE this repository is now deprecated!**

As of *January 2020*, I'm distributing my notes in a more "book-like" form known as
`The Climate Laboratory`_ (powered by `JupyterBook`_). The source can be found in
`this github repository`_.

You're more likely to find up-to-date content over there.

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
You will need a scientific Python distribution. Anaconda Python is strongly recommended.

The complete list of packages used in these notes includes:

- python      (versions 2.7, 3.6, 3.7 should all work)
- numpy       (base numerics)
- scipy       (general math/sci utilities)
- matplotlib  (graphics)
- xarray      (labeled data structures)
- metpy       (meteorological utilities)
- cartopy     (mapping)
- sympy       (symbolic math)
- climlab     (climate modeling engine)
- ffmpeg      (video conversion tool used under-the-hood for interactive animations)
- version_information  (display information about package versions)
- rise        (render slides as live slide shows)

which are all available through ``conda`` on the ``conda-forge`` channel (see below).

These notes rely heavily on the custom climlab_ package
(a computational engine for process-oriented climate modeling).
See the documentation_ or the `github page`_ for installation instructions.

Usage
------

The following commands will create a self-contained conda environment
with everything you need to run these notebooks (Mac, Linux and Windows).
From within the ``ClimateModeling_courseware`` directory
in your favorite terminal, do this::

    conda env create --file environment.yml
    conda activate climlab-courseware
    jupyter notebook


License
---------------
The notes and code are freely available under the MIT license.
See the accompanying LICENSE file.

Comments are always appreciated! Please `open an issue on github`_
(preferred because it keeps the discussion open) or send me an email.

.. _climlab: https://github.com/brian-rose/climlab
.. _documentation: http://climlab.readthedocs.io
.. _`github page`: https://github.com/brian-rose/climlab
.. _`open an issue on github`: https://github.com/brian-rose/ClimateModeling_courseware/issues
.. _`The Climate Laboratory`: https://brian-rose.github.io/ClimateLaboratoryBook
.. _`this github repository`: https://github.com/brian-rose/ClimateLaboratoryBook
.. _`JupyterBook`: https://jupyterbook.org

.. |binder| image:: https://mybinder.org/badge.svg
  :target: https://mybinder.org/v2/gh/brian-rose/ClimateModeling_courseware/master
