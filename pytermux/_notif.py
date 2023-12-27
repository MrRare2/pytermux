from . import _exception
from . import _check
import subprocess
import json

prog = "termux-notification"
prog_list = "termux-notification-list"
prog_remove = "termux-notifcation-remove"

class Notification:
    """Base class for monitoring notifications (termux-notifcation)"""
    def __init__(self):
        pass

    def _run(self, command):
        """Function to run commands on Termux
        Args:
        command - the command you want to execute"""
        return subprocess.run(command, capture_output=True)

    def notify(self, **kwargs):
        # TODO: this
        """Function to send notifications"""
        #cmd = [prog]

        #process = self._run(cmd)
        #success = _check.check_success(process)

        #try:
            #err_msg = json.loads(process.stdout.strip())
            #return err_msg["error"]
        #except:
            #pass
        #return True if success[0] else success
        return None

    def list(self):
        """Function to get list of currently active notifications"""
        cmd = [prog_list]

        process = self._run(cmd)
        success = _check.check_success(process)
        try:
            err_msg = json.loads(process.stdout.strip())
            return err_msg["error"]
        except:
            raise _exception.TermuxAPIError(err_msg["error"]) from None
        return json.loads(data.stdout.strip())

    def remove(self, id):
        """Function to remove a notification (mostly dosent work on system notifications)"""
        cmd = [prog_remove, str(id)]
        process = self._run(cmd)
        success = _check.check_success(process)
        try:
            err_msg = json.loads(process.stdout.strip())
            return err_msg["error"]
        except:
            raise _exception.TermuxAPIError(err_msg["error"]) from None
        return True if success[0] else False
