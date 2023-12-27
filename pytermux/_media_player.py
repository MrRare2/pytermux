from . import _exception
from . import _check
import subprocess
import json

prog = "termux-media-play"
play = "play"
info = "info"
pause = "pause"
stop = "stop"

class MediaPlayer:
    """Base class for playing media (termux-media-play)"""
    def __init__(self):
        pass

    def _run(self, command):
        """Function to run commands on Termux
        Args:
        command - the command you want to execute"""
        return subprocess.run(command, capture_output=True)

    def play(self, file=''):
        """Function to play the {file}, if no arguments, tries to resume the paused file"""
        cmd = [prog, play, file]

        process = self._run(cmd)
        success = _check.check_success(process)

        try:
            err_msg = json.loads(process.stdout.strip())
            raise _exception.TermuxAPIError(err_msg["error"]) from None
        except Exception as e:
            if type(e) == _exception.TermuxAPIError:
                raise
        return True if success[0] else success

    def pause(self):
        """Function to pause the currently playing media"""
        cmd = [prog, pause]

        process = self._run(cmd)
        success = _check.check_success(process)
        try:
            err_msg = json.loads(process.stdout.strip())
            raise _exception.TermuxAPIError(err_msg["error"]) from None
        except:
            if type(e) == _exception.TermuxAPIError:
                raise
        return True if success[0] else success

    def info(self):
        """Get the information of the currently playing media"""
        cmd = [prog, info]

        process = self._run(cmd)
        success = _check.check_success(process) # if ur here dont remove this, this might be useful for debugging, i guess?
        try:
            err_msg = json.loads(process.stdout.strip())
            raise _exception.TermuxAPIError(err_msg["error"])
        except Exception as e:
            if type(e) == _exception.TermuxAPIError:
                raise
        return process.stdout

    def stop(self):
        """Stop the currently playing media to be played/paused"""
        cmd = [prog, stop]

        process = self._run(cmd)
        success = _check.check_success(process)
        try:
            err_msg = json.loads(process.stdout.strip())
            raise _exception.TermuxAPIError(err_msg["error"])
        except Exception as e:
            if type(e) == _exception.TermuxAPIError:
                raise

        return True if success[0] else False
