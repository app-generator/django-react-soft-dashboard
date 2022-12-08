# [React Soft Dashboard](https://appseed.us/product/soft-ui-dashboard/api-server-django/react/) - `Django API`

Start your Development with an Innovative Admin Template for **Material-UI** and **React**. [Soft UI Dashboard React](https://appseed.us/product/soft-ui-dashboard/api-server-django/react/) is built with over 70 frontend individual elements, like buttons, inputs, navbars, nav tabs, cards, or alerts, giving you the freedom of choosing and combining. The product comes with a simple JWT authentication flow: login/register/logout. 

- 👉 [Django React Soft Dashboard](https://appseed.us/product/soft-ui-dashboard/api-server-django/react/) - product page
- 👉 [Django React Soft Dashboard](https://django-react-soft-dashboard.appseed-srv1.com/authentication/sign-in) - LIVE Demo

<br>

> Features

- ✅ Innovative `Material-UI Design` - Creafted by [Creative-Tim](https://bit.ly/3fKQZaL)
- ✅ React, Redux, Redux-persist
- ✅ Authentication: JWT Login/Register/Logout
- ✅ **Full-stack Ready** using a **Django API Server** (open-source project) - Server Features
  - Django / DRF / SQLite3 - a simple, easy to use backend
  - Authentication with JWT (login, logout, register)
  - Docker, Unitary tests
  
<br />

![React Soft Dashboard - Open-source full-stack product](https://user-images.githubusercontent.com/51070104/176936814-74386559-4e05-43d5-b9a4-8f70ce96a610.png)

<br />

> React UI Tests:

| NodeJS | NPM | YARN | Status | 
| --- | --- | --- | --- | 
| `v16.13.0` | `v8.1.0`   | `v1.22.5` | ✔️ | 
| `v14.15.0` | `v6.14.8`  | `v1.22.5` | ✔️ |
| `v12.22.0` | `v6.14.11` | `v1.22.5` | ✔️ |

<br />

## ✨ Quick-start 

> 👉 **Start the [Django API](./django-api)** using `Docker`

```bash
$ cd django-api
$ docker-compose up --build  
```

At this point, the API should be up & running at `http://localhost:5000`, and we can test the interface using POSTMAN or `curl`.

<br />

> 👉 **Start the [React UI](./react-ui)** (using another terminal)

```bash
$ cd react-ui
$ yarn         # install dependencies
$ yarn start   # start the app 
```

Once all the above commands are executed, the `React UI` should be visible in the browser. By default, the app redirects the guest users to authenticate. 
After we register a new user and Sign IN, all the private pages become accessible. 

<br />

![React Soft Dashboard - Open-source full-stack product with Django API Backend.](https://user-images.githubusercontent.com/51070104/136687466-1dfeeb6b-d474-45df-879b-0857b27eb615.gif) 

<br >

## ✨ General Information

The product is built using a `two-tier` pattern where the React frontend is decoupled logically and physically from the API backend. How to use the product: 

- `Compile and start` the **Django API Backend**
  - by default the server starts on port `5000`
- `Compile and start` the **React UI**
  - UI will start on port `3000` and expects a running backend on port `5000`
- `Configuration` (Optional)
  - Change the API port
  - Configure the API port used by the React UI to communicate with the backend 

<br />

## ✨ Manual build

### **Start the Django API** 

Simple starter built with Python / DRF Library / Sqlite3 and JWT Auth. The authentication flow is based on [json web tokens](https://jwt.io).

<br />

> 👉 **Step #1** -  Change the directory to `django-api`

```bash
$ cd django-api
```

<br />

> 👉 **Step #2** - Create a virtual environment

```bash
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
```

<br />

> 👉 **Step #3** - Install dependencies using PIP

```bash
$ pip install -r requirements.txt
```

<br />

> 👉 **Step #4** - Create a new `.env` file using sample `env.sample`

The meaning of each variable can be found below: 

- `DEBUG`: if `True` the app runs in develoment mode
  - For production value `False` should be used
- `SECRET_KEY`: used in assets management

<br />

> 👉 **Step #5** - Start the API server

```bash
$ python manage.py migrate
$ python manage.py runserver 5000
```

The API server will start using the explicit port `5000`.

<br />

### Compile & start the **React UI**

```bash
$ cd react-ui
$
$ # Install Modules
$ yarn
$
$ # Start for development (LIVE Reload)
$ yarn start 
```

<br />

### Configuration (Optional)

> Change the port exposed by the Djago API

```bash
$ python manage.py runserver 5000
```

Now, the API will start on port `5000`. 

<br />

> Update the API port used by the React Frontend

**API Server URL** - `src/config/constant.js` 

```javascript
    API_SERVER: 'http://localhost:5001/api/'  // <-- The magic line
```

The value can be updated during the build using the environment

```bash
$ export REACT_APP_BACKEND_SERVER='http://localhost:5001/api/' # Unix/MacOS
$ set REACT_APP_BACKEND_SERVER='http://localhost:5001/api/'    # Windows CMD
$ $env:REACT_APP_BACKEND_SERVER='http://localhost:5001/api/'   # Windows PowerShell
```

<br />

## ✨ API

For a fast set up, use this POSTMAN file: [api_sample](https://github.com/app-generator/api-server-unified/blob/main/api.postman_collection.json)

> 👉 **Register** - `api/users/register` (**POST** request)

```
POST api/users/register
Content-Type: application/json

{
    "username":"test",
    "password":"pass", 
    "email":"test@appseed.us"
}
```

<br />

> 👉 **Login** - `api/users/login` (**POST** request)

```
POST /api/users/login
Content-Type: application/json

{
    "password":"pass", 
    "email":"test@appseed.us"
}
```

<br />

> 👉 **Logout** - `api/users/logout` (**POST** request)

```
POST api/users/logout
Content-Type: application/json
authorization: JWT_TOKEN (returned by Login request)

{
    "token":"JWT_TOKEN"
}
```

<br />

## ✨ Product UI

> **Django React Soft UI Dashboard** - Login 

![Django React Soft UI Dashboard - Login.](https://user-images.githubusercontent.com/51070104/142403942-3a2228e6-c769-4259-8e78-c000056db7c4.png)

<br />

> **Django React Soft UI Dashboard** - User Profile

![Django React Soft UI Dashboard - User Profile](https://user-images.githubusercontent.com/51070104/142403992-81e86dc5-4d73-4cca-8a1b-300a0f5475a0.png)

<br />

> **Django React Soft UI Dashboard** - Billing Page

![Django React Soft UI Dashboard - Billing Page.](https://user-images.githubusercontent.com/51070104/142404073-68b96008-fb06-4ff5-98cf-c8e3eca636c9.png)

<br />

## Links & Resources

- Ask for [Support](https://appseed.us/support) on [Discord](https://discord.gg/fZC6hup)
- See for [React Starters](https://appseed.us/apps/react) - index provided by AppSeed

<br />

---
[Django React Soft Dashboard](https://appseed.us/product/soft-ui-dashboard/api-server-django/react/) - Provided by **[App Generator](https://appseed.us/app-generator)**.
