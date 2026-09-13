from pygooglenews import GoogleNews
from config.country_codes import COUNTRY_CODES

gn = GoogleNews()

def _safe_entries(entries, default=5):
    try:
        return int(entries)
    except Exception:
        return default

from pygooglenews import GoogleNews
from config.country_codes import COUNTRY_CODES

gn = GoogleNews()

def _safe_entries(entries, default=5):
    try:
        return int(entries)
    except Exception:
        return default

def get_geo_news(location, entries=5):
    try:
        count = _safe_entries(entries)
        location_key = str(location).strip().lower()
        articles = []

        if location_key in COUNTRY_CODES:
            lang, country = COUNTRY_CODES[location_key]
            local_gn = GoogleNews(lang=lang, country=country)
            headlines = local_gn.top_news()
            feed_title = headlines.get('feed', {}).get('title', '').lower()
            if country.lower() in feed_title or location_key in feed_title:
                articles = headlines.get('entries', [])[:count]

        if not articles:
            headlines = gn.search(f"{location} news")
            articles = headlines.get('entries', [])[:count]

        if not articles:
            return False, f"No news found for {location}."

        result = "\n".join(f"{i}. {a['title']}" for i, a in enumerate(articles, 1))
        return True, result
    except Exception as e:
        return False, f"Couldn't fetch the news: {e}"

def get_topic_news(topic, entries=5):
    try:
        count = _safe_entries(entries)
        topic_clean = str(topic).strip().upper()
        headlines = gn.topic_headlines(topic_clean)
        articles = headlines.get('entries', [])[:count]
        if not articles:
            # Fallback to search if topic is not standard
            headlines = gn.search(topic)
            articles = headlines.get('entries', [])[:count]
        result = "\n".join(f"{i}. {a['title']}" for i, a in enumerate(articles, 1))
        return True, result
    except Exception as e:
        return False, f"Couldn't fetch the news: {e}"

def get_search_news(query, entries=5):
    try:
        count = _safe_entries(entries)
        headlines = gn.search(str(query))
        articles = headlines.get('entries', [])[:count]
        if not articles:
            return False, f"No news found for '{query}'."
        result = "\n".join(f"{i}. {a['title']}" for i, a in enumerate(articles, 1))
        return True, result
    except Exception as e:
        return False, f"Couldn't fetch the news: {e}"

def get_top_headlines(entries=5):
    try:
        count = _safe_entries(entries)
        headlines = gn.top_news()
        articles = headlines.get('entries', [])[:count]
        if not articles:
            return False, "No top headlines found."
        result = "\n".join(f"{i}. {a['title']}" for i, a in enumerate(articles, 1))
        return True, result
    except Exception as e:
        return False, f"Couldn't fetch the news: {e}"
