# Fast API Documentation
This is the API documentation for the Fast Django Application

## Overview
Fast’s API is a JSON-based API built using a lightweight API framework called Restless.

## Creating and Authenticating Users
### Creating Users
Noob or Elite Users can be created using a post request to the **register/** url to create a client account. The data must be in Json format and should contain the username and password, is_noob and is_elite and main currency. The password must be a minimum of 8 and can contain characters and digits. The password must not be similar to the username. Is_noob and Is_elite determine the type of user and are boolean values

Example:

    {"username": "dannywalter", "password": "lily7543", "is_nooob": True, "is_elite": False}

Creating an Admin user only requires the username and password data to be posted to **api/admin/**. Only Superusers can create these accounts. Other users will receive a response Unauthorized with status code 401

### Login Users
Users can login in by sending a POST request with the username and password to **api/admin/**.

You will receive a response with a status code of 200 and user data in JSON format like this

    {
        'id': 'id',
        'username': 'username',
        'is_superuser': 'is_superuser',
        'is_noob': 'is_noob',
        'is_elite': 'is_elite',
    }

### Users List
Superusers(Admin) users can receive a list of all users GET request to **api/admin/**

You will receive a response with a status code of 200 and user data in JSON format like this

    {"objects": [{"id": 1, "username": "james", "is_superuser": false, "is_noob": true, "is_elite": false}, {"id": 2, "username": "admin", "is_superuser": true, "is_noob": false, "is_elite": false}]}

### Users Info
Superusers(Admin) users can receive a specific users info by sending a GET request to **api/admin/** with the user's id as an argument

You will receive a response with a status code of 200 and user data in JSON format like this

    {"id": 1, "admin_username": "james", "is_admin": false, "is_noob": true, "is_elite": false}   

Users can receive their info by sending a  `GET` request with their id as an argument  like `/api/client/<pk>/`

## Wallet
### Funding and Withdrawing Wallets
Clients can fund their wallets using a POST request to `api/wallet/fund/`. A response will be received like this:
    {
        'id': '1',
        'amount': '10000',
        'currency': 'USD', 
    }
Noob Users can only fund accounts in their main currency. Funding in other currencies will be converted and updated. Elite Users can fund accounts in any of the following currencies.

Withdrawing From Wallets is the same process but made to `api/wallet/withdraw/`

### View Wallets
Noob or Elite users can sending a `GET` request to `api/wallet/fund/` to view all their wallets. The response will look this way:
    
    {"objects": [{"id": 1, "amount": 12000, "currency": "USD"}, {"id": 2, "amount": 1200, "currency": "CAD",}]}

## Errors
Regardless of the error type, the exception’s message will get serialized into the response under the "error" key. 

Example:

    {
        "error": "Whatever."
    }

The two major errors are Unauthorized(status code = 401, happens due to the user not being authorized to perform that action) and BadRequest(status code = 400) and also The foundational HTTP-related error(status code = 500).

