import inspect
from dataclasses import dataclass
from typing import Any, Callable, Optional, Union, overload

from typing_extensions import TypeAlias

TemplateUdfFn: TypeAlias = Callable[..., Any]

TEMPLATE_UDF_ATTR = "__dagster_template_udf"


@overload
def template_udf(fn: TemplateUdfFn) -> TemplateUdfFn: ...


@overload
def template_udf() -> Callable[[TemplateUdfFn], TemplateUdfFn]: ...


def template_udf(
    fn: Optional[TemplateUdfFn] = None,
) -> Union[TemplateUdfFn, Callable[[TemplateUdfFn], TemplateUdfFn]]:
    def decorator(func: TemplateUdfFn) -> TemplateUdfFn:
        setattr(func, TEMPLATE_UDF_ATTR, True)
        return func

    if fn is None:
        # called as @template_udf()
        return decorator
    else:
        # called as @template_udf
        return decorator(fn)


def is_template_udf(obj: Any) -> bool:
    return getattr(obj, TEMPLATE_UDF_ATTR, False)


TemplateVarFn: TypeAlias = Callable[[], Any]

TEMPLATE_VAR_ATTR = "__dagster_template_var"


@overload
def template_var(fn: TemplateVarFn) -> TemplateVarFn: ...


@overload
def template_var() -> Callable[[TemplateVarFn], TemplateVarFn]: ...


def template_var(
    fn: Optional[TemplateVarFn] = None,
) -> Union[TemplateVarFn, Callable[[TemplateVarFn], TemplateVarFn]]:
    def decorator(func: TemplateVarFn) -> TemplateVarFn:
        setattr(func, TEMPLATE_VAR_ATTR, True)
        return func

    if fn is None:
        return decorator
    else:
        return decorator(fn)


def is_template_var(obj: Any) -> bool:
    return getattr(obj, TEMPLATE_VAR_ATTR, False)


@dataclass
class TemplateInjectables:
    """Container for template functions found in a module.

    Attributes:
        udfs: Dictionary of functions decorated with @template_udf, indexed by function name
        vars: Dictionary of functions decorated with @template_var, indexed by function name
    """

    template_udfs: dict[str, Callable]
    template_vars: dict[str, Callable]


def find_injectables(module: Any) -> TemplateInjectables:
    """Finds all template functions in the given module.

    Args:
        module: The module to search for template functions

    Returns:
        A TemplateFunctions object containing dictionaries of template UDFs and vars indexed by name
    """
    template_defs = {}
    template_vars = {}

    for name, obj in inspect.getmembers(module):
        if is_template_udf(obj):
            template_defs[name] = obj
        elif is_template_var(obj):
            template_vars[name] = obj

    return TemplateInjectables(template_udfs=template_defs, template_vars=template_vars)
