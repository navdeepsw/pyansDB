#!/usr/bin/python3
"""RESTful API client | RZFeeser@alta3.com"""

import requests # required to make API requests

MYAPI = "http://0.0.0.0:2224/"

def main():
    # send http GET request to MYAPI
    resp = requests.get(MYAPI)
    
    # display the HTTP resp code
    print(resp.status_code)
    
    # display text from the resp
    print(resp.text)
    
if __name__ == "__main__":
    main()

