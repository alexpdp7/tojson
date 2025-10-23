# tojson

tojson is a system to allow software to read JSON-like configuration from arbitrary formats.

tojson provides libraries for different languages with a load configuration function that takes the path to a file as an argument.
This function reads the file and then uses the first line to determine how to parse the rest of the file.

The first line should have the following format:

```
#? <FORMAT>
```

The function passes the rest of the file via standard input to the `<FORMAT>` parser, which is expected to produce JSON from the input to standard output , and returns the output parsed as JSON.

By using this library, your software can understand configuration defined in any format, or defined as code in any language that can output JSON.

## Safety

The [core of tojson](core) is compiled to an [Extism](https://extism.org/) plugin.
Extism plugins are WASM blobs executed in a controlled sandbox.

## Implemented parsers

### `json`

The `json` parser returns the rest of the file verbatim.

## Implemented libraries

* [`libraries/python`](libraries/python)
