import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image

opts = webdriver.ChromeOptions() 
opts.add_argument('--headless=new')
opts.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(options=opts)
driver.implicitly_wait(30)

def get_latest_feed(username, k=1) :
    assert username != None, "Enter username as a parameter."
    assert k >= 1, "k must be greater than 1."
 
    url = f"https://imgsed.com/{username}"
    resp = requests.get(url)
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    
    feeds = soup.find_all('img', loading="lazy")
    if feeds == None : return None
    
    outputs = []
    for feed in feeds[:k] :
        text = feed.get('alt')
        src = feed.get('src').split('?', maxsplit=1)[-1]
        img = Image.open(requests.get(src, stream=True).raw).convert('RGB')
        outputs.append((text, img))
    
    if len(outputs) == 1 : return outputs[0]
    return outputs

def get_latest_story(username, k=1) :
    assert username != None, "Enter username as a parameter."
    assert k >= 1, "k must be greater than 1."
    
    url = f"https://imgsed.com/stories/{username}"
    driver.get(url)
    
    highlight_selected = driver.find_element(By.CSS_SELECTOR, 'li.swiper-slide-active')
    highlight_selected_name = highlight_selected.find_element(By.TAG_NAME, 'div').text
    if highlight_selected_name != username : return None

    wraps = driver.find_elements(By.CLASS_NAME, 'media')
    if len(wraps) == 0 : return None
    
    outputs = []
    for wrap in list(reversed(wraps))[:k] :
        src = wrap.find_element(By.TAG_NAME, 'img').get_attribute('src').split('?', maxsplit=1)[-1]
        img = Image.open(requests.get(src, stream=True).raw).convert('RGB')
        outputs.append(img)
    
    if len(outputs) == 1 : return outputs[0]
    return outputs

if __name__ == "__main__" :
    get_latest_feed(username='starbucks')    
    get_latest_feed(username='starbucks', k=3)
    
    get_latest_story(username='hipkr_')
    get_latest_story(username='hipkr_', k=3)