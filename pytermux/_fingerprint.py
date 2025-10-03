from ._commands import Commands
from ._comm import communicate

import json

def fingerprint() -> None:
    """Authenticate with device's fingerprint"""
    out, err = communicate(Commands.fingerprint, {})
    if err: raise Exception(err.decode())
    return json.loads(out)
