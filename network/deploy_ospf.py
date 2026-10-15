"""Enable OSPF (process 1, area 0, all interfaces) on multiple Cisco IOS routers.

Usage:
    python deploy_ospf.py devices.txt
"""

import argparse

import ssh_helpers

OSPF_COMMANDS = [
    "configure terminal",
    "router ospf 1",
    "network 0.0.0.0 255.255.255.255 area 0",
    "end",
    "show ip protocols",
]


def configure(host: str, creds: dict) -> None:
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
        for cmd in OSPF_COMMANDS:
            ssh_helpers.send_command(shell, cmd)
        print(ssh_helpers.read_output(shell))
        print("*" * 80)
    finally:
        ssh_helpers.close(client)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("devices", help="file with one router IP or hostname per line")
    args = parser.parse_args()

    creds = ssh_helpers.get_credentials(need_enable=True)
    for host in ssh_helpers.load_devices(args.devices):
        configure(host, creds)


if __name__ == "__main__":
    main()
