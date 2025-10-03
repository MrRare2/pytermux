from ._commands import Commands
from ._comm import Arguments, Types, communicate

import json

def dialog_confirm(title: str = "", hint: str = "") -> dict:
    """Dialog confirm
    Args:
        hint: str
        title: stt"""
    args = Arguments()
    args += (Types.string, "input_method", "confirm")
    if hint: args += (Types.string, "input_hint", hint)
    if title: args += (Types.string, "input_title", title)
    out, err = communicate(Commands.dialog, args)
    if err: raise Exception(err.decode())
    return json.loads(out)

def dialog_checkbox(values: list[str], title: str = "") -> dict:
    """Dialog checkbox
    Args:
        values: list[str]
        title: stt"""
    args = Arguments()
    args += (Types.string, "input_method", "checkbox")
    if title: args += (Types.string, "input_title", title)
    v = ""
    if not isinstance(values, list) or not all([isinstance(x, str) for x in values]): raise ValueError("values argument must be list[str]")
    if len(values) <= 1: raise ValueError("values argument must have two or more elements")
    for el in values:
        v += el.replace(",", "\\,") + ","
    args += (Types.string, "input_values", v.rstrip(","))
    out, err = communicate(Commands.dialog, args)
    if err: raise Exception(err.decode())
    return json.loads(out)

def dialog_counter(title: str = "", min_: int = 0, max_: int = 100, start: int = 50) -> dict:
    """Dialog counter
    Args:
        title: str
        min_: int
        max_: int
        start: int"""
    args = Arguments()
    args += (Types.string, "input_method", "counter")
    if title: args += (Types.string, "input_title", title)
    if not all([isinstance(x, int) for x in [min_, max_, start]]): raise ValueError("min_, max_, and start arguments must be an integer")
    args += (Types.array_int, "input_range", f"{min_},{max_},{start}")
    out, err = communicate(Commands.dialog, args)
    if err: raise Exception(err.decode())
    return json.loads(out)

def dialog_date(title: str = "", fmt: str = "MM/dd/yyyy") -> dict:
    """Dialog date
    Args:
        title: str
        fmt: stt"""
    args = Arguments()
    args += (Types.string, "input_method", "date")
    if title: args += (Types.string, "input_title", title)
    args += (Types.string, "date_format", fmt)
    out, err = communicate(Commands.dialog, args)
    if err: raise Exception(err.decode())
    return json.loads(out)

def dialog_radio(values: list[str], title: str = "") -> dict:
    """Dialog radio
    Args:
        values: list[str]
        title: stt"""
    args = Arguments()
    args += (Types.string, "input_method", "radio")
    if title: args += (Types.string, "input_title", title)
    v = ""
    if not isinstance(values, list) or not all([isinstance(x, str) for x in values]): raise ValueError("values argument must be list[str]")
    if len(values) <= 1: raise ValueError("values argument must have two or more elements")
    for el in values:
        v += el.replace(",", "\\,") + ","
    args += (Types.string, "input_values", v.rstrip(","))
    out, err = communicate(Commands.dialog, args)
    if err: raise Exception(err.decode())
    return json.loads(out)

def dialog_spinner(values: list[str], title: str = "") -> dict:
    """Dialog spinner
    Args:
        values: list[str]
        title: stt"""
    args = Arguments()
    args += (Types.string, "input_method", "spinner")
    if title: args += (Types.string, "input_title", title)
    v = ""
    if not isinstance(values, list) or not all([isinstance(x, str) for x in values]): raise ValueError("values argument must be list[str]")
    if len(values) <= 1: raise ValueError("values argument must have two or more elements")
    for el in values:
        v += el.replace(",", "\\,") + ","
    args += (Types.string, "input_values", v.rstrip(","))
    out, err = communicate(Commands.dialog, args)
    if err: raise Exception(err.decode())
    return json.loads(out)

def dialog_speech(title: str = "", hint: str = "") -> dict:
    """Dialog speech
    Args:
        hint: str
        title: stt"""
    args = Arguments()
    args += (Types.string, "input_method", "speech")
    if hint: args += (Types.string, "input_hint", hint)
    if title: args += (Types.string, "input_title", title)
    out, err = communicate(Commands.dialog, args)
    if err: raise Exception(err.decode())
    return json.loads(out)

def dialog_text(title: str = "", hint: str = "", password: bool = False, multiline: bool = False, numeric: bool = False) -> dict:
    """Dialog text
    Args:
        hint: str
        title: str
        password: bool
        multiline: bool
        numeric: bool"""
    args = Arguments()
    args += (Types.string, "input_method", "text")
    if hint: args += (Types.string, "input_hint", hint)
    if title: args += (Types.string, "input_title", title)
    if multiline and numeric: raise Exception("incompatible pairs (multiline and numberic)")
    args += (Types.boolean, "numeric", f"{'true' if numeric else 'false'}")
    args += (Types.boolean, "multiline", f"{'true' if multiline else 'false'}")
    args += (Types.boolean, "password", f"{'true' if password else 'false'}")
    out, err = communicate(Commands.dialog, args)
    if err: raise Exception(err.decode())
    return json.loads(out)

def dialog_time(title: str = "") -> dict:
    """Dialog date
    Args:
        title: str"""
    args = Arguments()
    args += (Types.string, "input_method", "time")
    if title: args += (Types.string, "input_title", title)
    out, err = communicate(Commands.dialog, args)
    if err: raise Exception(err.decode())
    return json.loads(out)
