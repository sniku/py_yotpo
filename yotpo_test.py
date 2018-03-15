import requests  # pip install requests

API_KEY = ""  # type API_KEY here
API_SECRET = ""  # type API_SECRET here


class YotpoAPI(object):
    _token = None

    @property
    def token(self):
        if self._token is None:
            self._token = self.auth()
        return self._token

    def auth(self):
        print("Authenticating...")
        url = 'https://api.yotpo.com/oauth/token'
        data = {
            "client_id": API_KEY,
            "client_secret": API_SECRET,
            "grant_type": "client_credentials"
        }

        r = requests.post(url, data=data)
        print("received credentials:", r.json())

        return r.json()['access_token']

    def send_review_request(self):
        url = 'https://api.yotpo.com/apps/{API_KEY}/purchases'.format(API_KEY=API_KEY)

        # test data sent by the yotpo support team.
        data = {
            "validate_data": True,
            "platform": "general",
            "utoken": self.token,
            "email": "client@abc.com",
            "customer_name": "bob",
            "order_id": "order_1",
            "order_date": "2010-10-14",
            "currency_iso": "USD",
            "products": {
                "SKUaaa12": {
                    "url": "http://example_product_url1.com",
                    "name": "product1",
                    "image": "http://images2.fanpop.com/image/photos/13300000/A1.jpg",
                    "description": "this is the description of a product",
                    "price": "100",
                    "specs": {
                        "upc": "USB",
                        "isbn": "thingy"
                    },
                    "product_tags": "book"
                }
            }
        }
        print("POST {}".format(url))

        r = requests.post(url, data=data)

        print("received:")
        print(r.json())

        return r.json()

    def get_orders(self):
        url = 'https://api.yotpo.com/apps/{API_KEY}/purchases?utoken={TOKEN}&count=500'.format(TOKEN=self.token, API_KEY=API_KEY)

        r = requests.get(url)
        # print(r.text)
        return r.json()


############################
# TEST CODE BELOW
############################

api = YotpoAPI()

print("Retrieving orders...")
print("current number of orders:", len(api.get_orders()['response']['purchases']))

print("creating new order...")
api.send_review_request()

#This should print number higher by 1
print("Retrieving orders, expecting one more than previously...")
print("current number of orders:", len(api.get_orders()['response']['purchases']))
