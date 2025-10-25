#!/usr/bin/env python3
import io
import pathlib
import sys
import subprocess
import tarfile
import tempfile
import urllib.request

in_, out = sys.argv[1:]

with tempfile.TemporaryDirectory() as tempdir:
    tempdir = pathlib.Path(tempdir)
    print("Downloading extism...")
    with urllib.request.urlopen("https://github.com/extism/python-pdk/releases/download/v0.1.5/extism-py-x86_64-linux-v0.1.5.tar.gz") as f:
        archive = f.read()
    with tarfile.open(fileobj=io.BytesIO(archive)) as t:
        print("Extracting extism...")
        t.extractall(tempdir)
    print("Assembling wasm...")
    subprocess.run([tempdir / "extism-py" / "bin" / "extism-py", in_, "-o", out], check=True, env={"EXTISM_PYTHON_WASI_DEPS_DIR": tempdir / "extism-py" / "share" / "extism-py"})
print("Done!")
