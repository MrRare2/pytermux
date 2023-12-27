from . import _exception
from . import _check
import subprocess
import json

prog = "termux-camera-photo"

class Camera:
    """Base class for taking images (termux-camera-photo)"""
    def __init__(self):
        pass

    def _run(self, command):
        """Function to run commands on Termux
        Args:
        command - the command you want to execute"""
        return subprocess.run(command, capture_output=True, text=True)

    def take(self, file, cam_type=0):
        """Function to take photos
        Args:
        file - file to save the image
        cam_type - camera to use to take, 0 for back (default) and 1 for front"""
        if not isinstance(cam_type, int):
            raise ValueError("Not an integer")
        cmd = [prog, "-c", str(cam_type), file]

        process = self._run(cmd)

        success = _check.check_success(process)
        try:
            err_msg = json.loads(process.stdout.strip())
            raise _exception.TermuxAPIError(err_msg["error"]) from None
        except Exception as e:
            if type(e) == _exception.TermuxAPIError:
                raise
        return True if success[0] else False

