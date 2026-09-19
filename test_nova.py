from commands import execute
from lesson_engine import teach
from memory import remember, recall


print("NOVA TEST")
print("=========")

assert "Hello" in execute("hello")
assert "NOVA" in execute("who are you")

remember(
    "__nova_test__",
    "working"
)

assert recall(
    "__nova_test__"
) == "working"

lesson = teach(
    "mathematics",
    "form1",
    "numbers"
)

assert lesson is not None
assert "NUMBERS" in lesson

print("Core: OK")
print("Commands: OK")
print("Memory: OK")
print("Learning engine: OK")
print("Starter lessons: OK")
print("NOVA TEST: PASSED")
