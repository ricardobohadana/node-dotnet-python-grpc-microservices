# REST API using gRPC <i>http2</i> to communicate with microservices

A containerized Node.js API acting as a client gateway communicating with two independents microservices (a Python and a .NET gRPC servers).

## 🛠️ Open, Run and Test project

This project runs inside a docker network with four distincts docker containers, one for each microservice and the last one for the PostgreSQL database. Steps to run this project:

- Clone the github repository into your local folder
- Have docker installed in your computer
- Open your prefered CLI and navigate to the project's root folder
- Run the command `docker-compose up`
- Wait for all the images and containers to build and finish starting
- Test the local project using Postman or similar app making requests to `http://localhost:81/` as project's base url.

## 💻 Technologies

<div style="padding: 0.5rem">
    <img align="center" height="30" width="40" src="https://grpc.io/img/logos/grpc-icon-color.png">
    gRPC
</div>
<div style="padding: 0.5rem">
    <img align="center" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original.svg">
    Node.js
</div>
<div style="padding: 0.5rem">
    <img align="center" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg">
    Javascript
</div>
<div style="padding: 0.5rem">
    <img align="center" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
    Python
</div>
<div style="padding: 0.5rem">
    <img align="center" height="30" width="40" src="https://vegibit.com/wp-content/uploads/2018/07/JSON-Web-Token-Authentication-With-Node.png">
    JsonWebTokens
</div>
<div style="padding: 0.5rem">
    <img align="center" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/csharp/csharp-original.svg">
    C#
</div>
<div style="padding: 0.5rem">
    <img align="center" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/dotnetcore/dotnetcore-original.svg">
  Microsoft ASP.NET Core
</div>
<div style="padding: 0.5rem">
    <img align="center" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/postgresql/postgresql-original.svg">
PostgreSQL
</div>
<div style="padding: 0.5rem">
    <img align="center" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/1119b9f84c0290e0f0b38982099a2bd027a48bf1/icons/docker/docker-plain-wordmark.svg">
    Docker
</div>

## 🔨 Project Features

The communication only occurs with the Node.js Express API. It has 5 endpoints, three of them to communicate with the authentication gRPC Service, and the other two to communicate to the Stock Market gRPC Service.

- ### Authentication Service (`./user-service/GrpcServer`)

> The authentication service was built using .NET 6 gRPC Server Visual Studio Template. It also uses Entity Framework to map the User's Model to a exclusive PostgreSQL Docker database (only this microservice can access this database).
>
> ### Endpoints:
>
> `POST /user/register`
>
> - Endpoint that communicates with .NET gRPC server to register a new user into PostgreSQL database.
> - Expects the following request body:
>
>   - name: _string_
>   - email: _string_
>   - password: _string_
>   - passwordConfirmation: _string_
>
> - Returns a json with the following propeties:
>
>   - success: _boolean_
>   - message: _string_
>
> `POST /user/login`
>
> - Endpoint that communicates with .NET gRPC server to login a registered user.
> - Expects the following request body:
>
>   - email: _string_
>   - password: _string_
>
> - Returns a json with the following propeties:
>   - token: _boolean_
>   - user: { id: _string_, email: _string_, name: _string_}
>
> `GET /user/:id`
>
> - Endpoint that communicates with .NET gRPC server to get user information by its id. Returns a json with the following propeties:
>
>   - user: { id: _string_, email: _string_, name: _string_}

- ### Stock Market Service (`./asset-service`)

> The stock market service was built using python gRPC module. It uses HTTP requests to yahoo's financial endpoints to retrieve data via pandas-datareader module. The use of this service require the user to be logged in and using a Bearer Type authorization token in request header.
>
> ### Endpoints:
>
> `GET /stock/price/:ticker`
>
> - Endpoint that communicates with python gRPC server to get the latest price of a stock. Returns a json with the following propeties:
>
>   - ticker: _string_
>   - price: _float_
>
> `GET /stock/history/:ticker`
>
> - Endpoint that communicates with python gRPC server to login a registered user. Returns a json with the following propeties:
>
>   - data: {High: _float_, Low: _float_, Open: _float_, Close: _float_, Date: _string_}
