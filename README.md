# [Django React Soft Dashboard](https://appseed.us/product/django-react-soft-dashboard)

Start your Development with an Innovative Admin Template for **Material-UI** and **React**. [Soft UI Dashboard React](https://appseed.us/product/django-react-soft-dashboard) is built with over 70 frontend individual elements, like buttons, inputs, navbars, nav tabs, cards, or alerts, giving you the freedom of choosing and combining. The product comes with a simple JWT authentication flow: login/register/logout. 

> Features

- Innovative Material-UI Design - Creafted by [Creative-Tim](https://bit.ly/3fKQZaL)
- React, Redux, Redux-persist
- Authentication: JWT Login/Register/Logout
- **Full-stack Ready** using a **Django API Server** (open-source project) - Server Features
  - Django / DRF / SQLite3 - a simple, easy to use backend
  - Authentication with JWT (login, logout, register)
  - Docker, Unitary tests

> Links

- [Django React Soft Dashboard](https://appseed.us/product/django-react-soft-dashboard) - product page
- [Django React Soft Dashboard](https://django-react-soft-dashboard.appseed-srv1.com/authentication/sign-in) - LIVE Demo
- Download Backend: [Django API Server 📥](https://github.com/app-generator/api-server-django/archive/refs/heads/main.zip)
- Donwnload Frontend: [React Soft Dashboard 📥](https://github.com/app-generator/react-soft-ui-dashboard/archive/refs/heads/main.zip)  
* Free Support via Github (issues tracker) and [Discord](https://discord.gg/fZC6hup).
* Related Products:
  - Node JS API Backend - [Node React Soft Dashboard](https://appseed.us/product/node-js-react-soft-dashboard) - `open-source` project

<br >

![React Soft Dashboard - Open-source full-stack product with Django API Backend.](https://user-images.githubusercontent.com/51070104/136687466-1dfeeb6b-d474-45df-879b-0857b27eb615.gif) 

<br >

> **Note**: This product can be used with other API Servers for a complete fullstack experience. **ALL API servers use an unified interface**

- [Flask API Server](https://github.com/app-generator/api-server-flask) - open-source product
- [Node JS API Server](https://github.com/app-generator/api-server-nodejs) - open-source product / Typescript / SQLite / TypeORM / Joy for validation
- [Node JS API Server PRO](https://github.com/app-generator/api-server-nodejs-pro) - **commercial product**
    - SQLite / TypeORM / Joy / Docker
    - MongoDB / Mongoose / Joy Docker (separate branch, same project)

<br />

## Start Django API Server

Simple starter built with Python / DRF Library / Sqlite3 and JWT Auth. The authentication flow is based on [json web tokens](https://jwt.io).

<br />

> How to use the code

**Step #1** -  Clone the sources

```bash
$ git clone https://github.com/app-generator/api-server-django.git
$ cd api-server-django
```

**Step #2** - Create a virtual environment

```bash
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
```

**Step #3** - Install dependencies using PIP

```bash
$ pip install -r requirements.txt
```

**Step #4** - Start the API server

```bash
$ python manage.py migrate
$ python manage.py runserver 5000
```

The API server will start using the explicit port `5000`.

<br />

## Start React UI 

To use the product Node JS (>= 12.x) is required and GIT to clone/download the project from the public repository.

**Step #1** - Clone the project

```bash
$ git clone https://github.com/app-generator/react-soft-ui-dashboard.git
$ cd react-soft-ui-dashboard
```

<br >

**Step #2** - Install dependencies via NPM or yarn

```bash
$ npm i
// OR
$ yarn
```

<br />

**Step #3** - Start in development mode

```bash
$ npm run start 
// OR
$ yarn start
```

<br />

## Configure the backend server

The product comes with a usable JWT Authentication flow that provides only the basic requests: login/logout/register. 

**API Server URL** - `src/config/constant.js` 

```javascript
const config = {
    ...
    API_SERVER: 'http://localhost:5000/api/'  // <-- The magic line
};
```

<br />

**API Server Descriptor** - POSTMAN Collection

The backend server uses an [Unified API defition](https://docs.appseed.us/boilerplate-code/api-server/api-unified-definition) maintained and actively supported by AppSeed across multiple frameworks: Flask, Node JS, FastAPI.

- [API POSTMAN Collection](https://github.com/app-generator/api-unified-definition/blob/main/api.postman_collection.json) - can be used to mock (simulate) the backend server or code a new one in your preferred framework. 

<br />

---
[Django React Soft Dashboard](https://appseed.us/product/django-react-soft-dashboard) - Provided by **AppSeed [App Generator](https://appseed.us/app-generator)**.
