import json
import pathlib

import extism


HERE = pathlib.Path(__file__)


def load_config(path: pathlib.Path):
    header, rest = path.read_text().split("\n", 1)
    assert header == "#? json"

    manifest = {
        "wasm": [{"path": str(HERE.parent.parent.parent / "wasm" / "tojson.wasm")}]
    }
    with extism.Plugin(manifest, wasi=True) as plugin:
        return plugin.call(
            "tojson",
            data=rest,
            parse=lambda output: json.loads(bytes(output).decode("utf-8")),
        )
