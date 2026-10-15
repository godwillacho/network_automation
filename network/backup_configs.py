"""Back up the running configuration of multiple Cisco IOS devices over SSH.

Each device's config is saved to backups/<host>_<YYYY-MM-DD_HHMM>.txt.
Use --parallel to back up all devices at once with one thread per device.

Usage:
    python backup_configs.py devices.txt
    python backup_configs.py devices.txt --parallel
"""

import argparse
import threading
from datetime import datetime
from pathlib import Path

import ssh_helpers

BACKUP_DIR = Path("backups")


def backup_device(host: str, creds: dict) -> None:
    try:
        client = ssh_helpers.connect(host, creds["username"], creds["password"])
    except Exception as exc:
        print(f"[{host}] connection failed: {exc}")
        return

    try:
        shell = ssh_helpers.invoke_shell(client)
        ssh_helpers.send_command(shell, "terminal length 0")
        ssh_helpers.send_command(shell, "enable")
        ssh_helpers.send_command(shell, creds["enable_secret"])
        ssh_helpers.send_command(shell, "show running-config", wait=3)
        output = ssh_helpers.read_output(shell)

        # Keep only the config itself, from the first "version" line to the final "end".
        lines = output.splitlines()
        start = next((i for i, l in enumerate(lines) if l.startswith("version ")), 0)
        end = max((i for i, l in enumerate(lines) if l.strip() == "end"), default=len(lines) - 1)
        config = "\n".join(lines[start:end + 1])

        BACKUP_DIR.mkdir(exist_ok=True)
        stamp = datetime.now().strftime("%Y-%m-%d_%H%M")
        path = BACKUP_DIR / f"{host}_{stamp}.txt"
        path.write_text(config)
        print(f"[{host}] saved {path}")
    finally:
        ssh_helpers.close(client)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("devices", help="file with one device IP or hostname per line")
    parser.add_argument("--parallel", action="store_true", help="back up all devices concurrently")
    args = parser.parse_args()

    hosts = ssh_helpers.load_devices(args.devices)
    creds = ssh_helpers.get_credentials(need_enable=True)

    if args.parallel:
        threads = [threading.Thread(target=backup_device, args=(h, creds)) for h in hosts]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
    else:
        for host in hosts:
            backup_device(host, creds)


if __name__ == "__main__":
    main()
