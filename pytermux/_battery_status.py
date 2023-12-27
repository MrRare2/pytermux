from . import _exception
from . import _check
import subprocess
import json

prog = "termux-battery-status"

class Battery:
    """Base class for getting battery information (termux-battery-status)"""

    def __init__(self):
        pass

    def _jsonize(self, data):
        """Function to jsonize (convert a JSON compatible text into Python usable object) texts
        Args:
            text - the text you want to convert"""
        return json.loads(data)

    def _run(self, command):
        """Function to run commands on Termux
        Args:
        command - the command you want to execute
        """
        return subprocess.run(command, capture_output=True, text=True)

    def battery(self):
        """Get battery info"""
        cmd = [prog]
        process = self._run(cmd)
        success = _check.check_success(process)

        if success[0]:
            data = process.stdout.strip()
        else:
            raise _exception.NonZero(f"The command {cmd} returned a {success[1]} status") from None
        return self._jsonize(data)

