from dagster.components.component.injectables import template_udf, template_var


@template_var
def foo() -> str:
    return "value_for_foo"


@template_udf
def a_udf() -> str:
    return "a_udf_value"


@template_udf
def a_udf_with_args(x: str) -> str:
    return f"a_udf_value_{x}"
