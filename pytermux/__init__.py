"""pytermux - A package that interacts with termux-api using Python

"""

#
from . import _check
# 
from ._audio_info import audio_info
from ._battery_status import battery
from ._brightness import set_brightness
from ._camera import camera_info, camera_take, torch_set
from ._clipboard import clipboard_get, clipboard_set
from ._contacts import get_contacts
from ._dialog import dialog_checkbox, dialog_confirm, dialog_counter, dialog_date, dialog_radio, dialog_speech, dialog_spinner, dialog_text, dialog_time
from ._download import download
from ._fingerprint import fingerprint
from ._ir import infrared_frequencies, infrared_transmit
from ._sensor import Sensor
from ._wifi import WiFi
from ._notif import Notification
from ._vibrate import Vibrate
from ._wallpaper import Wallpaper
from ._sms import SMS
from ._telephony import call, call_logs, cell_info
from ._media_player import MediaPlayer
from ._mic_record import MicRec
from ._volume import Volume
from ._tts import TTS
VERSION = "1.1.3.2"

has_termux_api = _check.check_api()

if not has_termux_api:
    raise _exception.TermuxAPINotInstalled("Please install Termux:API and it's package `termux-api` to work")

del has_termux_api
