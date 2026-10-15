"""Reusable Paramiko helpers for interactive SSH sessions with network devices.

Credentials are never stored in code. They are read from environment
variables (NET_USERNAME, NET_PASSWORD, NET_ENABLE_SECRET) or prompted for.
"""

import os
import time
from getpass import getpass
from pathlib import Path

import paramiko


def get_credentials(need_enable: bool = False) -> dict:
    """Return SSH credentials from the environment, prompting for anything missing."""
    username = os.getenv("NET_USERNAME") or input("SSH username: ")
    password = os.getenv("NET_PASSWORD") or getpass(f"SSH password for {username}: ")
    creds = {"username": username, "password": password}
    if need_enable:
        creds["enable_secret"] = os.getenv("NET_ENABLE_SECRET") or getpass("Enable secret: ")
    return creds


def load_devices(path: str = "devices.txt") -> list:
    """Read one device IP or hostname per line, ignoring blanks and # comments."""
    lines = Path(path).read_text().splitlines()
    return [line.strip() for line in lines if line.strip() and not line.strip().startswith("#")]


def connect(host: str, username: str, password: str, port: int = 22) -> paramiko.SSHClient:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    # Lab convenience: accept unknown host keys. In production, pre-load known_hosts
    # and use paramiko.RejectPolicy() instead.
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f"Connecting to {host}")
    client.connect(hostname=host, port=port, username=username, password=password,
                   allow_agent=False, look_for_keys=False, timeout=10)
    return client


def invoke_shell(client: paramiko.SSHClient):
    return client.invoke_shell()


def send_command(shell, command: str, wait: float = 1.0) -> None:
    shell.send(command + "\n")
    time.sleep(wait)


def read_output(shell, size: int = 65535) -> str:
    return shell.recv(size).decode("utf-8", errors="replace")


def close(client: paramiko.SSHClient) -> None:
    transport = client.get_transport()
    if transport and transport.is_active():
        print("Closing connection")
        client.close()
