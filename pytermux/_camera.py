from ._commands import Commands
from ._comm import Arguments, Types, communicate

import json

def camera_info():
    """Get information about device camera(s)."""
    out, err = communicate(Commands.camera_info, {})
    if err: raise Exception(err.decode())
    return json.loads(out)

def camera_take(file: str, cam: int = 0):
    """Take a photo and save it to a file in JPEG format.

    Args:
        file (str): file path to store the image
        cam (int) = 0: camera id
    """

    args = Arguments()
    args += (Types.string, "file", file)
    args += (Types.string, "camera", str(cam))
    _, err = communicate(Commands.camera_photo, args)
    if err: raise Exception(err)

def torch_set(enabled: bool) -> dict:
    """Toggle torch/flashlight
    Args:
        enabled: bool"""
    args = Arguments()
    args += (Types.boolean, "enabled", f"{'true' if enabled else 'false'}")
    out, err = communicate(Commands.torch, args)
    if err: raise Exception(err.decode())
    return json.loads(out)
