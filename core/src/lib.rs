#[extism_pdk::plugin_fn]
pub fn tojson(input: String) -> extism_pdk::FnResult<String> {
    let (header, rest) = input
        .split_once("\n")
        .expect("file to have more than one line");
    match header {
        "#? json" => Ok(rest.into()),
        "#? python" => run_python(rest),
        _ => panic!("unknown header {header}"),
    }
}

pub fn run_python(python: &str) -> extism_pdk::FnResult<String> {
    panic!(
        "{:?}",
        extism::Plugin::new(
            extism::Manifest::new([extism::Wasm::data(include_bytes!(env!(
                "PYTHON_PARSER_WASM"
            )))]),
            [],
            true
        )
        .unwrap()
        .call::<&str, &str>("greet", "foo")
    );
}
