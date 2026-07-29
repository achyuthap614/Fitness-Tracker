import os
import subprocess
import sys

root = os.getcwd()
input_path = os.path.join(root, "input_test.txt")
lines = []

for i in range(1, 31):
    lines.extend([
        "1",
        f"User{i}",
        str(20 + (i % 10)),
        "male" if i % 2 == 0 else "female",
        str(160 + (i * 0.5)),
        str(60 + i),
        str(22.0 + (i % 3) * 0.2),
        str(55 + (i % 5)),
        str(1000 + i),
        "5",
        str(1000 + i),
        "1",
        f"2026-01-{(i % 28) + 1:02d}",
        str(8000 + i),
        str(300 + i),
        str(45 + i),
        "Running",
        str(120 + (i % 20)),
        str(4 + (i % 3)),
        "3",
    ])

lines.append("6")

with open(input_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

with open(input_path, "r", encoding="utf-8") as f_in:
    proc = subprocess.run(
        [sys.executable, "main.py"],
        stdin=f_in,
        cwd=root,
        capture_output=True,
        text=True,
    )

print(proc.stdout)
print("EXIT_CODE:", proc.returncode)

if os.path.exists("Users.csv"):
    with open("Users.csv", "r", encoding="utf-8") as f:
        saved_lines = f.readlines()
    print("CSV_ROWS:", len(saved_lines))
    print("FIRST_3_ROWS:")
    for line in saved_lines[:3]:
        print(line.rstrip())
else:
    print("Users.csv not created")
