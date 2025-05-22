from dagster.components.component.scope import Scope, is_scope_fn, scope
from dagster.components.core.context import ComponentLoadContext


def test_scope_decorator():
    @scope
    def my_scope(context: ComponentLoadContext) -> Scope:
        return Scope(scope={"foo": "bar"})

    assert is_scope_fn(my_scope)
    assert my_scope(ComponentLoadContext.for_test()).scope == {"foo": "bar"}


def test_scope_decorator_with_parens():
    @scope()
    def my_scope(context: ComponentLoadContext) -> Scope:
        return Scope(scope={"foo": "bar"})

    assert is_scope_fn(my_scope)
    assert my_scope(ComponentLoadContext.for_test()).scope == {"foo": "bar"}


def test_scope_decorator_preserves_function_metadata():
    @scope
    def my_scope(context: ComponentLoadContext) -> Scope:
        """Test docstring."""
        return Scope(scope={"foo": "bar"})

    assert my_scope.__name__ == "my_scope"
    assert my_scope.__doc__ == "Test docstring."


def test_is_scope_fn():
    def regular_fn(context: ComponentLoadContext) -> Scope:
        return Scope(scope={"foo": "bar"})

    @scope
    def scoped_fn(context: ComponentLoadContext) -> Scope:
        return Scope(scope={"foo": "bar"})

    assert not is_scope_fn(regular_fn)
    assert is_scope_fn(scoped_fn)
