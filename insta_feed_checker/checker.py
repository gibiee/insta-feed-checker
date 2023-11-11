import requests

def get_feeds(username: str) -> list :
    """Check the username's latest Instagram feeds up to 12.

    Args:
        username (str): The name of instagram user you want to check.

    Returns:
        list : It will be returned as list containing tuples.
    """
    assert username != None, "Enter username as a parameter."
    
    url = f"https://www.instagram.com/api/v1/users/web_profile_info/?username={username}"
    header = {'Accept': 'application/json', 'User-Agent': "Instagram 219.0.0.12.117 Android"}
    resp = requests.get(url, headers=header)

    posts = resp.json()['data']['user']['edge_owner_to_timeline_media']['edges']
    result = []
    for post in posts :
        img_src = post['node']['display_url']
        text = post['node']['edge_media_to_caption']['edges'][0]['node']['text']
        result.append((img_src, text))
        
    return result

if __name__ == "__main__" :
    username='starbucks'
    
    get_feeds(username='starbucks')

    help(get_feeds)
