# Simple arduino update service

[![Build Status](https://travis-ci.org/klucsik/arduino-webupdate-service.svg?branch=master)](https://travis-ci.org/klucsik/arduino-webupdate-service)
[![Coverage Status](https://coveralls.io/repos/github/klucsik/arduino-webupdate-service/badge.svg?branch=master)](https://coveralls.io/github/klucsik/arduino-webupdate-service?branch=master)

This application serves my arduino devices with updates when there is a new version available.
* It can distinguish between devices by devices based on the name parameter.
* It can hold only one version of the arduino binary
* Its compatible with the [ESP8266httpUpdate](https://github.com/esp8266/Arduino/tree/master/libraries/ESP8266httpUpdate) library
* It does not facilitaty any kind of authenticathion from the client side.

Check the tests for learn how it works

## Noszlop Greenhouse project
Various automations for a greenhouse at my fathers place in a rural village called Noszlop.
This project is my entry drug for IT, I working on this since 2014.

### Background
My father works a lot in his garden, he growns his own tomatoes and paprikas. He starts the process with germinateion. He puts the seeds in soil, and put those in a "reverse refigerator": Once was a refigerator, now it has a 100W lightbulb in it as a heatsource, and its job is to provide a nice 28 C° temperature and humid air for the germination.
After that, the young seedlings (around 2000 pieces) moves to the greenhouse. This usually happens in the early spring when it is a chance for night freezes, that would kill those poor seedlings. So before I started this porject father barely slept for about two weeks, checking the temperature hourly at nights.

I thought this shouldn't be that hard to automate, father should get enough sleep, so I started to learn building sensors, switching relays, collectiong and processing data. And code.

### The requirements
* The seedlings can't bee freeze to death.
* If some part of the system is fails, the others should work normally
* If some part is failing, there should be an alarm
* Father needs to see the actual data in the house (~100m away from the greenhouse)
* The system should be maintained remotely (as I not live in there anymore, and father won't be able to build and upload new firmware to the devices)

### The solution
 Built around the esp8266 board and the arduino framework, there is 3 thermostat with different settings:
 * One for the "reverse refigerator" for the germination
 * Two in the greenhouse, one for the whole greenhouse, and the other one is for a smaller portion of it.
 Built around the esp8266 and a simple led display and a speaker, the dispay and alarm unit in the house
 A google spreadsheet  which serves as a backend, holds the data and the configuration values
A python flask api server which manages the updates.

#### The repos included in this project
* https://github.com/klucsik/thermostat
* https://github.com/klucsik/arduino-webupdate-service
* https://gist.github.com/klucsik/da530b259c3476f6f1b3bd5e1f71a632