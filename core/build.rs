fn main() {
    let output = format!(
        "{}/python-parser.wasm",
        std::env::var("OUT_DIR").expect("OUT_DIR to be set")
    );
    println!("cargo::rerun-if-changed=../parsers/python/build.py");
    println!("cargo::rerun-if-changed=../parsers/python/parser.py");
    println!("cargo::rustc-env=PYTHON_PARSER_WASM={output}");
    let status = std::process::Command::new("../parsers/python/build.py")
        .arg("../parsers/python/parser.py")
        .arg(output)
        .status()
        .expect("builder to run");
    if !status.success() {
        panic!("builder exited with {status}");
    }
}
