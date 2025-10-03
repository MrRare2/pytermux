from ._commands import Commands
from ._comm import Arguments, Types, communicate

def download(url: str, file: str, title: str = "", description: str = "") -> None:
    """Downloads URL content using system's download manager
    Args:
        url: str
        file: str
        title: str
        description: str"""
    args = Arguments()
    args += (Types.string, "title", title)
    args += (Types.string, "description", description)
    args += (Types.string, "path", file)
    _, err = communicate(Commands.download, args, extra=[url])
    if err: raise Exception(err.decode())
