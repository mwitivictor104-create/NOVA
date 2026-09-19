"""
NOVA Order Block Analysis

Analysis only.
Identifies potential:
- Bullish order blocks
- Bearish order blocks

No trade execution.
"""


def find_order_blocks(candles, lookback=100):
    if not candles:
        return {
            "bullish": [],
            "bearish": []
        }

    recent = candles[-lookback:]

    bullish = []
    bearish = []

    for i in range(1, len(recent) - 1):
        previous = recent[i - 1]
        current = recent[i]
        following = recent[i + 1]

        current_open = float(current["open"])
        current_close = float(current["close"])
        current_high = float(current["high"])
        current_low = float(current["low"])

        next_close = float(following["close"])

        # Bearish candle followed by bullish displacement
        if current_close < current_open:
            if next_close > current_high:
                bullish.append({
                    "index": i,
                    "high": current_high,
                    "low": current_low,
                    "type": "BULLISH_ORDER_BLOCK"
                })

        # Bullish candle followed by bearish displacement
        elif current_close > current_open:
            if next_close < current_low:
                bearish.append({
                    "index": i,
                    "high": current_high,
                    "low": current_low,
                    "type": "BEARISH_ORDER_BLOCK"
                })

    return {
        "bullish": bullish,
        "bearish": bearish
    }


def analyze_order_blocks(candles, lookback=100):
    """Run order-block analysis."""

    if not candles:
        return {
            "success": False,
            "error": "No candle data."
        }

    blocks = find_order_blocks(candles, lookback)

    return {
        "success": True,
        "bullish_order_blocks": blocks["bullish"],
        "bearish_order_blocks": blocks["bearish"],
        "bullish_count": len(blocks["bullish"]),
        "bearish_count": len(blocks["bearish"])
    }

