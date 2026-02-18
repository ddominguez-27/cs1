import sys
import os

print("Python paths being checked:")
for p in sys.path:
    if os.path.exists(p):
        print(f"\nChecking {p}:")
        for f in os.listdir(p):
            if f.endswith(".py"):
                print("  ", f)
                