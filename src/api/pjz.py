import requests
import json
import csv

class OSINTProjz:
    def __init__(self):
        self.api = "https://www.projz.com/api/"

    def return_objectId(self, link):
        req = requests.post(self.api + "f/v1/parse-share-link", json={
            "link": link
        })

        if req.status_code == 200:
            info = req.json()
            if info['objectType'] == 1:
                req = requests.get(self.api + f"/f/v1/chat/threads/{info['objectId']}")
                if req.status_code == 200:
                    info = req.json()
                    return f"chat-{info['threadId']}", info

            elif info['objectType'] == 4:
                req = requests.get(self.api + f"/f/v1/user/{info['objectId']}")
                if req.status_code == 200:
                    info = req.json()
                    return f"user-{info['socialId']}", info
                else:
                    return 0
                
            elif info['objectType'] == 2:
                req = requests.get(self.api + f"/f/v1/blogs/{info['objectId']}")
                if req.status_code == 200:
                    info = req.json()
                    return f"blog-{info['blogId']}", info
                else:
                    return 0 
                
            elif info['objectType'] == 53:
                req = requests.get(self.api + f"/f/v1/nfts/{info['objectId']}")
                if req.status_code == 200:
                    info = req.json()
                    return f"nft-{info['nftId']}", info
            elif info['objectType'] == 55:
                req = requests.get(self.api + f"/f/v1/stores/0/merch/{info['objectId']}")
                if req.status_code == 200:
                    info = req.json()
                    return f"merch-{info['merchId']}", info
            else:
                return 0
        else:
            return 0
    
