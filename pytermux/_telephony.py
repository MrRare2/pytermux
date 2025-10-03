from ._commands import Commands
from ._comm import Arguments, Types, communicate

import json

def call_logs():
    """List call log history"""
    out, err = communicate(Commands.call_log, {})
    if err: raise Exception(err.decode())
    return json.loads(out)

def call(number: str, sim: int = 0):
    """Call the number

    Args:
        number (str): number to call
        sim (int) = 0: sim id
    """

    args = Arguments()
    args += (Types.string, "number", file)
    args += (Types.string, "sim", str(cam))
    out, err = communicate(Commands.camera_photo, args)
    if err: raise Exception(err)
