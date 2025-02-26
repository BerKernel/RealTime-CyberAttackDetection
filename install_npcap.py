# install_npcap.py

import os
import subprocess
import urllib.request
import winreg

def is_npcap_installed():
    try:
        reg_key = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            r"SOFTWARE\Npcap",
            0,
            winreg.KEY_READ
        )
        winreg.CloseKey(reg_key)
        return True
    except FileNotFoundError:
        return False

def install_npcap_silent():
    npcap_url = "https://nmap.org/npcap/dist/npcap-1.71.exe"
    installer_name = "npcap-setup.exe"

    print(f"Downloading Npcap from {npcap_url}...")
    urllib.request.urlretrieve(npcap_url, installer_name)

    print("Installing Npcap in silent mode...")
    # /S = silent, /winpcap_mode=yes = WinPcap compatibility
    # shell=True is used for passing arguments to the exe
    subprocess.run([installer_name, "/S", "/winpcap_mode=yes"], shell=True)

    print("Npcap installation completed (silent mode).")

def main():
    # 1) Check if Npcap is installed
    if is_npcap_installed():
        print("Npcap is already installed.")
    else:
        print("Npcap not found. Installing now...")
        install_npcap_silent()

        # Check again
        if is_npcap_installed():
            print("Npcap installed successfully!")
        else:
            print("Npcap installation might have failed or was blocked.")

if __name__ == "__main__":
    main()
