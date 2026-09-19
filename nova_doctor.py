import importlib
import os

CORE = [
    "calculator",
    "knowledge",
    "brain",
    "brain_api",
    "chatbot",
    "command_router",
    "config",
    "history",
    "session",
    "system",
    "task_manager",
    "utils",
    "weather",
    "search",
]

print("================================")
print("        NOVA DOCTOR")
print("================================")

passed = 0
failed = 0

for module in CORE:
    try:
        importlib.import_module(module)
        print(f"[OK]   {module}")
        passed += 1
    except Exception as e:
        print(f"[FAIL] {module} -> {type(e).__name__}: {e}")
        failed += 1

print("--------------------------------")
print("Files in NOVA:", len(os.listdir(".")))
print("PASSED:", passed)
print("FAILED:", failed)

if failed == 0:
    print("NOVA CORE: HEALTHY")
else:
    print("NOVA CORE: NEEDS REPAIR")

print("================================")
