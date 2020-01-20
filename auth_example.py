import requests
from requests.exceptions import Timeout, HTTPError
import json


class OT_example: 
    def __init__(self, username: str, password: str, mid: int, token_url: str, api_url) -> None:
        self.username=username
        self.password = password
        self.mid = mid
        self.token_url = token_url
        self.api_url=api_url

        self.token = ""    
    
    def auth(self) -> bool:
        try:
            response = requests.post(self.token_url, data={'grant_type': "password", 'username':self.username, 'password':self.password, 'client_id':str(self.mid)}, timeout=10)
            response.raise_for_status()
        # check exceptions
        except Timeout:
            print("The request timed out")
            return False
        except HTTPError as http_err:
            print("HTTP error occurred: " + str(http_err))
            return False
        except Exception as err:
            print("Error occurred: " + str(err))
            return False
        else:
            print("Success!")
            # parse response and store token
            self.token = json.loads(response.text)["access_token"]
            print("access_token: " + str(self.token))
            return True
    
    def get_all_devices(self) -> None:
        # call get_all_devices function 
        try:
            all_devices = requests.get(self.api_url + "/otdevice/getall?token={}".format(self.token), headers={'accept': 'application/json', 'mid': str(self.mid)}, timeout=10)
        # check exceptions
        except Timeout:
            print("The request timed out")
            return False
        except HTTPError as http_err:
            print("HTTP error occurred: " + str(http_err))
            return False
        except Exception as err:
            print("Other error occurred: " + str(err))
            return False
        else:
            print("Success!")
            print("All Devices: \n" + str(all_devices.text))    


def main():
    # Insert Credentials and correct URLs
    username="USERNAME"
    password = "PASSWORD"
    mid = 50
    token_url = "TOKEN_URL"
    api_url = "API_URL"
    ot = OT_example(username=username, password=password, mid=mid, token_url=token_url, api_url=api_url)
    
    if(ot.auth()):
        ot.get_all_devices()

main()
