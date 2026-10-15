# Network Automation with Python

Python tools for automating Cisco IOS routers and Linux servers over SSH with Paramiko: bulk configuration backups, OSPF deployment across multiple routers, and remote Linux administration.

## Featured Tools (`network/`)

| Script | What it does |
|---|---|
| `backup_configs.py` | Backs up the running configuration of every device in a list to timestamped files. `--parallel` runs one thread per device. |
| `deploy_ospf.py` | Enables OSPF process 1 in area 0 on every router in a list and prints `show ip protocols` to verify. |
| `configure_loopback.py` | Pushes a list of configuration commands (a loopback interface) to a device and shows the result. |
| `ssh_helpers.py` | Shared helpers for connecting, sending commands, reading output and loading device lists. |

**Stack:** Python 3, Paramiko, SCP, threading, argparse

## Quick Start

```bash
pip install -r requirements.txt
cd network
cp devices.example.txt devices.txt        # one IP or hostname per line

# Credentials come from the environment, or you are prompted for them
export NET_USERNAME=admin
export NET_PASSWORD='...'
export NET_ENABLE_SECRET='...'

python backup_configs.py devices.txt --parallel
python deploy_ospf.py devices.txt
```

Backups are written to `network/backups/<host>_<date>_<time>.txt`. A redacted example is in `sample_running_config.txt`.

## Security

- No credentials are stored in code or device files. Scripts read `NET_USERNAME`, `NET_PASSWORD` and `NET_ENABLE_SECRET`, or prompt with `getpass`.
- `ssh_helpers.connect()` loads system known hosts. It auto-accepts unknown host keys for lab use; switch to `paramiko.RejectPolicy()` in production. See `learning/ssh_host_keys_in_paramiko.py` for host key verification.
- `linux_create_user.py` validates the new username before using it in a shell command, preventing command injection.
- Device backups are git-ignored because they contain password hashes.

## Repository Layout

```
network/
  backup_configs.py, deploy_ospf.py, configure_loopback.py, ssh_helpers.py
  learning/          Step-by-step Paramiko exercises: SSH basics, interactive
                     shells, looping commands, host keys, SCP transfers, Linux admin
python_practice/     Python fundamentals: file I/O, CSV, JSON, pickle, REST APIs
```

## Lab Environment

Developed against a lab of Cisco IOS routers and a Kali Linux virtual machine.
