<p align="center">
  <a href="https://github.com/bnkc/morningbot"><img alt="Morning Bot" src="https://github.com/bnkc/morningbot/blob/master/images/logo.png" width="60%"></a>
</p>


![PyPI pyversions](https://img.shields.io/pypi/pyversions/deadlink.svg?style=flat-square)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
![gh-actions](https://img.shields.io/github/workflow/status/nschloe/deadlink/ci?style=flat-square)

## What is it?

I live in Ohio, which means the weather is incredibly unpredictable, sort of like Horton Hears a Who! Because of this, checking the weather on a daily basis is a must. Sometimes I forget and step outside in shorts to quickly find myself in ankle-high snow. **Morning Bot** makes sure this doesn't happen. Every morning I receive a text from Morning Bot that gives Cliff notes on what the weather is like. Additionally, Morning Bot is location dependent on your phone. Yes, this means you can travel and still get weather updates on wherever you might find yourself.

## Main Features
Here are just a few of the things that **Morning Bot** does well:

- Hands-off weather updates every morning
- Easily `configurable` to receive weather updates at your desired time using [**Heroku Scheduler**](https://devcenter.heroku.com/articles/scheduler)
- Tethered to your phone. Feel free to travel and still get those weather updates as you go. Accomplished using [**Shortcuts**](https://apps.apple.com/us/app/shortcuts/id915249334). You may also set a `default` location if you wish to not share your location.
- Deployed on [**Heroku**](https://dashboard.heroku.com/apps). You don't need to run this locally
- Weather data collected from [**Open Weather**](https://openweathermap.org/), a reliable RESTful API
- Morning Bot uses [**Twilio**](https://www.twilio.com/) to be able to `send` and `receive` messages with your **FREE** virtual number created
- Bulk SMS capabilities. feel free to add your close ones to the callers list
- Most importantly, a badass app
 
## Configuration

* [Folder Structure/Requirements](#folder-structure/requirements)  
* [Cloning and Installing Dependencies](#cloning-and-installing-dependencies)
* [Setting Up Twilio](#removing-outliers)
* [Setting Up Shortcuts](#life-expectancy-analysis)
* [Hosting on Heroku/Scheduler](#life-expectancy-analysis)

## Folder Structure/Requirements

- Python `3.9.1` or above
- Linux/MacOS *(Not tested on windows)*

```
morningbot
├── app
│   ├── app.py
│   ├── crud
│   │   ├── __init__.py
│   │   ├── core.py
│   │   └── helper.py
│   ├── docs
│   │   ├── __init__.py
│   │   ├── config_twilio.py
│   │   ├── config_weather.py
│   │   └── inbound_messages.py
│   ├── schemas
│   │   ├── __init__.py
│   │   └── weather.py
│   ├── tests
│   │   ├── crud
│   │   │   ├── __init__.py
│   │   │   └── test_core.py
│   │   ├── docs
│   │   │   ├── __init__.py
│   │   │   └── test_inbound_messages.py
│   │   └── weather
│   │       ├── __init__.py
│   │       └── test_weather.py
│   └── weather
│       ├── __init__.py
│       └── weather.py
├── images
│   └── logo.png
├── README.md
├── requirements.txt
└── runtime.txt
```

## Cloning and Installing Dependencies

The source code is currently hosted on GitHub at:
https://github.com/bnkc/morningbot

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





