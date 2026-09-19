"""
NOVA Trend Engine

Analysis only.
Combines:
- EMA trend
- Market structure trend

No trade execution.
"""

from .indicators import ema
from .market_structure import analyze_structure


def analyze_trend(candles):
    if not candles or len(candles) < 20:
        return {
            "success": False,
            "trend": "UNKNOWN",
            "reason": "Not enough candle data."
        }

    closes = [
        float(candle["close"])
        for candle in candles
    ]

    ema20 = ema(closes, 20)
    ema50 = ema(closes, 50)
    ema200 = ema(closes, 200)

    structure = analyze_structure(candles)
    structure_trend = structure["trend"]["trend"]

    bullish_points = 0
    bearish_points = 0
    reasons = []

    if ema20 is not None and ema50 is not None:
        if ema20 > ema50:
            bullish_points += 1
            reasons.append("EMA20 above EMA50")
        elif ema20 < ema50:
            bearish_points += 1
            reasons.append("EMA20 below EMA50")

    price = closes[-1]

    if ema200 is not None:
        if price > ema200:
            bullish_points += 1
            reasons.append("Price above EMA200")
        elif price < ema200:
            bearish_points += 1
            reasons.append("Price below EMA200")

    if structure_trend == "BULLISH":
        bullish_points += 2
        reasons.append("Market structure bullish")
    elif structure_trend == "BEARISH":
        bearish_points += 2
        reasons.append("Market structure bearish")

    if bullish_points > bearish_points:
        trend = "BULLISH"
    elif bearish_points > bullish_points:
        trend = "BEARISH"
    else:
        trend = "RANGE"

    return {
        "success": True,
        "trend": trend,
        "ema20": ema20,
        "ema50": ema50,
        "ema200": ema200,
        "structure_trend": structure_trend,
        "bullish_points": bullish_points,
        "bearish_points": bearish_points,
        "reasons": reasons
    }
