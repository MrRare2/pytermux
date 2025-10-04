from ._commands import Commands
from ._comm import Arguments, Types, communicate

import json

def infrared_frequencies() -> dict | list:
    """Query supported carrier IR frequencies"""
    out, err = communicate(Commands.infrared_frequencies, {})
    if err: raise Exception(err.decode())
    return json.loads(out)

def infrared_transmit(frequency: int, pattern: list[int]) -> dict:
    """Transmit IR, if available
    Args:
        frequency: int
        pattern: list[int]"""
    args = Arguments()
    v = ""
    if not all([isinstance(x, int) for x in pattern]): raise ValueError("pattern argument must be list[int]")
    for el in pattern:
        v += f"{el},"
    args += (Types.array_int, "pattern", v.rstrip(","))
    args += (Types.integer, "frequency", str(frequency))
    out, err = communicate(Commands.infrared_transmit, args)
    if err: raise Exception(err)
    return json.loads(out)
