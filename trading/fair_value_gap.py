"""
NOVA Fair Value Gap Analysis

Analysis only.
Detects potential:
- Bullish Fair Value Gaps
- Bearish Fair Value Gaps

No trade execution.
"""


def find_fvg(candles, lookback=100):
    if not candles:
        return {
            "bullish": [],
            "bearish": []
        }

    recent = candles[-lookback:]

    bullish = []
    bearish = []

    # Three-candle FVG structure:
    #
    # Bullish:
    # candle 1 high < candle 3 low
    #
    # Bearish:
    # candle 1 low > candle 3 high

    for i in range(1, len(recent) - 1):
        first = recent[i - 1]
        third = recent[i + 1]

        first_high = float(first["high"])
        first_low = float(first["low"])

        third_high = float(third["high"])
        third_low = float(third["low"])

        # Bullish FVG
        if first_high < third_low:
            bullish.append({
                "index": i,
                "low": first_high,
                "high": third_low,
                "type": "BULLISH_FVG"
            })

        # Bearish FVG
        elif first_low > third_high:
            bearish.append({
                "index": i,
                "low": third_high,
                "high": first_low,
                "type": "BEARISH_FVG"
            })

    return {
        "bullish": bullish,
        "bearish": bearish
    }


def analyze_fvg(candles, lookback=100):
    """Run complete Fair Value Gap analysis."""

    if not candles:
        return {
            "success": False,
            "error": "No candle data."
        }

    gaps = find_fvg(candles, lookback)

    return {
        "success": True,
        "bullish_fvg": gaps["bullish"],
        "bearish_fvg": gaps["bearish"],
        "bullish_count": len(gaps["bullish"]),
        "bearish_count": len(gaps["bearish"])
    }
