from ._class import LocationInfo
from ._commands import Commands
from ._comm import communicate

def location() -> LocationInfo:
    """Get current location"""
    out, err = communicate(Commands.location, {})
    if err: raise Exception(err.decode())
    return LocationInfo(out)
