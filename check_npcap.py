# check_npcap.py

import winreg

def is_npcap_installed():
    """
    Checks the Windows Registry to see if Npcap is installed.
    Returns True if found, False otherwise.
    """
    try:
        # Open the key where Npcap typically stores its info
        reg_key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Npcap",
            0,
            winreg.KEY_READ
        )
        # If we can open the key, we assume Npcap is installed
        winreg.CloseKey(reg_key)
        return True
    except FileNotFoundError:
        return False
