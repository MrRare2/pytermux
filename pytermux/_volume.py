from . import _exception
from . import _check
import subprocess
import json

prog = "termux-volume"

class Volume:
    """Base class for controlling volume (termux-volume)"""
    def __init__(self):
        self._streams = [entry['stream'] for entry in self.list_streams()]

    def _run(self, command):
        """Function to run commands on Termux
        Args:
        command - the command you want to execute"""
        return subprocess.run(command, capture_output=True)

    def list_streams(self):
        """Function to list streams"""
        cmd = [prog]

        process = self._run(cmd)
        success = _check.check_success(process)

        try:
            err_msg = json.loads(process.stdout.strip())
            raise _exception.TermuxAPIError(err_msg["error"]) from None
        except Exception as e:
            if type(e) == _exception.TermuxAPIError:
                raise
        return json.loads(process.stdout.strip())

    def set(self, stream, volume):
        """Function to set the volume of the audio stream

        Args:
            stream - the stream you want to use, to list the available streams for your device, use `Volume.list_streams()` method
            volume (x>0) = The volume you want to set it"""

        if volume <= 0: # you cant have negative volume lol ur going to the fifth dimension?
            volume = 0
        cmd = [prog, stream, str(volume)]

        process = self._run(cmd)
        success = _check.check_success(process)
        try:
            err_msg = json.loads(process.stdout.strip())
            raise _exception.TermuxAPIError(err_msg["error"]) from None
        except Exception as e:
            if type(e) == _exception.TermuxAPIError:
                raise
        return True if success[0] else success
