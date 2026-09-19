"""
NOVA Liquidity Analysis

Analysis only.
Identifies:
- Buy-side liquidity
- Sell-side liquidity
- Equal highs
- Equal lows
- Recent liquidity levels

No trade execution.
"""


def _price_close(a, b, tolerance):
    return abs(a - b) <= tolerance


def find_equal_highs(candles, tolerance=0.20, lookback=100):
    """Find groups of nearby highs."""

    if not candles:
        return []

    recent = candles[-lookback:]
    results = []

    for i in range(len(recent)):
        high_a = float(recent[i]["high"])

        for j in range(i + 1, len(recent)):
            high_b = float(recent[j]["high"])

            if _price_close(high_a, high_b, tolerance):
                results.append({
                    "price": round((high_a + high_b) / 2, 5),
                    "first_index": i,
                    "second_index": j,
                    "type": "EQUAL_HIGH"
                })

    return results


def find_equal_lows(candles, tolerance=0.20, lookback=100):
    """Find groups of nearby lows."""

    if not candles:
        return []

    recent = candles[-lookback:]
    results = []

    for i in range(len(recent)):
        low_a = float(recent[i]["low"])

        for j in range(i + 1, len(recent)):
            low_b = float(recent[j]["low"])

            if _price_close(low_a, low_b, tolerance):
                results.append({
                    "price": round((low_a + low_b) / 2, 5),
                    "first_index": i,
                    "second_index": j,
                    "type": "EQUAL_LOW"
                })

    return results


def find_recent_liquidity(candles, lookback=50):
    """Find recent high and low liquidity levels."""

    if not candles:
        return {
            "buy_side": None,
            "sell_side": None
        }

    recent = candles[-lookback:]

    highest = max(
        float(candle["high"])
        for candle in recent
    )

    lowest = min(
        float(candle["low"])
        for candle in recent
    )

    return {
        "buy_side": {
            "price": highest,
            "type": "BUY_SIDE_LIQUIDITY"
        },
        "sell_side": {
            "price": lowest,
            "type": "SELL_SIDE_LIQUIDITY"
        }
    }


def analyze_liquidity(candles, tolerance=0.20, lookback=100):
    """Run complete liquidity analysis."""

    if not candles:
        return {
            "success": False,
            "error": "No candle data."
        }

    equal_highs = find_equal_highs(
        candles,
        tolerance,
        lookback
    )

    equal_lows = find_equal_lows(
        candles,
        tolerance,
        lookback
    )

    recent = find_recent_liquidity(
        candles,
        min(lookback, 50)
    )

    return {
        "success": True,
        "equal_highs": equal_highs,
        "equal_lows": equal_lows,
        "recent_liquidity": recent
    }
