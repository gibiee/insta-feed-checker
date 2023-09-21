import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image

opts = webdriver.ChromeOptions() 
opts.add_argument('--headless=new')

driver = webdriver.Chrome(options=opts)
driver.implicitly_wait(30)

def get_latest_feed(username, several=False) :
    assert username != None, "Enter username as a parameter."
 
    url = f"https://imgsed.com/{username}"
    resp = requests.get(url)
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    
    feed = soup.find('img', loading="lazy")
    if feed == None : return None
    text = feed.get('alt')
    src = feed.get('src').split('?', maxsplit=1)[-1]
    img = Image.open(requests.get(src, stream=True).raw).convert('RGB')
    return text, img

def get_latest_story(username, highlight=None, several=False) :
    assert username != None, "Enter username as a parameter."
    
    url = f"https://imgsed.com/stories/{username}"
    driver.get(url)
    
    if highlight == None :
        highlight = url.strip('/').split('/')[-1]
    
    highlight_selected = driver.find_element(By.CSS_SELECTOR, 'li.active')
    highlight_selected_name = highlight_selected.find_element(By.TAG_NAME, 'div').text
    if highlight_selected_name != highlight : return None

    wraps = driver.find_elements(By.CLASS_NAME, 'media')
    if len(wraps) == 0 : return None
    wrap = wraps[-1]
    src = wrap.find_element(By.TAG_NAME, 'img').get_attribute('src').split('?', maxsplit=1)[-1]
    img = Image.open(requests.get(src, stream=True).raw).convert('RGB')
    return img
