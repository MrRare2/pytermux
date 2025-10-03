Introduction
============

Welcome to ``pytermux``, a simple Python module that ables to control your Android device with Termux:API.

Notes
-----

This module expects you have **Termux** and **Termux:API** (including its apt package) installed on your Android phone

If not, you can download and install Termux `here <https://github.com/termux/termux-app>`__ and Termux:API `here <https://github.com/termux/termux-api>`__.

Another note here that this project is still in development, some examples here are not made yet, marked with ``(not implemented)``

If you want to help into the project, email me at `mrrare.dev@gmail.com <mailto: mrrare.dev@gmail.com>`__.

Functions/Methods
=================

Battery
-------

To get the battery information, you use the  ``battery()`` function which is shown as example below

.. code-block:: python

    import pytermux

    battery = pytermux.battery()
    percentage = battery['percentage']

    print(f'Your device battery percentage is: {percentage}%')

In this example, we used the ``battery()`` function to get the battery info, then we take the `percentage` value from `info` then printed it, this is mostly easy to use, but some outputs may depend on your device.

Brightness
----------

Brightness setting is useful if you want to change your device's brightness based on your use, its also good when also used with ``Sensor()``, which you will see later on this guide:

.. code-block:: python

    import pytermux
    bn = pytermux.set_brightness(-1)

Here, you set your brightness with ``pytermux.set_brightness(...)`` function, the argument ``-1`` means the brightness will he automatic, this argument can be an integer, from 0 to 255, 0 being lowest and 255 being brightest possible you can set.

Note that it might ask for the permission to **write on system settings** or this will not work. That is only asked once.

Camera
------

Some sample usage in ``pytermux`` are taking pictures with your phone camera

.. code-block:: python

    import pytermux
    pytermux.camera_take('image.jpg', 0)

Here, it uses the ``camera_take()`` function to actually take images and save it to ``image.jpg``, here, the ``0`` is used to specify the camera to use if you want to use your phone's back or front camera, 0 for back, which is default, and 1 for front.

Permissions:

- ``android.permssion.CAMERA``

Clipboard
---------

You can also get and set the data of your device's clipboard with ``pytermux``

.. code-block:: python

    import pytermux
    data = clipboard_get()
    print(f"Current clipboard data:", data)
    new_data = "Hello World!"
    pytermux.clipboard_set(new_data)

Here, you get the current clipboard by using ``clipboard_get()`` function, and set it with a new data with ``clipboard_set()``

Unfortunately, ``clipboard_get()`` doesn't return an image blob, nor ``clipboard_set()``, i can't fix this because ``pytermux`` just uses the Termux:API and it currently does not support image copying/getting.

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

Note: may drain your device battery if used for too long (especially to ``all()`` method)

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

You can make TTS speak with ``pytermux`` as well! yea

.. code-block:: python

   import pytermux
   tts = pytermux.TTS()
   tts.speak('hello')

This has lot of arguments, but you can see what are those using the built-in ``help()`` function, but here is a simple way to make TTS speak.

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

You can set your device's wallpaper with ``Wallpaper()``

.. code-block:: python

   import pytermux
   wp = pytermux.Wallpaper()
   wp.set('/sdcard/image.jpeg')


WiFi
----

As of December 2023, you can only scan (``WiFi.scan()``), check connection info (``WiFi.conninfo()``) and turn it on or off. As Termux:API dosen't support connecting to WiFi networks yet.

Permissions:

- ``android.permission.ACCESS_FINE_LOCATION``

Notes again
===========

There you have it, if you have more questions you can create an issue on the `repo <https://github.com/MrRare2/pytermux/issues>`__

The developers, and ``pytermux`` **WILL NEVER** collect any personal info/data you use as arguments in ``pytermux``, you can look the source code yourself `here <https://github.com/MrRare2/pytermux>`__ so you dont have get worried using this.

Warning!!!
----------
Please do **NOT** use this on any unethical hacking activies. We are not responsible for any damages or cause you make on using this script.


