from . import _exception
from . import _check
import subprocess
import json

prog = "termux-brightness"

class Brightness:
    """Base class for controlling the brightness (termux-brightness)"""
    def __init__(self):
        pass

    def _run(self, command):
        """Function to run commands on Termux
        Args:
        command - the command you want to execute"""
        return subprocess.run(command, capture_output=True)

    def set(self, value=69):
        """Function to set value of brightness
        Args:
            value - integer, or str (auto)"""
        cmd = [prog, "auto" if isinstance(value, str) else str(value)]

        process = self._run(cmd)
        success = _check.check_success(process)

        try:
            err_msg = json.loads(process.stdout.strip())
            raise _exception.TermuxAPIError(err_msg["error"])
        except:
            pass
        return True if success[0] else success
