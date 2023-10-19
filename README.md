# Simple Interface for Image generation through Telegram bot

This is a simple repo that you can use in anyway you like - take parts of it or the whole code. This telegram bot serves one sole purpose - generate images based on any HuggingFace diffusers model by using one command. I released it since for me its quite hard to generate images through notebooks or any other way. You can easily manipulate the repo through Makefile

### Why was it worth to release it?

While it may appear that is quite minimal, it can provide a good starting point to launch your own Image generation like bot in Telegram. It has fully functional parts such as Telegram bot, PostgreSQL database to store user data and server for image generation.

### Contents

1. image_gen
2. server
3. .env

### Image_gen

This directory provides a simple FastAPI application for image generation with diffusers. It gets the name of the model from .env file in the root of the repo.

### Server

This directory is a fully functional telegram bot that is backed by PostgreSQL database. It gets the name of the telegram token and your inference server URL from .env file in the root of the repo.

### .env

I really liked ideas conveyed in .env files, so I just used one here. It contains all the necessary secret codes that are used in the bot.