from ._class import Contact
from ._commands import Commands
from ._comm import communicate

import json

def get_contacts() -> list[Contact]:
    """Get all contacts"""
    out, err = communicate(Commands.contact_list, {})
    if err: raise Exception(err.decode())
    return [Contact(contact) for contact in json.loads(out)]
