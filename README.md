![PyPI - Downloads](https://img.shields.io/pypi/dm/instacrawler)
![PyPI - License](https://img.shields.io/pypi/l/instacrawler?color=blue)

**instacrawler** is the fastest way to check someone's instagram feed/story.
- No instagram account required.
- Available on VM

If it helped you, please give a github star⭐️. Thank you!
If you want to see the detail, please check [Caution](#caution).

## Installation
```bash
# Python > 3.6
pip install instacrawler
```

## Quick start
```py
import instacrawler

latest_feed = instacrawler.get_latest_feed(username='starbuckskorea')
# OUTPUT : (text, PIL.image)

latest_story = instacrawler.get_latest_story(username='starbuckskorea')
# OUTPUT : PIL.image
```

## Caution
- It use the mirror site named [imgsed](https://imgsed.com/). So if the site changes, it may not work.
- Due to the nature of the mirror site, it is hard to identify fixed feeds.
- When a new feed/story is posted, it needs time to be reflected. (about ???)
