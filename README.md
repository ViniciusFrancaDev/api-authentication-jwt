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

#### Products
**HTTP Method**|**URI Path**|**Description**
:--|:--|:--
POST|/api/register|Register new user
POST|/api/login|Login of the user sending `email` and `password` in the request body
GET|/api/user|Get user logged
POST|/api/logout|Logout user

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
