from ._commands import Commands
from ._comm import Arguments, Types, communicate

def clipboard_get() -> bytes:
    """Get current contents of the clipbosrd

    Returns:
        bytes: clipboard data"""
    out, err = communicate(Commands.clipboard, {Types.string: ("api_version", "2"), Types.boolean: ("set", "false")})
    if err: raise Exception(err.decode())
    return out

def clipboard_set(data: bytes) -> None:
    """Put data to the clipbosrd

    Args:
        data (bytes): data to be put on the clipboard
    """
    args = Arguments()
    if not data: return
    args += (Types.string, "api_version", "2")
    args += (Types.boolean, "set", "true")
    out, err = communicate(Commands.clipboard, args, stdin=data)
    if err: raise Exception(err)
