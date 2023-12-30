from . import _exception
from . import _check
import subprocess
import json

prog_list = "termux-sms-list"
prog_send = "termux-sms-send"

class SMS:
    """Base class for SMS messages (termux-sms)"""
    def __init__(self):
        pass

    def _run(self, command):
        """Function to run commands on Termux
        Args:
        command - the command you want to execute"""
        return subprocess.run(command, capture_output=True)

    def list(self):
        """Function to list messages"""
        cmd = [prog_list]

        process = self._run(cmd)
        success = _check.check_success(process)

        try:
            err_msg = json.loads(process.stdout.strip())
            raise _exception.TermuxAPIError(err_msg["error"]) from None
        except Exception as e:
            if type(e) == _exception.TermuxAPIError:
                raise
        data = json.loads(process.stdout.strip())
        return data

    def send(self, numbers, message, slot=1):
        """Function to send text messages
        Args:
          numbers - recipient
          message - the actual message
          slot (1,2) - the sim card slot you want to use

        Data usages may apply
        """
        slot_opt = "-s "
        slot_ = slot_opt + str(slot)
        use_slot_arg = True
        if slot not in (1, 2) or not isinstance(slot, int): # this prevents silent errors (as described by termux-api itself)
            raise ValueError('invalid SIM card slot')
        if slot_ == "-s 1": # for single sim users, just remove it entirely
            use_slot_arg = False
        cmd = [prog_send, "-n", str(numbers)]
        cmd.append(slot_) if use_slot_arg else None
        cmd.append(message)

        process = self._run(cmd)
        success = _check.check_success(process)
        try:
            err_msg = json.loads(process.stdout.strip())
            raise _exception.TermuxAPIError(err_msg["error"]) from None
        except Exception as e:
            if type(e) == _exception.TermuxAPIError:
                raise
        return True if success[0] else success
