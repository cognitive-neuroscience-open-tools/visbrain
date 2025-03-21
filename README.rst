This is the fork of a fork of Visbrain. 

The first focus lies on visbrain.sleep. The original sleep moducal was design for AASM style sleep scoring. The first fork adapted this module for animal research. This for should adapt Sleep for SOP sleep scoring in humans, while benefitting of the continued improvements of the first fork.

The first fork added in particular, added the following features:

* Dissociation of 'display window' and 'scoring window', allowing one to score in short epochs while still visualizing data around the scoring window, as in standard in animal scoring. In "locked" mode, the scoring and display window are identical (as is standard for human scoring)

* Flexible definition of vigilance states (name, value in old-style hypnograms, color and order in the GUI) from a YAML file.  Use by specifying the `state_config_path` kwarg to the `Sleep` object.  Refer to the documentation for an exemple. The default configuration contains the following states: ['Art', 'Wake', 'REM', 'N1', 'N2', 'N3'] and their associated values: [-1, 0, 4, 1, 2, 3]

* Integration of a video player synchronized with data. Use with by specifying the `video_file` and `video_offset` kwargs to the `Sleep` object. Supported formats are the same as Qt's QMediaPlayer class.

* Adding a hypnogram color overlay onto signal data. This slows up state assignment quite a bit but can be deactivated in the menu.

* Adding a "click-and-drag" window to select arbitrary epochs for subsequent scoring.  Life hack: if there is a rather long continuous epoch to score: click on signal to create the "click-and-drag" window, use "N" (while holding the mouse) to go to next window until you reach the end of the epoch, "close" the window where appropriate and score the whole thing at once. This will speed up dramatically scoring and hopefully make you happy.

Hopefully all this stuff will be merged to the main repo eventually. *At this point it seems unlikely, that the original Visbrain project will be continued to be maintained*

Unfortunately this all comes with no guarantee regarding maintenance and system
compatibility but feel free to contribute.

Cheers,
Erik


========
Visbrain
========

.. image:: https://travis-ci.org/EtienneCmb/visbrain.svg?branch=master
    :target: https://travis-ci.org/EtienneCmb/visbrain

.. image:: https://ci.appveyor.com/api/projects/status/fdxhhmpagms1so8l/branch/master?svg=true
    :target: https://ci.appveyor.com/project/EtienneCmb/visbrain/branch/master

.. image:: https://circleci.com/gh/EtienneCmb/visbrain/tree/master.svg?style=svg
    :target: https://circleci.com/gh/EtienneCmb/visbrain/tree/master

.. image:: https://codecov.io/gh/EtienneCmb/visbrain/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/EtienneCmb/visbrain

.. image:: https://badge.fury.io/py/visbrain.svg
    :target: https://badge.fury.io/py/visbrain

.. image:: https://pepy.tech/badge/visbrain
    :target: https://pepy.tech/project/visbrain

.. image:: https://badges.gitter.im/visbrain-python/chatroom.svg
    :target: https://gitter.im/visbrain-python/chatroom?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge

.. figure::  https://github.com/EtienneCmb/visbrain/blob/master/docs/_static/ico/visbrain.png
    :align:  center

**Visbrain** is an open-source python 3 package dedicated to brain signals visualization. It is based on top of `VisPy <http://vispy.org/>`_ and PyQt and is distributed under the 3-Clause BSD license. We also provide an on line `documentation <http://visbrain.org>`_, `examples and datasets <http://visbrain.org/auto_examples/>`_ and can also be downloaded from `PyPi <https://pypi.python.org/pypi/visbrain/>`_.

Important links
---------------

* Official source code repository : https://github.com/EtienneCmb/visbrain
* Online documentation : http://visbrain.org
* Visbrain `chat room <https://gitter.im/visbrain-python/chatroom?utm_source=share-link&utm_medium=link&utm_campaign=share-link>`_


Installation
------------

Dependencies
++++++++++++

Visbrain requires :

* NumPy >= 1.13
* SciPy
* VisPy >= 0.5.3
* Matplotlib >= 1.5.5
* PyQt5
* Pillow
* PyOpenGL

MNE-Python is recommended.

User installation
+++++++++++++++++

Install Visbrain :
Get the dependencies

.. code-block:: console

    pip install -r requeriments.txt

Clone the repo and install visbrain from the folder

.. code-block:: console

    pip install -U .

