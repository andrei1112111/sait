# src/my_cli_tool/platform_info.py
import platform
import sys
from dataclasses import dataclass


@dataclass()
class PlatformInfo:
    def __init__(self, **kwargs) -> None:
        self.system = kwargs.get("system", "system not found")
        self.machine = kwargs.get("machine", "machine not found")
        self.release = kwargs.get("release", "release not found")
        self.python_version = kwargs.get("python_version", "python version not found")

        if self.system == "Darwin":
            self.system = "macOS"
        if self.machine.lower() in ("arm64", "aarch64"):
                self.machine = "arm64"
        elif self.machine.lower() in ("x86_64", "amd64"):
            self.machine = "x86_64"

    @property
    def key(self) -> str:
        system = self.system.lower()
        machine = self.machine.lower()

        return f"{system}-{machine}"

    def __str__(self):
        return f"{self.system} {self.release} {self.machine}"

def detect_platform() -> PlatformInfo:
    return PlatformInfo(
        system=platform.system(),
        machine=platform.machine(),
        release=platform.release(),
        version=platform.version(),
        is_64bit=sys.maxsize > 2**32,
        python_version=f"{sys.version_info.major}.{sys.version_info.minor}",
    )
