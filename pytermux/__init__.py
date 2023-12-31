"""pytermux - A package that interacts with termux-api using Python

"""

#
from . import _exception
from . import _check
# 
from ._battery_status import Battery
from ._camera import Camera
from ._torch import Torch
from ._fingerprint import Fingerprint
from ._sensor import Sensor
from ._wifi import WiFi
from ._clipboard import Clipboard
from ._notif import Notification
from ._vibrate import Vibrate
from ._wallpaper import Wallpaper
from ._sms import SMS
from ._telephony import Telephony
from ._brightness import Brightness
from ._media_player import MediaPlayer
from ._mic_record import MicRec
from ._volume import Volume
from ._tts import TTS
VERSION = "1.1.3"

has_termux_api = _check.check_api()

if not has_termux_api:
    raise _exception.TermuxAPINotInstalled("Please install Termux:API and it's package `termux-api` to work")

del has_termux_api
