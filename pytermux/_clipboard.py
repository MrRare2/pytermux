from . import _exception
from . import _check
import subprocess

prog_get = "termux-clipboard-get"
prog_set = "termux-clipboard-set"

class Clipboard:
    """Base class for getting/setting the clipboard"""

    def __init__(self):
        pass

    def _run(self, command):
        """Function to run commands on Termux
        Args:
        command - the command you want to execute
        """
        return subprocess.run(command, capture_output=True, text=True)

    def get(self):
        """Get the contents of the clipboard
        Returns None if the contents are empty or there's an error"""
        cmd = [prog_get]
        process = self._run(cmd)

        success = _check.check_success(process)

        if success[0]:
            return process.stdout.strip()
        else:
            return

    def set(self, data):
        """Set clipboard data
        Args:
        data - the data you want ro set to clipboard"""
        cmd = [prog_set, data]

        process = self._run(cmd)

        success = _check.check_success(process)

        return True if success[0] else False
