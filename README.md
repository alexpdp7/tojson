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

## Motivating examples and features

tojson has none of these features yet.
However, tojson is designed to enable these features.

### Using your favorite format

Many tools allow only JSON, YAML, or other popular formats for configuration.

Some people dislike JSON or YAML, and prefer other configuration formats, such as TOML, or more featureful languages such as Jsonnet or Dhall.

If tojson implements support for a format, then all software using tosjon can use this format.

### WASM

#### Sandboxing

By using WASM parsers, execution of the parser is sandboxed by default.

tojson could implement opt-in capabilities for parsers, such as accessing parts of the filesystem, making network calls, and others.

#### Extensibility

tojson could support loading parsers from the network or from other parts of the filesystem.

By doing this, third parties can add new parsers without modifying tojson.

### Programming language parsers

Some configuration artifacts, such as Kubernetes resources manifests, can be very tedious to write.

Programmable configurable languages such as Jsonnet implement libraries to automate configurations, such as [the Jsonnet Kubernetes library](https://jsonnet-libs.github.io/k8s-libsonnet/).

Tools that use Kubernetes manifests that use tojson would automatically gain support for such libraries, if tojson added Jsonnet support.

Additionally, by implementing tojson parsers such as a Python executor, tojson users could write their own abstractions in their language of choice.

For example:

```
#? https://tojson.parsers/python3x.wasm +mount(https://python.k8s/lib.py,/k8s.py)
import k8s

k8s.deployment(name="foo", image="myimage")
```

A similar example would be continuous integration manifests.
Systems such as GitHub Actions use YAML configuration files.

In general, many projects can use similar GitHub Actions configurations.
For example, projects using the same programming language often use similar GitHub Actions workflows.

If GitHub Actions supported tojson, then:

```
#? https://tojson.parsers/python3x.wasm +mount(https://python.ci/lib.py,/ruby.py)

ruby.github_actions()
```

could provide a configurable set of workflows that lint and test Ruby projects.

### Declarative operating systems

Declarative operating systems such as NixOS or GNU Guix use a programming language to write the operating system configuration.

This requires users of those operating systems to learn a very specific language.

Declarative operating systems could use tojson instead of their own language, and build the system from JSON input.
Then, users could write their configuration in their language of choice, instead of having to learn a specialized language.

By implementing tojson parsers for their languages, users could continue using their existing configurations.
