from ._commands import Commands
from ._comm import Arguments, Types, communicate

import json

def call_logs() -> dict:
    """List call log history"""
    out, err = communicate(Commands.call_log, {})
    if err: raise Exception(err.decode())
    return json.loads(out)

def call(number: str) -> None:
    """Call the number

    Args:
        number (str): number to call
    """

    args = Arguments()
    args += (Types.string, "number", number)
    _, err = communicate(Commands.telephony_call, args)
    if err: raise Exception(err)

def cell_info() -> dict:
    """Get cell tower information"""

    out, err = communicate(Commands.telephony_cell_info, {})
    if err: raise Exception(err)
    return json.loads(out)
