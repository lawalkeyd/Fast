# Fast API Documentation
This is the API documentation for the Fast Django Application

## Overview
Fast’s API is a JSON-based API built using the Djangorestframework.

## Creating and Authenticating Users
### Creating Users
Noob or Elite Users can be created using a post request to the **register/** url to create a client account. The data must be in Json format and should contain the username and password, is_noob and is_elite and main currency. The password must be a minimum of 8 and can contain characters and digits. The password must not be similar to the username. Is_noob and Is_elite determine the type of user and are boolean values

Example:

    {"username": "dannywalter", "password": "lily7543", "is_nooob": True, "is_elite": False}


### Login Users
Users can login in by sending a POST request with the username and password to **api/admin/**.

        {
        'username': 'username',
        'password': 'james2234'
        }

You will receive a response with a status code of 200 and the user token as data

    {
        'token': 'ft67y7ggngftf76666',
    }

### Users List
Superusers(Admin) users can receive a list of all users GET request to **user/admin/**

You will receive a response with a status code of 200 and user data in JSON format like this

    {"objects": [{"id": 1, "username": "james", "is_superuser": false, "is_noob": true, "is_elite": false, "main_currency": "USD"}, {"id": 2, "username": "admin", "is_superuser": true, "is_noob": false, "is_elite": false}]}

### Users Info
Superusers(Admin) users can receive a specific users info by sending a GET request to **user/admin/<id>** with the user's id as an argument

You will receive a response with a status code of 200 and user data in JSON format like this

    {"id": 1, "admin_username": "james", "is_admin": false, "is_noob": true, "is_elite": false, "main_currency": "USD"}   

Users can receive their info by sending a  `GET` request with their id as an argument  like `/api/client/<pk>/`

## Wallet
### Funding and Withdrawing Wallets
Clients can fund their wallets using a POST request to `/client/fund/`. A response will be received with a status code of 200 like this:
    {
        'user': '1',
        'amount': '10000',
        'currency': 'USD', 
    }
Noob Users can only fund accounts in their main currency. Funding in other currencies will be converted and updated. Elite Users can fund accounts in any of the following currencies.

Withdrawing From Wallets is the same process but made to `client/withdraw/`

Users can view their wallets by sending a GET request to `client/list`

Admin can view all wallets by sending a GET request to `wallet/list/` and can update user wallets by sending requests to `wallet/admin/<pk>`

### View Wallets
Noob or Elite users can sending a `GET` request to `wallet/list/` to view all their wallets. The response will look this way:
    
    {"objects": [{"user": 1, "amount": 12000, "currency": "USD"}, {"user": 2, "amount": 1200, "currency": "CAD",}]}

## Errors
Regardless of the error type, the exception’s message will get serialized into the response under the "error" key. 

Example:

    {
        "error": "Whatever."
    }

The two major errors are Unauthorized(status code = 401, happens due to the user not being authorized to perform that action) and BadRequest(status code = 400) and also The foundational HTTP-related error(status code = 500).


