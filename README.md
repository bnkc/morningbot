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

* [Overview/Folder Structure](#overview-and-folder-structure)  
* [Cloning Repo and Installing Dependencies](#data-cleaning)
* [Setting Up Twilio](#removing-outliers)
* [Setting Up Shortcuts](#life-expectancy-analysis)
* [Hosting on Heroku/Scheduler](#life-expectancy-analysis)

## Overview and folder structure

```
morningbot
├── README.md
├── app
│   ├── __pycache__
│   │   ├── app.cpython-310.pyc
│   │   ├── app.cpython-39.pyc
│   │   └── run.cpython-39.pyc
│   ├── app.py
│   ├── crud
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   ├── __init__.cpython-39.pyc
│   │   │   ├── core.cpython-310.pyc
│   │   │   ├── core.cpython-39.pyc
│   │   │   ├── helper.cpython-310.pyc
│   │   │   └── helper.cpython-39.pyc
│   │   ├── core.py
│   │   └── helper.py
│   ├── docs
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   ├── __init__.cpython-39.pyc
│   │   │   ├── config.cpython-310.pyc
│   │   │   ├── config.cpython-39.pyc
│   │   │   ├── config_twilio.cpython-39.pyc
│   │   │   ├── config_weather.cpython-39.pyc
│   │   │   └── inbound_messages.cpython-39.pyc
│   │   ├── config_twilio.py
│   │   ├── config_weather.py
│   │   └── inbound_messages.py
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-310.pyc
│   │   │   ├── __init__.cpython-39.pyc
│   │   │   ├── weather.cpython-310.pyc
│   │   │   └── weather.cpython-39.pyc
│   │   └── weather.py
│   ├── tests
│   │   ├── __pycache__
│   │   │   ├── test_core.cpython-310-pytest-7.1.1.pyc
│   │   │   └── test_weather.cpython-310-pytest-7.1.1.pyc
│   │   ├── crud
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-310.pyc
│   │   │   │   ├── __init__.cpython-39.pyc
│   │   │   │   ├── test_core.cpython-310-pytest-7.1.1.pyc
│   │   │   │   └── test_core.cpython-39-pytest-7.1.1.pyc
│   │   │   └── test_core.py
│   │   ├── docs
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   │   ├── __init__.cpython-39.pyc
│   │   │   │   └── test_inbound_messages.cpython-39-pytest-7.1.1.pyc
│   │   │   └── test_inbound_messages.py
│   │   └── weather
│   │       ├── __init__.py
│   │       ├── __pycache__
│   │       │   ├── __init__.cpython-310.pyc
│   │       │   ├── __init__.cpython-39.pyc
│   │       │   ├── test_weather.cpython-310-pytest-7.1.1.pyc
│   │       │   └── test_weather.cpython-39-pytest-7.1.1.pyc
│   │       └── test_weather.py
│   └── weather
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-310.pyc
│       │   ├── __init__.cpython-39.pyc
│       │   ├── weather.cpython-310.pyc
│       │   └── weather.cpython-39.pyc
│       └── weather.py
├── images
│   └── logo.png
├── requirements.txt
└── runtime.txt
```
