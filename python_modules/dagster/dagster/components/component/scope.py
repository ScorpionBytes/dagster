import inspect
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Callable, Optional, Union, overload

from typing_extensions import TypeAlias

from dagster._core.errors import DagsterInvalidDefinitionError

if TYPE_CHECKING:
    from dagster.components.core.context import ComponentLoadContext

SCOPE_FN_ATTR = "__dagster_scope_fn"


@dataclass
class Scope:
    scope: dict[str, Any]


TScopeFn: TypeAlias = Callable[["ComponentLoadContext"], Scope]


@overload
def scope(fn: TScopeFn) -> TScopeFn: ...


@overload
def scope() -> Callable[[TScopeFn], TScopeFn]: ...


def scope(fn: Optional[TScopeFn] = None) -> Union[TScopeFn, Callable[[TScopeFn], TScopeFn]]:
    def decorator(func: TScopeFn) -> TScopeFn:
        setattr(func, SCOPE_FN_ATTR, True)
        return func

    if fn is None:
        # Called as @scope()
        return decorator
    else:
        # Called as @scope
        return decorator(fn)


def is_scope_fn(obj: Any) -> bool:
    return getattr(obj, SCOPE_FN_ATTR, False)


def find_scope_fn(module: Any) -> Optional[TScopeFn]:
    """Finds a scope function in the given module.

    Args:
        module: The module to search for a scope function

    Returns:
        The scope function if found, None otherwise
    """
    scope_fns = [obj for _, obj in inspect.getmembers(module, is_scope_fn)]
    if len(scope_fns) == 0:
        return None
    elif len(scope_fns) == 1:
        return scope_fns[0]
    else:
        raise DagsterInvalidDefinitionError(
            f"Multiple scope functions found in module: {scope_fns}"
        )
