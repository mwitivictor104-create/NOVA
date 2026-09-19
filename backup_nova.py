import os
import shutil
import datetime


BASE = os.path.expanduser("~/NOVA")

timestamp = datetime.datetime.now().strftime(
    "%Y%m%d_%H%M%S"
)

backup_dir = os.path.expanduser(
    f"~/NOVA_BACKUP_{timestamp}"
)

shutil.copytree(
    BASE,
    backup_dir,
    ignore=shutil.ignore_patterns(
        "__pycache__",
        "*.pyc",
    )
)

print("NOVA BACKUP CREATED")
print(backup_dir)
