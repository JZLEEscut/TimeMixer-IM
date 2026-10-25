from src.interfaces import ForecastRequest


def test_forecast_request_is_dataset_independent():
    request = ForecastRequest(history=[[0.0]], future_covariates=None, horizon=28)
    assert request.horizon == 28
    assert request.future_covariates is None
