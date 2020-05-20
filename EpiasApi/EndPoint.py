
import requests as Request
from Utils.Errors import ErrorCodes

class _EpiasApi:
    """Dahili class. Lüfen kullanmayınız.
    """
    def __init__(self, authKey):
        self.URL = "https://api.epias.com.tr/epias/exchange"
        self.PATH = "/transparency"
        self.KEY = authKey
    
    def __consumeAPI(self, path, params, list):
        headers = {
                    'x-ibm-client-id': self.KEY,
                    'accept': 'application/json',
                    'cache-control' : 'no-cache'
                  }
        try:
            request = Request.get(self.URL + self.PATH + path, params = params, headers = headers)
            if request.status_code==200:
                if not request.text.startswith("<html>"):
                    result = request.json(encoding="utf-8")
                    if result["resultCode"] == "0":
                        return True, result["body"]
                    else:
                        return False, ErrorCodes[1001]
                else:
                    return False, ErrorCodes[1002]
            else:
                return False, ErrorCodes[request.status_code]

        except Exception as ex:
            print("Hata : %s", ex)
            return False, ex
