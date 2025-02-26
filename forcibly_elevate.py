# forcibly_elevate.py
import ctypes, sys

def run_as_admin():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        # re-run as admin
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit(0)
