"""
NOVA Realistic Trading Backtester

Educational/simulation only.
Does NOT place real trades.

Tests NOVA signals candle-by-candle and records:
- BUY / SELL / WAIT
- Entry
- Stop loss
- Take profit
- Win/loss
- P&L in simulated price units
"""

from .signal_engine import analyze_market


class Backtester:
    def __init__(self, candles, starting_balance=10000):
        self.candles = candles
        self.starting_balance = starting_balance
        self.balance = starting_balance
        self.trades = []

    def run(self):
        if len(self.candles) < 60:
            return {
                "error": "At least 60 candles are required.",
                "trades": [],
                "balance": self.balance,
            }

        for i in range(50, len(self.candles) - 1):
            history = self.candles[:i + 1]

            analysis = analyze_market(history)

            if analysis["signal"] == "WAIT":
                continue

            entry = self.candles[i]["close"]
            stop_loss = analysis["stop_loss"]
            take_profit = analysis["take_profit"]

            if stop_loss is None or take_profit is None:
                continue

            result = self._simulate_trade(
                i,
                analysis["signal"],
                entry,
                stop_loss,
                take_profit,
            )

            if result:
                self.trades.append(result)
                self.balance += result["pnl"]

        return self._summary()

    def _simulate_trade(self, index, signal, entry, stop_loss, take_profit):
        for j in range(index + 1, len(self.candles)):
            candle = self.candles[j]

            high = candle["high"]
            low = candle["low"]

            if signal == "BUY":
                # Conservative rule:
                # If both SL and TP occur inside the same candle,
                # assume SL was hit first.
                if low <= stop_loss:
                    return {
                        "signal": signal,
                        "entry": entry,
                        "exit": stop_loss,
                        "stop_loss": stop_loss,
                        "take_profit": take_profit,
                        "result": "LOSS",
                        "pnl": stop_loss - entry,
                        "entry_index": index,
                        "exit_index": j,
                    }

                if high >= take_profit:
                    return {
                        "signal": signal,
                        "entry": entry,
                        "exit": take_profit,
                        "stop_loss": stop_loss,
                        "take_profit": take_profit,
                        "result": "WIN",
                        "pnl": take_profit - entry,
                        "entry_index": index,
                        "exit_index": j,
                    }

            elif signal == "SELL":
                # Conservative rule:
                # If both SL and TP occur inside the same candle,
                # assume SL was hit first.
                if high >= stop_loss:
                    return {
                        "signal": signal,
                        "entry": entry,
                        "exit": stop_loss,
                        "stop_loss": stop_loss,
                        "take_profit": take_profit,
                        "result": "LOSS",
                        "pnl": entry - stop_loss,
                        "entry_index": index,
                        "exit_index": j,
                    }

                if low <= take_profit:
                    return {
                        "signal": signal,
                        "entry": entry,
                        "exit": take_profit,
                        "stop_loss": stop_loss,
                        "take_profit": take_profit,
                        "result": "WIN",
                        "pnl": entry - take_profit,
                        "entry_index": index,
                        "exit_index": j,
                    }

        return None

    def _summary(self):
        wins = sum(1 for t in self.trades if t["result"] == "WIN")
        losses = sum(1 for t in self.trades if t["result"] == "LOSS")

        total = wins + losses

        win_rate = (wins / total * 100) if total else 0

        total_pnl = self.balance - self.starting_balance

        return {
            "starting_balance": self.starting_balance,
            "ending_balance": round(self.balance, 2),
            "total_pnl": round(total_pnl, 2),
            "trades": total,
            "wins": wins,
            "losses": losses,
            "win_rate": round(win_rate, 2),
            "trade_history": self.trades,
        }
