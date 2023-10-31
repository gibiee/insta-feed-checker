![PyPI - Version](https://img.shields.io/pypi/v/instacrawler?color=red)
![PyPI - Downloads](https://img.shields.io/pypi/dm/instacrawler?color=orange)
![PyPI - License](https://img.shields.io/pypi/l/instacrawler?color=green)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/instacrawler?color=blue)

# Now, it doesn't seem to work because the mirror site has changed.



# instacrawler
**instacrawler** is the fastest and simplest way to check someone's instagram feed/story.
- No instagram account required.
- Available on VM

You can find more detailed information in [Caution](#caution).

**<ins>If it helped you, please give me a star⭐️. Thank you!</ins>**


## Installation
- Python >= 3.7
```bash
pip install --upgrade pip
pip install instacrawler
```

## Quick start
```py
import instacrawler

instacrawler.get_latest_feed(username='starbucks')
# OUTPUT : (text, PIL.Image)

instacrawler.get_latest_story(username='starbucks')
# OUTPUT : PIL.Image
```

## Caution
- This library use the mirror site named [imgsed](https://imgsed.com/). So if the site changes, this may not be worked.
- Due to the nature of the mirror site, it is hard to identify fixed feeds.
- When a new feed/story is posted, it needs time to be reflected.
  - New feed : *maybe* up to 4 hours
  - New Story : *maybe* up to 3 hours