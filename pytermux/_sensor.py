from . import _exception
from . import _check
import subprocess
import json

# templates
prog = "termux-sensor"
args = ["-a", "-c", "-l", "-s"] # no -n since we dont want it to continuously update, and no -d since its useless because theres no -n anyway

class Sensor:
    """Base class for monitoring sensors (termux-sensor)
    """
    def __init__(self):
        pass

    def _run(self, command):
        """Function to run commands on Termux
        Args:
        command - the command you want to execute
        """
        return subprocess.run(command, capture_output=True, text=True)

    def _jsonize(self, text):
        """Function to jsonize (convert a JSON compatible text into Python usable object) texts
        Args:
        text - the text you want to convert"""
        return json.loads(text)

    def all(self):
        """Listen to all sensors (WARNING! may have battery impact when used in a while loop)
        Equivalent to:
        `termux-sensor -a -n 1`"""
        cmd = [prog, args[0], "-n", "1"]

        process = self._run(cmd)

        success = _check.check_success(process)

        if success[0]:
            data = process.stdout.strip()
        else:
            raise _exception.NonZero(f"The command {cmd} returned a {success[1]} status")

        return self._jsonize(data)

    def cleanup(self):
        """Perform cleanup (release sensor resources)"""
        cmd = [prog, args[1]]
        process = self._run(cmd)

        success = _check.check_success(process)

        if success[0]:
            print("Cleanup success!")
        else:
            print("No cleanup necessary")
    def list(self):
        """Show list of available sensors"""
        cmd = [prog, args[2]]
        process = self._run(cmd)

        success = _check.check_success(process)

        if success[0]:
            data = process.stdout.strip()
        else:
            raise _exception.NonZero(f"The command {cmd} returned a {success[1]} status")

        return self._jsonize(data)

    def sensor(self, sensor_type):
        """Sensors to listen to (can contain just partial name)
        Args:
        sensor_type - the sensor you want to use, can be multiple by using a comma, can contain just partial names)"""

        cmd = [prog, args[3], sensor_type, "-n", "1"]

        process = self._run(cmd)

        success = _check.check_success(process)

        if success[0]:
            data = process.stdout.strip()
        else:
            raise _exception.NonZero(f"The command {cmd} returned a {success[1]} status")

        return self._jsonize(data)
