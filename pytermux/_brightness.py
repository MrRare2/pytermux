from ._commands import Commands
from ._comm import Arguments, Types, communicate

import json

def set_brightness(value: int) -> None:
    """Set the screen brightness between 0 - 255 or auto
    
    Args:
        value (int): value to set, between 0 and 255, or -1 for auto

    Raises:
        ValueError: value not within 0-255 or -1
        Exception: command errors"""
    args = Arguments()
    if 255 >= value >= 0: args += (Types.integer, "brightness", str(value))
    elif value == -1: args += (Types.boolean, "auto", "true")
    else: raise ValueError("Value not within 0 - 255 or -1")
    out, err = communicate(Commands.brightness, args)
    if err: raise Exception(err.decode())

