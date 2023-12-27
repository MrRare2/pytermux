from . import _exception
from . import _check
import subprocess
import json

prog = "termux-vibrate"

class Vibrate:
    """Base class for vibrating (termux-vibrate)"""
    def __init__(self):
        pass

    def _run(self, command):
        """Function to run commands on Termux
        Args:
        command - the command you want to execute"""
        return subprocess.run(command, capture_output=True)

    def vibrate(self, duration=1000, force_on_silent=False):
        """Function to vibrate phone
        Args:
            duration - duration of the vibrate, default is 1000ms , which is equivalent to 1 second
            force_on_silent (bool) - Force vibrate even in silent mode, default is False"""
        cmd = [prog, "-d", str(duration)]
        if force_on_silent:
            cmd.append("-f")


        process = self._run(cmd)
        success = _check.check_success(process)

        try:
            err_msg = json.loads(process.stdout.strip())
            raise _exception.TermuxAPIError(err_msg["error"])
        except:
            if type(e) == _exception.TermuxAPIError:
                raise
        return True if success[0] else success
