"""
NOVA Trading Indicators
Real OHLC-based technical indicators.
No trade execution.
"""

from math import sqrt


def _closes(candles):
    return [float(c["close"]) for c in candles]


def _highs(candles):
    return [float(c["high"]) for c in candles]


def _lows(candles):
    return [float(c["low"]) for c in candles]


def sma(values, period):
    if len(values) < period:
        return None
    return sum(values[-period:]) / period


def ema(values, period):
    if len(values) < period:
        return None

    multiplier = 2 / (period + 1)
    value = sum(values[:period]) / period

    for price in values[period:]:
        value = (price - value) * multiplier + value

    return value


def rsi(candles, period=14):
    closes = _closes(candles)

    if len(closes) <= period:
        return None

    gains = []
    losses = []

    for i in range(1, len(closes)):
        change = closes[i] - closes[i - 1]

        if change > 0:
            gains.append(change)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(change))

    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period

    for i in range(period, len(gains)):
        avg_gain = ((avg_gain * (period - 1)) + gains[i]) / period
        avg_loss = ((avg_loss * (period - 1)) + losses[i]) / period

    if avg_loss == 0:
        return 100.0

    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))


def atr(candles, period=14):
    if len(candles) <= period:
        return None

    true_ranges = []

    for i in range(1, len(candles)):
        high = float(candles[i]["high"])
        low = float(candles[i]["low"])
        previous_close = float(candles[i - 1]["close"])

        tr = max(
            high - low,
            abs(high - previous_close),
            abs(low - previous_close)
        )

        true_ranges.append(tr)

    return sum(true_ranges[-period:]) / period


def macd(candles, fast=12, slow=26, signal=9):
    closes = _closes(candles)

    if len(closes) < slow + signal:
        return None

    fast_ema = ema(closes, fast)
    slow_ema = ema(closes, slow)

    if fast_ema is None or slow_ema is None:
        return None

    macd_line = fast_ema - slow_ema

    macd_history = []

    for i in range(slow, len(closes) + 1):
        subset = closes[:i]

        f = ema(subset, fast)
        s = ema(subset, slow)

        if f is not None and s is not None:
            macd_history.append(f - s)

    signal_line = ema(macd_history, signal)

    if signal_line is None:
        return None

    histogram = macd_line - signal_line

    return {
        "macd": macd_line,
        "signal": signal_line,
        "histogram": histogram,
    }


def bollinger_bands(candles, period=20, deviations=2):
    closes = _closes(candles)

    if len(closes) < period:
        return None

    window = closes[-period:]
    middle = sum(window) / period

    variance = sum((x - middle) ** 2 for x in window) / period
    standard_deviation = sqrt(variance)

    return {
        "upper": middle + deviations * standard_deviation,
        "middle": middle,
        "lower": middle - deviations * standard_deviation,
    }


def support_resistance(candles, lookback=50):
    if len(candles) < lookback:
        return None

    recent = candles[-lookback:]

    support = min(float(c["low"]) for c in recent)
    resistance = max(float(c["high"]) for c in recent)

    return {
        "support": support,
        "resistance": resistance,
    }


def calculate_all(candles):
    """
    Calculate the complete NOVA indicator set.
    """

    if not candles:
        return None

    closes = _closes(candles)
    price = closes[-1]

    result = {
        "price": price,
        "ema_20": ema(closes, 20),
        "ema_50": ema(closes, 50),
        "ema_200": ema(closes, 200),
        "rsi_14": rsi(candles, 14),
        "atr_14": atr(candles, 14),
        "macd": macd(candles),
        "bollinger": bollinger_bands(candles),
        "support_resistance": support_resistance(candles),
    }

    return result
