# Not yet available. (developing now)

**instacrawler** is the fastest way to check someone's instagram feed/story.
- No instagram account required.
- Available on VM

If you want to see the detail, please check [Caution](#caution).

## Installation
```bash
pip install instacrawler
```

## Quickstart
```py
import instacrwaler

feed = instacrwaler.get_latest_feed(username='')

story = instacrwaler.get_latest_story(username='')
```

## Caution
- It use the mirror site named [imgsed](https://imgsed.com/). So if the site changes, it may not work.
- When a new feed/story is posted, it needs time to be reflected. (about ???)
