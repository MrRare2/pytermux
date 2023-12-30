from . import _exception
from . import _check
import subprocess
import json

prog_toggle = "termux-wifi-enable"
prog_scan = "termux-wifi-scaninfo"
prog_conninfo = "termux-wifi-connectioninfo"

class WiFi:
    """Base class for monitoring WiFi connections (termux-wifi)"""
    def __init__(self):
        pass

    def _run(self, command):
        """Function to run commands on Termux
        Args:
        command - the command you want to execute"""
        return subprocess.run(command, capture_output=True)

    def on(self):
        """Function to open WiFi"""
        cmd = [prog_toggle, "true"]

        process = self._run(cmd)
        success = _check.check_success(process)

        try:
            err_msg = json.loads(process.stdout.strip())
            raise _exception.TermuxAPIError(err_msg["error"]) from None
        except Exception as e:
            if type(e) == _exception.TermuxAPIError:
                raise
        return True if success[0] else success

    def off(self):
        """Function to close WiFi"""
        cmd = [prog_toggle, "false"]

        process = self._run(cmd)
        success = _check.check_success(process)
        try:
            err_msg = json.loads(process.stdout.strip())
            raise _exception.TermuxAPIError(err_msg["error"]) from None
        except Exception as e:
            if type(e) == _exception.TermuxAPIError:
                raise
        return True if success[0] else success

    def conninfo(self):
        """Function to get the connection info"""
        cmd = [prog_conninfo]

        process = self._run(cmd)
        success = _check.check_success(process)

        try:
            err_msg = json.loads(process.stdout.strip())
            raise _exception.TermuxAPIError(err_msg["error"]) from None
        except Exception as e:
            if type(e) == _exception.TermuxAPIError:
                raise
        return json.loads(process.stdout.strip())

    def scan(self):
        """Function to scan WiFi networks"""
        cmd = [prog_scan]

        process = self._run(cmd)
        success = _check.check_success(process)

        try:
            err_msg = json.loads(process.stdout.strip())
            m = err_msg.get('error') or err_msg.get("API_ERROR")
            raise _exception.TermuxAPIError(m) from None
        except Exception as e:
            if type(e) == _exception.TermuxAPIError:
                raise
        return json.loads(process.stdout.strip())

    def connect(self):
        # NOTE: Termux:API dosen't have WiFi connectivity yet
        raise NotImplementedError("Termux:API dosen't support this feature yet")

    def disconnect(self):
        # NOTE: Termux:API dosen't have WiFi connectivity yet
        raise NotImplementedError("Termux:API dosen't support this feature yet")
