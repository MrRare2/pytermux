from ._commands import Commands
from ._comm import communicate

import json

def get_contacts() -> dict:
    """Get all contacts"""
    out, err = communicate(Commands.contact_list, {})
    if err: raise Exception(err.decode())
    return json.loads(out)
