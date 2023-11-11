![PyPI - Version](https://img.shields.io/pypi/v/insta-feed-checker?color=red)
![PyPI - Downloads](https://img.shields.io/pypi/dm/insta-feed-checker?color=orange)
![PyPI - License](https://img.shields.io/pypi/l/insta-feed-checker?color=green)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/insta-feed-checker?color=blue)

# Instagram Feed Checker
This is the fastest and simplest way to check someone's instagram feeds.
- Free.
- Not required your instagram account.
- Instagram defends the use of web scraping tools in VM. But, this library can be used in VM.

**<ins>If it helped you, please give me a star⭐️. Thank you!</ins>**

## Quick start
- Python >= 3.6
```bash
pip install --upgrade pip
pip install insta_feed_checker
```

```py
import insta_feed_checker

insta_feed_checker.get_feeds(username='starbucks')
# It will be returned pairs of url(image src) and caption as [(text, text), (text, text), ...]
```

## Caution
**This library is free, so it has some constraints.**
- You can only get up to 12 Instagram latest feeds.
- If you repeat the call in a short time, you may get ***blocked***.
  - `JSONDecodeError: Expecting value: line 1 column 1 (char 0)` means you are blocked.
  - If you are blocked, it will be released after some time.
  - When I tested it, even if I request once every 10 minutes, I was blocked around the 40th time.