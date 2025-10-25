use extism_pdk::*;

#[plugin_fn]
pub fn tojson(input: String) -> FnResult<String> {
    let (header, rest) = input
        .split_once("\n")
        .expect("file to have more than one line");
    match header {
        "#? json" => Ok(rest.into()),
        _ => panic!("unknown header {header}"),
    }
}
