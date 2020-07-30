# Simple arduino update service
This application serves my arduino devices with updates when there is a new version available.
* It can distinguish between devices by devices based on the name parameter.
* It can hold only one version of the arduino binary
* Its compatible with the [ESP8266httpUpdate](https://github.com/esp8266/Arduino/tree/master/libraries/ESP8266httpUpdate) library
* It does not facilitaty any kind of authenticathion from the client side.

Check the tests for learn how it works