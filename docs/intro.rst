Introduction
============

Welcome to ``pytermux``, a simple Python module that ables to control your Android device with Termux:API

Notes
-----

This module expects you have **Termux** and **Termux:API** (including its apt package) installed on your Android phone

If not, you can install it `here <https://github.com/termux/termux-app>`__ and Termux:API `here <https://github.com/termux/termux-api>`__.

Basics
------

Some sample usages are taking pictures with your phone camera

.. code-block:: python

    import pytermux
    cam = pytermux.Camera()
    cam.take('image.jpg', cam_type=0)

Here, it uses the `Camera()` instance for camera and `take()` function to actually take images with file `image.jpg`, here, the `cam_type` argument is used if you want to use your phone's back or front camera, 0 for back, which is default, and 1 for front.
