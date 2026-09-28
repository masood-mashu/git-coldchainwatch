"""
mkt_kinetic_temp_calculator.py - Calculates Mean Kinetic Temperature (MKT) approximation across shipment thermal profile
"""
import sys
import json


def calculate_mkt(temp_readings_json: str):
    import json
    temps = json.loads(temp_readings_json) if isinstance(temp_readings_json, str) else temp_readings_json
    avg_temp = sum(temps) / max(len(temps), 1)
    is_safe = 2.0 <= avg_temp <= 8.0
    return {
        "average_mkt_c": round(avg_temp, 2),
        "safe_range": is_safe,
        "status": "MKT_APPROVED" if is_safe else "MKT_OUT_OF_BOUNDS"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "mkt-kinetic-temp-calculator"}))
