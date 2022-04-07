<p align="center">
  <a href="https://github.com/bnkc/morningbot"><img alt="Morning Bot" src="https://github.com/bnkc/morningbot/blob/master/images/logo.png" width="60%"></a>
</p>


![PyPI pyversions](https://img.shields.io/pypi/pyversions/deadlink.svg?style=flat-square)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
![gh-actions](https://img.shields.io/github/workflow/status/nschloe/deadlink/ci?style=flat-square)

## What is it?

I live in Ohio, which means the weather is incredibly unpredictable, sort of like Horton Hears a Who! Because of this, checking the weather on a daily basis is a must. Sometimes I forget and step outside in shorts to quickly find myself in ankle high snow. **Morning Bot** makes sure this doesnt happen. Every morning I recieve a text from **Morning Bot** that gives cliff notes on what the weather is like. Additionally **Morning Bot** is location dependant on your phone. Yes, this means you can travel and still get weather updates on wherever you might find yourself.

## Main Features
Here are just a few of the things that **Morning Bot** does well:

  - Weather updates every morning without you clicking a button
  - Easily `configurable` to recieve the morning texts at your desired time using [**Heroku Scheduler**](https://devcenter.heroku.com/articles/scheduler)
  - Tethered to your phone. Feel free to travel and still get those weather updates as you go. Accomplished using [**Shortcuts**](https://apps.apple.com/us/app/shortcuts/id915249334). You may also set a `default` location if you wish to not share your location. 
  - Deployed on [**Heroku**](https://dashboard.heroku.com/apps). You dont need to run this locally
  - Weather data collected from [**Open Weather**](https://openweathermap.org/), a reliable RESTful api with weather data around the world
  - Morning Bot uses [**Twilio**](https://www.twilio.com/) to be able to `send` and `recieve` messages with your **FREE** virtual number created
  - Bulk SMS capabilities. feel free to add your close ones to the callers list
  - Overall, a badass app
 
