from ._commands import Commands
from ._comm import communicate

import json

def audio_info():
    """Get information about audio capabilities."""
    out, err = communicate(Commands.audio_info, {})
    if err: raise Exception(err.decode())
    return json.loads(out)
