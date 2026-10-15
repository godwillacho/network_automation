"""Create a Linux user on a remote host over SSH, then optionally list users.

Usage: python linux_create_user.py <host>
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import ssh_helpers  # noqa: E402

if len(sys.argv) != 2:
    sys.exit("Usage: python linux_create_user.py <host>")
host = sys.argv[1]

creds = ssh_helpers.get_credentials()
new_user = input("User to create: ").strip()

# Only allow valid Linux usernames, so the value cannot inject extra shell commands.
if not re.fullmatch(r"[a-z_][a-z0-9_-]{0,31}", new_user):
    sys.exit("Invalid username")

client = ssh_helpers.connect(host, creds["username"], creds["password"])
try:
    shell = ssh_helpers.invoke_shell(client)
    ssh_helpers.send_command(shell, f"sudo useradd -m -d /home/{new_user} -s /bin/bash {new_user}")
    ssh_helpers.send_command(shell, creds["password"])  # answer the sudo prompt
    print(f"User {new_user} created.")

    if input("Display users? (y/n) ").strip().lower() in {"y", "yes"}:
        ssh_helpers.send_command(shell, "cut -d: -f1 /etc/passwd")
        print(ssh_helpers.read_output(shell))
finally:
    ssh_helpers.close(client)
