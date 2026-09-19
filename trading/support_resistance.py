"""
NOVA Support & Resistance Engine

Analysis only.
Identifies recent support and resistance levels.

No trade execution.
"""


def find_levels(candles, lookback=100):
    if not candles:
        return {
            "support": None,
            "resistance": None
        }

    recent = candles[-lookback:]

    support = min(
        float(candle["low"])
        for candle in recent
    )

    resistance = max(
        float(candle["high"])
        for candle in recent
    )

    return {
        "support": support,
        "resistance": resistance
    }


def analyze_support_resistance(candles, lookback=100):
    if not candles:
        return {
            "success": False,
            "error": "No candle data."
        }

    levels = find_levels(candles, lookback)

    price = float(candles[-1]["close"])
    support = levels["support"]
    resistance = levels["resistance"]

    if price <= support:
        position = "AT_SUPPORT"
    elif price >= resistance:
        position = "AT_RESISTANCE"
    else:
        position = "BETWEEN_LEVELS"

    return {
        "success": True,
        "price": price,
        "support": support,
        "resistance": resistance,
        "position": position
    }
