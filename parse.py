import os
import sys
from pathlib import Path

marker = "#path.fll-DATA"

# Read the file (optionally pass input path as first arg)
input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("file.txt")
data = input_path.read_text(encoding="utf-8")

idx = data.find(marker)
if idx != -1:
    data = data[:idx].rstrip("\r\n")

data = '{"path": [' + data + ']}'

output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("path.json")
output_path.write_text(data, encoding="utf-8")

