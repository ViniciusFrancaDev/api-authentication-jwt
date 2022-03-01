# API authentication using JWT Tokens
Project that handles API authentication generating JWT token using HttpOnly cookies.

## Requirements
* [Docker desktop](https://www.docker.com/products/docker-desktop)

## Installation
1. Clone the repository

2. Change to the directory was created by the clone

3. Run docker-compose file:
```bash
docker-compose up -d
```

## Usage
The API is available through `http://localhost:8000` with the endpoints:

**HTTP Method**|**URI Path**|**Description**
:--|:--|:--
POST|/api/register|Register new user sending `name`, `email` and `password` in the request body
POST|/api/login|Login of the user sending `email` and `password` in the request body
GET|/api/user|Get user logged using access token as an authorization bearer token
POST|/api/refresh|Refresh access token
POST|/api/logout|Logout user

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
