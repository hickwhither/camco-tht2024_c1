import subprocess
from subprocess import PIPE

from typing import Any

class Interactor(subprocess.Popen):

    def __init__(self, path, *args, **kwargs) -> None:
        super().__init__(path, stdin=PIPE, stdout=PIPE, encoding='utf-8')
    
    def readline(self) -> None:
        text = self.stdout.readline().strip()
        return text

    def writeline(self, *inp: Any) -> None:
        text = str(' '.join(str(i) for i in inp) + '\n')
        self.stdin.write(text)
        self.stdin.flush()
    