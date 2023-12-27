from . import _exception
import subprocess

def check_success(raw):
    """Check process status"""
    if raw.returncode != 0:
        return [False, raw.returncode]
    else:
        return [True, 0]

def install():
    cmd = ["apt","install","termux-api"]
    proc = subprocess.run(cmd)

def check_api():
    """Function to check if Termux:API is installed"""
    cmd = subprocess.run(['apt', 'list', 'termux-api'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if b'[installed]' in cmd.stdout:
        return True
    else:
        return False
