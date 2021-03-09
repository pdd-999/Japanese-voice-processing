from pathlib import Path

for path in Path('.').rglob('*.py'):
    print(path)