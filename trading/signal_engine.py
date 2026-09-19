"""
NOVA Realistic Trading Signal Engine

Analysis only.
NO trades are placed.

Features:
- EMA trend
- RSI momentum
- MACD confirmation
- Bollinger Bands
- ATR volatility
- Support/resistance
- Bullish/bearish scoring
- Conflict detection
- Signal strength
- ATR-based SL/TP
"""


from .indicators import calculate_all


def _add_reason(reasons, text):
    if text not in reasons:
        reasons.append(text)


def analyze_market(candles):

    if not candles or len(candles) < 50:
        return {
            "signal": "WAIT",
            "strength": "INSUFFICIENT DATA",
            "confidence": 0,
            "reason": (
                "Not enough candle data. "
                "At least 50 candles are required."
            ),
        }

    data = calculate_all(candles)

    if not data:
        return {
            "signal": "WAIT",
            "strength": "NO DATA",
            "confidence": 0,
            "reason": "Indicators could not be calculated.",
        }

    price = data["price"]
    ema20 = data["ema_20"]
    ema50 = data["ema_50"]
    ema200 = data["ema_200"]
    rsi = data["rsi_14"]
    atr = data["atr_14"]
    macd = data["macd"]
    bb = data["bollinger"]
    sr = data["support_resistance"]

    buy_score = 0
    sell_score = 0

    buy_reasons = []
    sell_reasons = []
    neutral_reasons = []

    # -------------------------------------------------
    # EMA20 / EMA50 TREND
    # -------------------------------------------------

    if ema20 is not None and ema50 is not None:

        ema_difference = abs(ema20 - ema50)

        if ema20 > ema50:
            buy_score += 20
            _add_reason(
                buy_reasons,
                "EMA20 is above EMA50"
            )

            if ema_difference < (atr * 0.10 if atr else 0):
                buy_score -= 5
                _add_reason(
                    neutral_reasons,
                    "EMA20/EMA50 separation is very small"
                )

        elif ema20 < ema50:
            sell_score += 20
            _add_reason(
                sell_reasons,
                "EMA20 is below EMA50"
            )

            if ema_difference < (atr * 0.10 if atr else 0):
                sell_score -= 5
                _add_reason(
                    neutral_reasons,
                    "EMA20/EMA50 separation is very small"
                )

    # -------------------------------------------------
    # EMA200 LONGER-TERM TREND
    # -------------------------------------------------

    if ema200 is not None:

        if price > ema200:
            buy_score += 20
            _add_reason(
                buy_reasons,
                "Price is above EMA200"
            )

        elif price < ema200:
            sell_score += 20
            _add_reason(
                sell_reasons,
                "Price is below EMA200"
            )

    # -------------------------------------------------
    # RSI MOMENTUM
    # -------------------------------------------------

    if rsi is not None:

        if 50 < rsi < 70:
            buy_score += 15
            _add_reason(
                buy_reasons,
                "RSI supports bullish momentum"
            )

        elif 30 < rsi < 50:
            sell_score += 15
            _add_reason(
                sell_reasons,
                "RSI supports bearish momentum"
            )

        elif rsi >= 70:
            _add_reason(
                neutral_reasons,
                "RSI is overbought"
            )

        elif rsi <= 30:
            _add_reason(
                neutral_reasons,
                "RSI is oversold"
            )

    # -------------------------------------------------
    # MACD
    # -------------------------------------------------

    if macd is not None:

        histogram = macd.get("histogram", 0)

        if histogram > 0:
            buy_score += 20
            _add_reason(
                buy_reasons,
                "MACD histogram is positive"
            )

        elif histogram < 0:
            sell_score += 20
            _add_reason(
                sell_reasons,
                "MACD histogram is negative"
            )

    # -------------------------------------------------
    # BOLLINGER BANDS
    # -------------------------------------------------

    if bb is not None:

        middle = bb["middle"]

        if price > middle:
            buy_score += 10
            _add_reason(
                buy_reasons,
                "Price is above Bollinger middle band"
            )

        elif price < middle:
            sell_score += 10
            _add_reason(
                sell_reasons,
                "Price is below Bollinger middle band"
            )

    # -------------------------------------------------
    # SUPPORT / RESISTANCE
    # -------------------------------------------------

    if sr is not None:

        support = sr["support"]
        resistance = sr["resistance"]

        if price > resistance:
            buy_score += 10
            _add_reason(
                buy_reasons,
                "Price is above recent resistance"
            )

        elif price < support:
            sell_score += 10
            _add_reason(
                sell_reasons,
                "Price is below recent support"
            )

    # -------------------------------------------------
    # SCORE LIMITS
    # -------------------------------------------------

    buy_score = max(0, min(buy_score, 100))
    sell_score = max(0, min(sell_score, 100))

    # -------------------------------------------------
    # CONFLICT DETECTION
    # -------------------------------------------------

    score_difference = abs(buy_score - sell_score)

    conflict = (
        buy_score >= 40
        and sell_score >= 40
        and score_difference < 20
    )

    # -------------------------------------------------
    # SIGNAL
    # -------------------------------------------------

    if conflict:

        signal = "WAIT"
        strength = "CONFLICTED"
        confidence = max(buy_score, sell_score)

        _add_reason(
            neutral_reasons,
            "Bullish and bearish indicators are too closely matched"
        )

    elif buy_score >= 80 and buy_score > sell_score:

        signal = "BUY"
        strength = "STRONG"
        confidence = buy_score

    elif buy_score >= 60 and buy_score > sell_score:

        signal = "BUY"
        strength = "MODERATE"
        confidence = buy_score

    elif sell_score >= 80 and sell_score > buy_score:

        signal = "SELL"
        strength = "STRONG"
        confidence = sell_score

    elif sell_score >= 60 and sell_score > buy_score:

        signal = "SELL"
        strength = "MODERATE"
        confidence = sell_score

    else:

        signal = "WAIT"
        strength = "WEAK"
        confidence = max(buy_score, sell_score)

    # -------------------------------------------------
    # ATR RISK LEVELS
    # -------------------------------------------------

    stop_loss = None
    take_profit = None

    if atr is not None:

        if signal == "BUY":

            stop_loss = price - (atr * 1.5)
            take_profit = price + (atr * 3.0)

        elif signal == "SELL":

            stop_loss = price + (atr * 1.5)
            take_profit = price - (atr * 3.0)

    # -------------------------------------------------
    # COMBINED REASONS
    # -------------------------------------------------

    reasons = []

    if signal == "BUY":
        reasons.extend(buy_reasons)

    elif signal == "SELL":
        reasons.extend(sell_reasons)

    reasons.extend(neutral_reasons)

    # -------------------------------------------------
    # RESULT
    # -------------------------------------------------

    return {
        "signal": signal,
        "strength": strength,
        "confidence": round(confidence, 2),

        "price": price,

        "buy_score": buy_score,
        "sell_score": sell_score,
        "score_difference": round(score_difference, 2),

        "conflict": conflict,

        "rsi": rsi,
        "atr": atr,

        "ema20": ema20,
        "ema50": ema50,
        "ema200": ema200,

        "macd": macd,
        "bollinger": bb,
        "support_resistance": sr,

        "stop_loss": stop_loss,
        "take_profit": take_profit,

        "buy_reasons": buy_reasons,
        "sell_reasons": sell_reasons,
        "reasons": reasons,

        "analysis_only": True,
        "trade_placed": False,
    }
