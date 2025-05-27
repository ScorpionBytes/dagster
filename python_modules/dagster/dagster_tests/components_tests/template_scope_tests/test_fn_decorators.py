from dagster.components.component.injectables import (
    is_template_udf,
    is_template_var,
    template_udf,
    template_var,
)


def test_template_udf_decorator():
    @template_udf
    def my_udf(x: str) -> str:
        return f"udf_{x}"

    assert is_template_udf(my_udf)
    assert my_udf("test") == "udf_test"


def test_template_udf_decorator_with_parens():
    @template_udf()
    def my_udf(x: str) -> str:
        return f"udf_{x}"

    assert is_template_udf(my_udf)
    assert my_udf("test") == "udf_test"


def test_template_udf_decorator_preserves_function_metadata():
    @template_udf
    def my_udf(x: str) -> str:
        """Test docstring."""
        return f"udf_{x}"

    assert my_udf.__name__ == "my_udf"
    assert my_udf.__doc__ == "Test docstring."


def test_is_template_udf():
    def regular_fn(x: str) -> str:
        return f"regular_{x}"

    @template_udf
    def udf_fn(x: str) -> str:
        return f"udf_{x}"

    assert not is_template_udf(regular_fn)
    assert is_template_udf(udf_fn)


def test_template_var_decorator():
    @template_var
    def my_var() -> str:
        return "var_value"

    assert is_template_var(my_var)
    assert my_var() == "var_value"


def test_template_var_decorator_with_parens():
    @template_var()
    def my_var() -> str:
        return "var_value"

    assert is_template_var(my_var)
    assert my_var() == "var_value"


def test_template_var_decorator_preserves_function_metadata():
    @template_var
    def my_var() -> str:
        """Test docstring."""
        return "var_value"

    assert my_var.__name__ == "my_var"
    assert my_var.__doc__ == "Test docstring."


def test_is_template_var():
    def regular_fn() -> str:
        return "regular_value"

    @template_var
    def var_fn() -> str:
        return "var_value"

    assert not is_template_var(regular_fn)
    assert is_template_var(var_fn)
