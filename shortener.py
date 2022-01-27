# shortening algorithm

import random, string
import requests

def get_random_scrap(N=5) -> str:
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

def check_availability(url: str):
    try:
        r = requests.get(url)
        r.raise_for_status()
    except:
        return False
    
    return True