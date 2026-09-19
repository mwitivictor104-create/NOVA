"""
NOVA Market Structure Engine

Analysis only.
Detects:
- Swing highs
- Swing lows
- Higher highs (HH)
- Higher lows (HL)
- Lower highs (LH)
- Lower lows (LL)
- Basic bullish/bearish structure

No trade execution.
"""


def find_swing_highs(candles, strength=2):
    """Return indexes of swing highs."""
    swings = []

    if len(candles) < (strength * 2 + 1):
        return swings

    for i in range(strength, len(candles) - strength):
        current_high = float(candles[i]["high"])

        is_swing = True

        for j in range(1, strength + 1):
            if current_high <= float(candles[i - j]["high"]):
                is_swing = False
                break

            if current_high <= float(candles[i + j]["high"]):
                is_swing = False
                break

        if is_swing:
            swings.append({
                "index": i,
                "price": current_high,
                "type": "SWING_HIGH"
            })

    return swings


def find_swing_lows(candles, strength=2):
    """Return indexes of swing lows."""
    swings = []

    if len(candles) < (strength * 2 + 1):
        return swings

    for i in range(strength, len(candles) - strength):
        current_low = float(candles[i]["low"])

        is_swing = True

        for j in range(1, strength + 1):
            if current_low >= float(candles[i - j]["low"]):
                is_swing = False
                break

            if current_low >= float(candles[i + j]["low"]):
                is_swing = False
                break

        if is_swing:
            swings.append({
                "index": i,
                "price": current_low,
                "type": "SWING_LOW"
            })

    return swings


def classify_structure(swing_highs, swing_lows):
    """
    Classify recent swing points as:
    HH, LH, HL, LL.
    """

    classifications = []

    previous_high = None
    previous_low = None

    for swing in sorted(
        swing_highs + swing_lows,
        key=lambda x: x["index"]
    ):
        price = swing["price"]

        if swing["type"] == "SWING_HIGH":
            if previous_high is not None:
                if price > previous_high:
                    structure = "HH"
                else:
                    structure = "LH"
            else:
                structure = "HIGH"

            previous_high = price

        else:
            if previous_low is not None:
                if price > previous_low:
                    structure = "HL"
                else:
                    structure = "LL"
            else:
                structure = "LOW"

            previous_low = price

        classifications.append({
            "index": swing["index"],
            "price": price,
            "type": swing["type"],
            "structure": structure
        })

    return classifications


def detect_trend(classifications):
    """Determine basic market structure trend."""

    if not classifications:
        return {
            "trend": "UNKNOWN",
            "reason": "Not enough swing points."
        }

    recent = classifications[-10:]

    hh = sum(1 for x in recent if x["structure"] == "HH")
    hl = sum(1 for x in recent if x["structure"] == "HL")
    lh = sum(1 for x in recent if x["structure"] == "LH")
    ll = sum(1 for x in recent if x["structure"] == "LL")

    bullish = hh + hl
    bearish = lh + ll

    if bullish > bearish:
        trend = "BULLISH"
    elif bearish > bullish:
        trend = "BEARISH"
    else:
        trend = "RANGE"

    return {
        "trend": trend,
        "bullish_points": bullish,
        "bearish_points": bearish,
        "reason": (
            f"Recent structure: "
            f"HH={hh}, HL={hl}, LH={lh}, LL={ll}"
        )
    }


def analyze_structure(candles, strength=2):
    """Run the complete market-structure analysis."""

    if not candles:
        return {
            "success": False,
            "error": "No candle data."
        }

    highs = find_swing_highs(candles, strength)
    lows = find_swing_lows(candles, strength)

    classifications = classify_structure(highs, lows)
    trend = detect_trend(classifications)

    return {
        "success": True,
        "swing_highs": highs,
        "swing_lows": lows,
        "structure": classifications,
        "trend": trend
    }
