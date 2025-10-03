import subprocess

EXEC = "/data/data/com.termux/files/usr/libexec/termux-api"

class Types(object):
    string = 0
    integer = 1
    double = 2
    boolean = 3
    uri = 4
    null = 5
    float = 6
    long = 7
    short = 8
    char = 9
    byte = 10

class Argument(object):
    """
    Represents a single argument for an Intent.

    Attributes:
        type (int): Type of the argument (enum from Types).
        key (str): The key name for the argument.
        value (str|None): The string value of the argument.
    """
    def __init__(self, type: int, key: str, value: str | None = None):
        self.type = type
        self.key = key
        self.value = value

class Arguments(object):
    """
    Represents a collection of arguments for an Intent.

    Operators:
        += (int, str, str|None): Appends a new Argument with type, key, and value.

    Methods:
        build() -> list[str]: Converts arguments into CLI-ready string list.
    """
    def __init__(self):
        self._args = []

    def __iadd__(self, other):
        if not isinstance(other, tuple) or len(other) not in (2, 3):
            raise TypeError("Must be a tuple (int, str, str|None)")
        if len(other) == 2:
            t, k = other
            v = None
        else:
            t, k, v = other
        if not isinstance(t, int) or not isinstance(k, str) or (v is not None and not isinstance(v, str)):
            raise TypeError("Tuple must be (int, str, str|None)")
        self._args.append(Argument(t, k, v))
        return self

    def build(self) -> list[str]:
        result = []
        for arg in self._args:
            if arg.type == Types.string:
                result.extend(["--es", arg.key, arg.value])
            elif arg.type == Types.integer:
                result.extend(["--ei", arg.key, arg.value])
            elif arg.type == Types.double:
                result.extend(["--ed", arg.key, arg.value])
            elif arg.type == Types.boolean:
                result.extend(["--ez", arg.key, arg.value])
            elif arg.type == Types.uri:
                result.extend(["--eu", arg.key, arg.value])
            elif arg.type == Types.null:
                result.extend(["--esn", arg.key])
            elif arg.type == Types.float:
                result.extend(["--ef", arg.key, arg.value])
            elif arg.type == Types.long:
                result.extend(["--el", arg.key, arg.value])
            elif arg.type == Types.short:
                result.extend(["--es", arg.key, arg.value])
            elif arg.type == Types.char:
                result.extend(["--ec", arg.key, arg.value])
            elif arg.type == Types.byte:
                result.extend(["--eb", arg.key, arg.value])
            else:
                raise ValueError(f"Unsupported type: {arg.type}")
        return result

def communicate(command: str, args=None, stdin=None, timeout=30) -> tuple[bytes, bytes]:
    """
    Executes a termux-api command with arguments.

    Args:
        command (str): Command to run.
        args (None|Arguments|list[Argument|tuple[int,str,str|None]]|dict[int,tuple[str]|tuple[str,str]]): Arguments to process.
        stdin (bytes|None): Optional input stream.
        timeout (int): Timeout for process execution.

    Returns:
        tuple[bytes, bytes]: stdout and stderr as bytes.

    Raises:
        subprocess.TimeoutExpired: If process times out.
    """
    arg_list = []
    if args is None:
        arg_list = []
    elif isinstance(args, Arguments):
        arg_list = args.build()
    elif isinstance(args, list):
        arg_obj = Arguments()
        for item in args:
            if isinstance(item, Argument):
                arg_obj += (item.type, item.key, item.value)
            elif isinstance(item, tuple) and len(item) in (2, 3):
                arg_obj += item
            else:
                raise TypeError("List must contain Argument objects or (int,str,str|None) tuples")
        arg_list = arg_obj.build()
    elif isinstance(args, dict):
        arg_obj = Arguments()
        for t, kv in args.items():
            if kv is None:
                continue
            if not isinstance(t, int):
                raise TypeError("Dict keys must be Types")
            if not isinstance(kv, tuple) or len(kv) not in (1, 2):
                raise TypeError("Dict values must be (key,) or (key, value)")
            if len(kv) == 1:
                k = kv[0]
                v = None
            else:
                k, v = kv
            arg_obj += (t, k, v)
        arg_list = arg_obj.build()
    else:
        raise TypeError("Arguments must be None, Arguments, list, or dict[int, (str,) | (str, str)]")

    process = subprocess.Popen(
        [EXEC, command] + arg_list,
        stdin=subprocess.PIPE if stdin else None,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate(input=stdin, timeout=timeout)
    return stdout, stderr
