import json
import pathlib

import extism


HERE = pathlib.Path(__file__)


def load_config(path: pathlib.Path):
    manifest = {
        "wasm": [{"path": str(HERE.parent.parent.parent / "wasm" / "tojson.wasm")}]
    }
    with extism.Plugin(manifest, wasi=True) as plugin:
        return plugin.call(
            "tojson",
            data=path.read_text(),
            parse=lambda output: json.loads(bytes(output).decode("utf-8")),
        )
