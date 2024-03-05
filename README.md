# inoob_web_forum

This is a website forum where users can discus anything about Tech.

It is inspired by [Stackoverflow](https://stackoverflow.com)

We build this web as implementation of our knowledge after learn web development at [onxp](https://onxp.net)

## Website Spesification

### Name

Inoob (index out of bound)

### Features

- Authentication (Login Register Logout)
- CRU Profile
- CRUD Question
- CRUD Answer
- CRUD Reply (balasan dari jawaban)
- Upvote and Downvote Question
- Upvote dan Downvote Answer
- Category
- Save Question

## How to run this app

### Prerequisite

To run this app, we encourage you to use nix package manager

In case you don't want to use nix package manager, you can run prepare this app in your machine

- git
- podman
- nodejs_20
- python 3.11
- pip
- pdm (python package manager)
- redis
- postgresql

### Steps to run this app

1. Clone this github repository

   ```
   git clone https://github.com/dianprsty/inoob_web_forum.git
   ```

2. Go to inoob_web_forum directory

   ```
   cd inoob_web_forum
   ```

3. Go to nix shell environment

   ```
   nix-shell shell.nix
   ```

4. Install the required python package

   ```
   pdm install
   ```

5. Install the required nodejs package (for tailwind and daisyui)

   ```
   npm install
   ```

6. copy .env.example to .env and set the environment variables

7. Run database migration

   ```
   pdm run src/manage.py migrate
   ```

8. Create Super Admin

   ```
   pdm run src/manage.py createsuperuser
   ```

   follow the steps and insert the required data

9. Run the web app
   ```
   pdm run src/manage.py runserver
   ```
