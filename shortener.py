# shortening algorithm

import hashlib
import requests

def shorten(link: str):
    """
    Calculates a hash function for a string and returns eight characters
    from the beginning of the received value.
    """
    # ! The algorithm used in this function must be checked out for
    # ! the probability of URL collision when hash calculation for two
    # ! different strings gives the same result 
    return hashlib.sha256(link.encode()).hexdigest()[:8]

def check_availability(url: str):
    try:
        r = requests.get(url)
        r.raise_for_status()
    except:
        return False
    
    return True