

This code demonstrates the bug/misconfiguration of my account with Yotpo.

1. I'm able to authenticate, and retrieve orders stored in the system correctly.
2. I'm able to "create purchase" (at least server responds with 'code': 200, 'message': 'OK')
3. Newly created purchase/order is not stored on the server side. When I retrieve all purchases, the newly created order is nowhere to be seen.
4. This situation has persisted over last 4 weeks. My number of purchases is 163, even though I created 50 more purchases over this period of time.

See sample execution of the script below:

```shell
sniku@homedesktop:~/workspace/teklager/yotpo_support_test$ python3 yotpo_test.py 
Retrieving orders...
Authenticating...
received credentials: {'access_token': 'gI5i5MZJYeOeC==redacted==z47e0C20U2OoZbh', 'token_type': 'bearer'}
current number of orders: 163
creating new order...
POST https://api.yotpo.com/apps/r9Gl0DNbH8cHl==redacted==kjgnoEH6v3oN/purchases
received:
{'code': 200, 'message': 'OK', 'uuid': '2e51b117-3c99-4c07-9b8f-65f01fe60d03'}
Retrieving orders, expecting one more than previously...
current number of orders: 163

```