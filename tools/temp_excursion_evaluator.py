"""
temp_excursion_evaluator.py - Evaluates temperature time-series logs against standard 2C to 8C cold chain bounds
"""
import sys
import json


def evaluate_temp_excursion(temp_series_json: str, min_c: float = 2.0, max_c: float = 8.0):
    import json
    temps = json.loads(temp_series_json) if isinstance(temp_series_json, str) else temp_series_json
    excursions = [t for t in temps if t < min_c or t > max_c]
    has_excursion = len(excursions) > 0
    return {
        "readings_count": len(temps),
        "excursions_count": len(excursions),
        "compliant": not has_excursion,
        "status": "COLD_CHAIN_MAINTAINED" if not has_excursion else "TEMPERATURE_EXCURSION_ALERT"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "temp-excursion-evaluator"}))
