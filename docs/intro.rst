Introduction
============

Welcome to ``pytermux``, a simple Python module that ables to control your Android device with Termux:API

Notes
-----

This module expects you have **Termux** and **Termux:API** (including its apt package) installed on your Android phone

If not, you can install it `here <https://github.com/termux/termux-app>`__ and Termux:API `here <https://github.com/termux/termux-api>`__.

Another note here that this project is still in development, some examples here are not made yet, marked with ``(not implemented)``

If you want to help into the project, email me at `mrrare.dev@gmail.com <mailto: mrrare.dev@gmail.com>`__.

Functions/Methods
=================

Battery
-------

To get the battery information, you need to use ``pytermux.Battery()`` which is shown as example below

.. code-block:: python

    import pytermux
    battery = pytermux.Battery()
    info = battery.battery()

    percentage = info['percentage']

    print(f'Your device battery percentage is: {percentage}')
In this example, we used ``pytermux.Battery()`` instance for getting battery information, and used ``battery()`` to get the info, then we take the `percentage` value from `info` then printed it, this is mostly easy to use, but some outputs may depend on your device

Brightness
----------

Brightness setting is useful if you want to change your devices brightness based on your preferences, its also good when also used with ``Sensor()``, which you will see later on this guide

.. code-block:: python

    import pytermux
    bn = pytermux.Brightness()
    bn.set('auto')

Here, you set your brightness on ``bn.set()`` in ``Brightness()`` instance, the argument ``auto`` means the brightness will he automatic, this argument can be an integer, from 0 to 255, 0 being lowest and 255 being brightest possible you can set.


Camera
------

Some sample usage in ``pytermux`` are taking pictures with your phone camera

.. code-block:: python

    import pytermux
    cam = pytermux.Camera()
    cam.take('image.jpg', cam_type=0)

Here, it uses the ``Camera()`` instance for camera and `take()` function to actually take images with file ``image.jpg``, here, the ``cam_type`` argument is used if you want to use your phone's back or front camera, 0 for back, which is default, and 1 for front.

Permissions:

- ``android.permssion.CAMERA``

Clipboard
---------

You can also get, and set the data of your clipboard with the ``Clipboard()`` instance

.. code-block:: python

    import pytermux
    clipboard = pytermux.Clipboard()
    data = clipboard.get()
    new_data = "Hello World!"
    clipboard.set(new_data)

Here, you get the data by using ``get()`` method, and set it with new data with ``set()``

Unfortunately, ``get()`` doesn't work when you copy an image, i can't fix this because ``pytermux`` just executes system commands to the system

Dialog
------

not implemented yet

Fingerprint
-----------

not implemented yet

Media Player
------------

You can play any music file that is supported on your device

.. code-block:: python

   import pytermux
   import time
   mp = pytermux.MediaPlayer()
   mp.play('/sdcard/Musics/song.mp3')

   time.sleep(2)
   mp.pause()

   time.sleep(2)
   mp.play()

   time.sleep(10)
   if mp.isPlaying():
     mp.stop()

Here, it plays the song (defined by the path of the file) through the ``play()`` method, then after some time, it paused due to ``pause()`` method, then played it again, if ``isPlaying()`` is true, then it will stop playing it completely (not playable by ``play()``, unless you specified the path again.

Permissions:

- ``android.permission.READ_EXTERNAL_STORAGE``

Microphone Recorder
-------------------

You can also record using your device's built in microphone.

.. code-block:: python

   import pytermux
   mic = pytermux.MicRec()

   mic.record('audio.mp3', duration=60)

Here, you start recording by using the ``record()`` method, which has the file name and its duration (on seconds), you can manually stop it using the ``stop()`` method

Permissions:

- ``android.permission.READ_EXTERNAL_STORAGE``
- ``android.permission.MICROPHONE``

NFC
---

not implemented yet

Sensor
------

Yeah, you can also get sensor information, as long your devices supports one

.. code-block:: python

   import pytermux
   sensor = pytermux.Sensor()
   value = sensor.sensor('proximity')['PROXIMITY']['values'][0]
   if value == 5: # means its far
     print('far')
   elif value == 0:
     print('close')

Hard to explain, but here it gets the value of the ``Proximity`` sensor, btw, the values and names of the sensor are different for each devices, that above is an example, to list the sensors available, use the ``list()`` method

SMS
---

You can text any numbers in ``pytermux`` as well!

.. code-block:: python

   import pytermux
   sms = pytermux.SMS()
   number = 123456789
   sms.send(number, "Hello world!")

You use the ``send()`` method to send the message, along with the number (i.e. recipient) and the message, if your phone is multi-SIM, you can add the ``slot`` keyword argument at the ``send()`` method for it to send either SIM 1 or 2

Data charges may apply

Permissions:
- ``android.permission.SEND_SMS``
- ``android.permission.READ_SMS``
- ``android.permission.READ_CONTACTS``

Telephony
---------

You can call a number in Python with ease

.. code-block:: python

   import pytermux

   caller = pytermux.Telephony()

   caller.call('<number>')

Here, you use the ``call()`` with the number as an argument, when you execute this, Android will prompt for the SIM card you want to use, if you have multiple.

Permissions:

- ``android.permission.CALL_PHONE``

Toast
-----

not implemented yet

Torch (Flashlight)
------------------

You can open/close your device's flashlight by:

.. code-block:: python

   import pytermux
   import time
   torch = pytermux.Torch()

   torch.on()
   time.sleep(1)
   torch.off()

yeah, simple as that

Permissions:

- ``android.permission.CAMERA``

TTS (Text-to-speech)
--------------------

not implemented yet

Volume
------

You can set the audio volume using the` `Volume()`` instance

.. code-block:: python

   import pytermux
   vol = pytermux.Volume()
   vol.set('media', 5)

Using the ``set()`` method, with the audio stream name (use ``list_streams()`` for list of available streams)

Dont use negative numbers:)

Vibrate
-------

You can vibrate your phone as well:)

.. code-block:: python

   import pytermux
   vibrator = pytermux.Vibrate()
   vibrator.vibrate(300)

The ``300`` basically is the duration of  the vibration (per milisecond)

Wallpaper
---------

not implemented yet

WiFi
----

not implemented yet


Notes
=====

There you have it, if you have more questions you can create an issue on the `repo <https://github.com/MrRare2/pytermux/issues>`__

The developers, and ``pytermux`` **WILL NEVER** collect any personal info/data you use as arguments in ``pytermux``, you can look the source code yourself `here <https://github.com/MrRare2/pytermux>`__ so you dont have get worried using this.

Warning!!!
----------
Please do **NOT** use this on any unethical hacking activies. We are not responsible for any damages or cause you make on using this script.
