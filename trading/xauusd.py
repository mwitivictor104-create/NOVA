import json
import urllib.request
import urllib.error

from trading.indicators import calculate_all
from trading.signal_engine import analyze_market


class XAUUSDAnalyzer:
    """
    NOVA XAUUSD market analyzer.

    Data source:
        Yahoo Finance GC=F gold futures

    IMPORTANT:
        This is analysis only.
        No trades are placed.
    """

    def __init__(self, timeout=10):
        self.timeout = timeout

    def get_market_data(self):
        url = (
            "https://query1.finance.yahoo.com/v8/finance/chart/"
            "GC=F?range=5d&interval=5m"
        )

        try:
            request = urllib.request.Request(
                url,
                headers={"User-Agent": "Mozilla/5.0"}
            )

            with urllib.request.urlopen(
                request,
                timeout=self.timeout
            ) as response:
                data = json.loads(
                    response.read().decode("utf-8")
                )

            chart = data.get("chart", {})
            results = chart.get("result")

            if not results:
                return {
                    "success": False,
                    "error": "Yahoo returned no chart data",
                    "raw": chart.get("error")
                }

            result = results[0]

            timestamps = result.get("timestamp")
            indicators = result.get("indicators", {})
            quotes = indicators.get("quote", [])

            if not timestamps or not quotes:
                meta = result.get("meta", {})

                price = meta.get("regularMarketPrice")

                if price is not None:
                    return {
                        "success": True,
                        "symbol": "XAUUSD",
                        "source": "Yahoo Finance GC=F",
                        "candles": [],
                        "latest_price": float(price),
                        "warning": (
                            "Current gold price available, "
                            "but historical candles were not returned."
                        )
                    }

                return {
                    "success": False,
                    "error": "No timestamp or candle data returned"
                }

            quote = quotes[0]

            candles = []

            for i, timestamp in enumerate(timestamps):
                try:
                    o = quote["open"][i]
                    h = quote["high"][i]
                    l = quote["low"][i]
                    c = quote["close"][i]

                    if None in (o, h, l, c):
                        continue

                    volume_data = quote.get("volume", [])
                    volume = (
                        volume_data[i]
                        if i < len(volume_data)
                        and volume_data[i] is not None
                        else 0
                    )

                    candles.append({
                        "time": timestamp,
                        "open": float(o),
                        "high": float(h),
                        "low": float(l),
                        "close": float(c),
                        "volume": float(volume)
                    })

                except (KeyError, IndexError, TypeError, ValueError):
                    continue

            if not candles:
                return {
                    "success": False,
                    "error": "No valid OHLC candles were returned"
                }

            return {
                "success": True,
                "symbol": "XAUUSD",
                "source": "Yahoo Finance GC=F",
                "candles": candles,
                "latest_price": candles[-1]["close"]
            }

        except urllib.error.URLError as error:
            return {
                "success": False,
                "error": f"Network error: {error}"
            }

        except Exception as error:
            return {
                "success": False,
                "error": f"Data error: {error}"
            }

    def analyze(self):
        market = self.get_market_data()

        if not market["success"]:
            return market

        candles = market.get("candles", [])

        if len(candles) < 50:
            return {
                "success": False,
                "symbol": "XAUUSD",
                "latest_price": market.get("latest_price"),
                "error": (
                    f"Only {len(candles)} valid candles available. "
                    "At least 50 are required for NOVA's indicators."
                ),
                "source": market.get("source")
            }

        try:
            indicators = calculate_all(candles)
            signal = analyze_market(candles)

            return {
                "success": True,
                "symbol": "XAUUSD",
                "source": market["source"],
                "candles": len(candles),
                "latest_price": candles[-1]["close"],
                "indicators": indicators,
                "analysis": signal
            }

        except Exception as error:
            return {
                "success": False,
                "symbol": "XAUUSD",
                "error": f"Analysis error: {error}"
            }


def analyze_xauusd():
    analyzer = XAUUSDAnalyzer()
    return analyzer.analyze()


if __name__ == "__main__":
    result = analyze_xauusd()
    print(json.dumps(result, indent=2))
