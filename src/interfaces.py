"""Dataset-independent public interfaces.

These contracts make the future public release easier to maintain without
exposing the current private model or training implementation.
"""

from dataclasses import dataclass
from typing import Any, Mapping, Protocol, Sequence


@dataclass(frozen=True)
class ForecastRequest:
    """Inputs required by a future forecasting implementation."""

    history: Any
    future_covariates: Any | None
    horizon: int


class Forecaster(Protocol):
    """Minimal prediction contract for future public implementations."""

    def predict(self, request: ForecastRequest) -> Any:
        ...


class Evaluator(Protocol):
    """Evaluation contract; metric implementations remain private for now."""

    def evaluate(self, truth: Any, prediction: Any, horizons: Sequence[int]) -> Mapping[str, float]:
        ...
