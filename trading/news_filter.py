"""
NOVA News Filter

Analysis only.

Flags potentially high-impact economic news periods.
This module does NOT place, modify, or close trades.
"""

from datetime import datetime, timezone


HIGH_IMPACT_KEYWORDS = [
    "fed",
    "federal reserve",
    "fomc",
    "interest rate",
    "rate decision",
    "nonfarm payroll",
    "non-farm payroll",
    "nfp",
    "consumer price index",
    "cpi",
    "producer price index",
    "ppi",
    "inflation",
    "unemployment",
    "jobs report",
    "powell",
]


def normalize_event(event):
    """Convert a news event into a consistent dictionary."""

    if isinstance(event, str):
        return {
            "title": event,
            "time": None,
            "impact": "UNKNOWN"
        }

    if isinstance(event, dict):
        return {
            "title": str(event.get("title", "")),
            "time": event.get("time"),
            "impact": str(
                event.get("impact", "UNKNOWN")
            ).upper()
        }

    return {
        "title": "",
        "time": None,
        "impact": "UNKNOWN"
    }


def is_high_impact(event):
    """Check whether an event appears high impact."""

    item = normalize_event(event)

    title = item["title"].lower()
    impact = item["impact"]

    if impact in ("HIGH", "3"):
        return True

    return any(
        keyword in title
        for keyword in HIGH_IMPACT_KEYWORDS
    )


def analyze_news(events=None):
    """
    Analyze supplied news events.

    No external news request is made here.
    """

    if events is None:
        events = []

    high_impact = []

    for event in events:
        if is_high_impact(event):
            high_impact.append(
                normalize_event(event)
            )

    if high_impact:
        status = "NEWS_RISK"
        allow_analysis = False
    else:
        status = "CLEAR"
        allow_analysis = True

    return {
        "success": True,
        "status": status,
        "high_impact_events": high_impact,
        "high_impact_count": len(high_impact),
        "allow_analysis": allow_analysis,
        "analysis_only": True,
        "trade_placed": False
    }


def current_news_status():
    """
    Return a conservative default when no live
    news feed has been connected.
    """

    now = datetime.now(timezone.utc)

    return {
        "success": True,
        "status": "UNKNOWN",
        "reason": "No live news feed connected.",
        "checked_at": now.isoformat(),
        "allow_analysis": False,
        "analysis_only": True,
        "trade_placed": False
    }
