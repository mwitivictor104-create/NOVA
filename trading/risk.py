"""
NOVA Risk Analysis

Analysis only.
Calculates:
- Stop loss
- Take profit
- Risk/reward ratio

No trade execution.
"""


def calculate_levels(price, atr, direction, sl_multiplier=1.5, tp_multiplier=3.0):
    """
    Calculate ATR-based SL and TP.

    direction:
        BUY
        SELL
    """

    price = float(price)
    atr = float(atr)
    direction = str(direction).upper()

    if atr <= 0:
        return {
            "success": False,
            "error": "ATR must be greater than zero."
        }

    if direction == "BUY":
        stop_loss = price - (atr * sl_multiplier)
        take_profit = price + (atr * tp_multiplier)

    elif direction == "SELL":
        stop_loss = price + (atr * sl_multiplier)
        take_profit = price - (atr * tp_multiplier)

    else:
        return {
            "success": False,
            "error": "Direction must be BUY or SELL."
        }

    risk_distance = abs(price - stop_loss)
    reward_distance = abs(take_profit - price)

    risk_reward = (
        reward_distance / risk_distance
        if risk_distance > 0
        else None
    )

    return {
        "success": True,
        "direction": direction,
        "entry_reference": price,
        "stop_loss": stop_loss,
        "take_profit": take_profit,
        "risk_distance": risk_distance,
        "reward_distance": reward_distance,
        "risk_reward": risk_reward,
        "analysis_only": True,
        "trade_placed": False
    }
