import json
import urllib.request
import urllib.error


class LiveMarket:
    """
    Live market-data client for NOVA.

    This module only retrieves market data.
    It does NOT place, modify, or close trades.
    """

    def __init__(self, timeout=10):
        self.timeout = timeout

    def get_price(self, symbol):
        """
        Retrieve a current price from a public market-data endpoint.

        Example:
            BTCUSDT
        """
        symbol = symbol.upper().strip()

        url = (
            "https://api.binance.com/api/v3/ticker/price"
            f"?symbol={symbol}"
        )

        try:
            request = urllib.request.Request(
                url,
                headers={"User-Agent": "NOVA-AI/1.0"}
            )

            with urllib.request.urlopen(
                request,
                timeout=self.timeout
            ) as response:
                data = json.loads(response.read().decode("utf-8"))

            if "price" not in data:
                return {
                    "success": False,
                    "error": "Price not found",
                    "data": data
                }

            return {
                "success": True,
                "symbol": symbol,
                "price": float(data["price"])
            }

        except urllib.error.URLError as error:
            return {
                "success": False,
                "error": f"Network error: {error}"
            }

        except Exception as error:
            return {
                "success": False,
                "error": str(error)
            }


def get_live_price(symbol):
    market = LiveMarket()
    return market.get_price(symbol)


if __name__ == "__main__":
    result = get_live_price("BTCUSDT")
    print(json.dumps(result, indent=2))
