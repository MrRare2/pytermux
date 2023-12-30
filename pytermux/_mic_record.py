from . import _exception
from . import _check
import subprocess
import json
import os

prog = "termux-microphone-record"

class MicRec:
    """Base class for voice recording (termux-microphone-recoerd)"""
    def __init__(self):
        pass

    def _run(self, command):
        """Function to run commands on Termux
        Args:
        command - the command you want to execute"""
        return subprocess.run(command, capture_output=True)

    def record(self, file, duration=60):
        """Function to record using your device's microphone
        Args:
            file - file you want the recording will be saved
            duration - the duration of the record, default is 60"""
        # UPDATE: i fixed it, we will use MPEG-4 (aac), which is m4a
        fn, ex = os.path.splitext(file)
        if not ex:
            ex = ".m4a"
        file = fn + ex
        cmd = [prog, "-e", "aac", "-f", file, "-l", str(duration)]

        process = self._run(cmd)
        success = _check.check_success(process)

        try:
            err_msg = json.loads(process.stdout.strip())
            raise _exception.TermuxAPIError(err_msg["error"]) from None
        except Exception as e:
            if type(e) == _exception.TermuxAPIError:
                raise
        return True if success[0] else success

    def info(self):
        """Get info of the currently recording file"""
        cmd = [prog, "-i"]

        process = self._run(cmd)
        success = _check.check_success(process)
        try:
            err_msg = json.loads(process.stdout.strip())
            raise _exception.TermuxAPIError(err_msg["error"]) from None
        except Exception as e:
            if type(e) == _exception.TermuxAPIError:
                raise
        data = json.loads(process.stdout.strip())

        if data['isRecording']:
            return data['outputFile']
        else:
            return False

    def stop(self):
        """Stop the recording"""
        cmd = [prog, "-q"]

        process = self._run(cmd)
        success = _check.check_success(process)

        try:
            err_msg = json.loads(process.stdout.strip())
            raise _exception.TermuxAPIError(err_msg["error"]) from None
        except Exception as e:
            if type(e) == _exception.TermuxAPIError:
                raise

        return True if success[0] else False
    # fun fact, i just realize you can just do return success[0] but im tired of fixing is myself:)
