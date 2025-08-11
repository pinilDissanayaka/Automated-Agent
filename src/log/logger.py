import logging
import functools
from typing import Any, Callable, Type, TypeVar

logger = logging.getLogger(__name__)

T = TypeVar("T")


def log_io(func: Callable) -> Callable:
    """
    Decorator to log input parameters and output of a function.

    This decorator logs the name of the function being executed, the input parameters
    passed to it, and the result it returns. It is useful for debugging and monitoring
    the behavior of functions.

    Args:
        func: The function to be wrapped and logged.

    Returns:
        A new callable that logs input and output when the original function is called.
    """

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Log input parameters
        """
        Wrapper function that logs input parameters and output of the wrapped function.

        The wrapper will log the name of the function being executed, the input parameters
        passed to it, and the result it returns.

        Args:
            *args: The positional arguments passed to the wrapped function.

            **kwargs: The keyword arguments passed to the wrapped function.

        Returns:
            The result of the wrapped function.

        """
        func_name = func.__name__
        params = ", ".join(
            [*(str(arg) for arg in args), *(f"{k}={v}" for k, v in kwargs.items())]
        )
        logger.debug(f"Tool {func_name} called with parameters: {params}")

        # Execute the function
        result = func(*args, **kwargs)

        # Log the output
        logger.debug(f"Tool {func_name} returned: {result}")

        return result

    return wrapper


class LoggedToolMixin:
    def _log_operation(self, method_name: str, *args: Any, **kwargs: Any) -> None:
        """Logs a message about the tool operation being called.

        The log message will include the name of the tool and the method being called,
        along with the parameters passed to the method.

        Args:
            method_name (str): The name of the method being called.
            *args (Any): The positional arguments passed to the method.
            **kwargs (Any): The keyword arguments passed to the method.
        """
        tool_name = self.__class__.__name__.replace("Logged", "")
        params = ", ".join(
            [*(str(arg) for arg in args), *(f"{k}={v}" for k, v in kwargs.items())]
        )
        logger.debug(f"Tool {tool_name}.{method_name} called with parameters: {params}")

    def _run(self, *args: Any, **kwargs: Any) -> Any:
        """Logs a message about the _run method being called.

        The log message will include the name of the tool and the method being called,
        along with the parameters passed to the method.

        Args:
            *args (Any): The positional arguments passed to the _run method.
            **kwargs (Any): The keyword arguments passed to the _run method.
        """
        self._log_operation("_run", *args, **kwargs)
        result = super()._run(*args, **kwargs)
        logger.debug(
            f"Tool {self.__class__.__name__.replace('Logged', '')} returned: {result}"
        )
        return result


def create_logged_tool(base_tool_class: Type[T]) -> Type[T]:
    """
    Factory function to create a logged version of any tool class.

    Args:
        base_tool_class: The original tool class to be enhanced with logging

    Returns:
        A new class that inherits from both LoggedToolMixin and the base tool class
    """

    class LoggedTool(LoggedToolMixin, base_tool_class):
        pass

    # Set a more descriptive name for the class
    LoggedTool.__name__ = f"Logged{base_tool_class.__name__}"
    return LoggedTool
