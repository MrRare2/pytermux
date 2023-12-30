from . import _exception
from . import _check
from ._volume import Volume
import subprocess
import json

prog = "termux-tts-speak"

class TTS:
    """Base class for Text-to-speak (TTS) (termux-tts-speak)"""
    def __init__(self):
        self._streams = Volume()._streams

    def _run(self, command):
        """Function to run commands on Termux
        Args:
        command - the command you want to execute"""
        return subprocess.run(command, capture_output=True)

    def speak(self, text, lang="en", region=None, variant=None, pitch=1, rate=1, stream="music"):
        """Make TTS speak
        Args:
            text - the text you want TTS speak
            lang - the language of the TTS (defsult is English)
            region - the region of language to speak in
            variant - the variant of the language to speak in
            pitch - pitch of the TTS (default is 1)
            rate - speech rate, the greater, the faster TTS will speak
            stream - audio stream to use (see Volume.list_streams())"""

        if pitch <= 0:
            pitch = 0.1
        if rate <= 0:
            rate = 0.1
        if stream not in self._streams:
            raise ValueError('invalid stream')
        region_ = False if region == None else True
        variant_ = False if variant == None else True
        stream = stream.upper()

        cmd = [prog, "-l", lang]
        cmd.extend(["-r", region]) if region_ else None
        cmd.extend(["-v", variant]) if variant_ else None
        cmd.extend(["-p", str(pitch), "-r", str(rate), "-s", stream, text])

        process = self._run(cmd)
        success = _check.check_success(process)

        try:
            err_msg = json.loads(process.stdout.strip())
            raise _exception.TermuxAPIError(err_msg["error"]) from None
        except Exception as e:
            if type(e) == _exception.TermuxAPIError:
                raise
        return True if success[0] else success
