use extism_pdk::*;

#[plugin_fn]
pub fn tojson(name: String) -> FnResult<String> {
    Ok(name)
}
