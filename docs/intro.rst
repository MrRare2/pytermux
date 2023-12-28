Introduction
============

Welcome to ``pytermux``, a simple Python module that ables to control your Android device with Termux:API

Notes
-----

This module expects you have **Termux** and **Termux:API** (including its apt package) installed on your Android phone

If not, you can install it `here <https://github.com/termux/termux-app>`__ and Termux:API `here <https://github.com/termux/termux-api>`__.

Another note here that this project is still in development, some examples here are not made yet, marked with ``(not implemented)``

If you want to help into the project, email me at `mrrare.dev@gmail.com <mailto: mrrare.dev@gmail.com>`__.

Basics
------

``Battery``

To get the battery information, you need to use ``pytermux.Battery()`` which is shown as example below

.. code-block:: python

    import pytermux
    battery = pytermux.Battery()
    info = battery.battery()

    percentage = info['percentage']

    print(f'Your device battery percentage is: {percentage}")
In this example, we used ``pytermux.Battery()`` instance for getting battery information, and used ``battery()`` to get the info, then we take the `percentage` value from `info` then printed it, this is mostly easy to use, but some outputs may depend on your device

``Brightness``

Brightness setting is useful if you want to change your devices brightness based on your preferences, its also good when also used with ``Sensor()``, which you will see later on this guide

.. code-block:: python

    import pytermux
    bn = pytermux.Brightness()
    bn.set('auto')

Here, you set your brightness on ``bn.set()`` in ``Brightness()`` instance, the argument ``auto`` means the brightness will he automatic, this argument can be an integer, from 0 to 255, 0 being lowest and 255 being brightest possible you can set.


``Camera``

Some sample usage in ``pytermux`` are taking pictures with your phone camera

.. code-block:: python

    import pytermux
    cam = pytermux.Camera()
    cam.take('image.jpg', cam_type=0)

Here, it uses the ``Camera()`` instance for camera and `take()` function to actually take images with file ``image.jpg``, here, the ``cam_type`` argument is used if you want to use your phone's back or front camera, 0 for back, which is default, and 1 for front.

To use this command, you need to grant it the camera permission, i.e. ``android.permssion.CAMERA``

``Clipboard``
