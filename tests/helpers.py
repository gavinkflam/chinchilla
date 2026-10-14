"""Helpers for writing tests."""

from typing import Any, Callable, NamedTuple


class TestCase(NamedTuple):
    """Tuple to define a test case."""

    inputs: dict[str, Any]
    expected: Any


def run_test_cases(test_cases: list[TestCase], test_fn: Callable[..., Any]):
    """Run `test_fn` against the provided test cases."""

    for i, tc in enumerate(test_cases):
        actual = test_fn(*tc.inputs.values())

        assert (
            actual == tc.expected
        ), f"test case #{i}: expected {tc.expected}, got {actual}, inputs {tc.inputs}"
