from . import _exception
from . import _check
import subprocess
import json

prog = "termux-telephony-call"

class Telephony:
    """Base class for calling phone numbers (termux-telephony-call)"""
    def __init__(self):
        pass

    def _run(self, command):
        """Function to run commands on Termux
        Args:
        command - the command you want to execute"""
        return subprocess.run(command, capture_output=True)

    def call(self, number):
        """Function to open flashlight"""
        cmd = [prog, str(number)]

        process = self._run(cmd)
        success = _check.check_success(process)

        try:
            err_msg = json.loads(process.stdout.strip())
            raise _exception.TermuxAPIError(err_msg["error"]) from None
        except Exception as e:
            if type(e) == _exception.TermuxAPIError:
                raise
        return True if success[0] else success

