from dagster.components.component.scope import Scope, scope
from dagster.components.core.context import ComponentLoadContext


@scope
def inject_scope(context: ComponentLoadContext) -> Scope:
    return Scope(
        scope={
            "foo": "value_for_foo",
            "a_udf": lambda: "a_udf_value",
            "a_udf_with_args": lambda x: f"a_udf_value_{x}",
        }
    )
