import os
import sys
from pathlib import Path
import textwrap

marker = "#path.fll-DATA"

input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("file.txt")
data = input_path.read_text(encoding="utf-8")

idx = data.find(marker)
if idx != -1:
    data = data[:idx].rstrip("\r\n")

data = data.replace("#PATH-POINTS-START Path", "")

data = textwrap.indent(data, "    ")

data = '[' + data + '\n]'

data = textwrap.indent(data, "    ")

data = '{"path": ' + '\n' + data + '\n}'

output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("path.json")
output_path.write_text(data, encoding="utf-8")

