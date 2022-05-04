<p align="center">
  <a href="https://github.com/bnkc/morningbot"><img alt="Morning Bot" src="https://github.com/bnkc/morningbot/blob/master/images/logo.png" width="60%"></a>
</p>


![PyPI pyversions](https://img.shields.io/pypi/pyversions/deadlink.svg?style=flat-square)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
![gh-actions](https://img.shields.io/github/workflow/status/nschloe/deadlink/ci?style=flat-square)

## What is it?

I live in Ohio, which means the weather is incredibly unpredictable. Because of this, checking the weather on a daily basis is a must. **Morning Bot** makes this easy. Every morning I receive a text from Morning Bot that provides Cliff notes on what the weather is like. Additionally, Morning Bot synced up with [**Shortcuts**](https://apps.apple.com/us/app/shortcuts/id915249334) meaning you will always get weather updates based on your most current location.

## Main Features
Here are just a few of the things that **Morning Bot** does well:

- Hands-off weather updates every morning
- Easily `configurable` to receive weather updates at your desired time every morning.
- Tethered to your phone. Feel free to travel and get weather updates for your most current location. Accomplished using [**Shortcuts**](https://apps.apple.com/us/app/shortcuts/id915249334). You may also set a `default` location if you wish to not share your location.
- Weather data collected from [**Open Weather**](https://openweathermap.org/), a reliable RESTful API
- Subscribe or unsubscribe for Morning Bot with a click of a button 
- Most importantly, a badass app
 
## Configuration

* [Setting up Shortcuts](#setting-up-shortcuts)
* [Additional Info](#additional-info)


## Setting up Shortcuts



Apple Users:

1. Go to the app store and download [**Shortcuts**](https://apps.apple.com/us/app/shortcuts/id915249334)
2. 




## Additional Info

The source code is currently hosted on GitHub at:
https://github.com/bnkc/morningbot

- Python `3` and above
- Linux/MacOS *(Not tested on windows)*

Folder Structure:
```
morningbot
├── Procfile
├── README.md
├── app
│   ├── api
│   │   ├── __init__.py
│   │   └── api.py
│   ├── config.py
│   ├── conftest.py
│   ├── crud
│   │   ├── __init__.py
│   │   ├── crud_user.py
│   │   └── crud_weather.py
│   ├── db
│   │   ├── __init__.py
│   │   ├── database.db
│   │   └── session.py
│   ├── messages
│   │   ├── __init__.py
│   │   └── message.py
│   ├── schemas
│   │   ├── __init__.py
│   │   └── weather.py
│   └── tests
│       ├── crud
│       │   ├── __init__.py
│       │   ├── test_user.py
│       │   └── test_weather.py
│       └── data
│           ├── __init__.py
│           └── sample_data.py
├── images
│   └── logo.png
├── requirements.txt
└── runtime.txt
```

To get started, mkdir and cd into where Morning Bot will be stored.
Run:

```console
$ git clone https://github.com/bnkc/morningbot.git
```
From `./morningbot/`, install the dependecies with:

```console
$ pip install -r requirements.txt
```
Create a virtual environment from the `requirements.txt` *(or installed globally)*.

You will need to create a `.env` in the the path `./morningbot/app/` for the os environment variables. It should look something like this:

```
WX_API_KEY=<openweather key>
```
You will need to sign up with [**Open Weather**](https://openweathermap.org/), as well as setup your [**Twilio**](https://www.twilio.com/).
Both of these resources have great documentation.


