from . import _exception
from . import _check
import subprocess
import json

prog = "termux-wallpaper"

class Wallpaper:
    """Base class for setting wallpapers (termux-wallpape4)"""
    def __init__(self):
        pass

    def _run(self, command):
        """Function to run commands on Termux
        Args:
        command - the command you want to execute"""
        return subprocess.run(command, capture_output=True)

    def set(self, img_path, lockscreen=False):
        """Function to set device wallpaper

        Args:
            img_path - the image to set
            lockscren (default False) - enable if you want to set to lockscreen"""
        cmd = [prog, "-f", img_path]
        if lockscreen:
            cmd.append('-l')

        process = self._run(cmd)
        success = _check.check_success(process)

        try:
            err_msg = json.loads(process.stdout.strip())
            raise _exception.TermuxAPIError(err_msg["error"]) from None
        except Exception as e:
            if type(e) == _exception.TermuxAPIError:
                raise
        return True if success[0] else success
