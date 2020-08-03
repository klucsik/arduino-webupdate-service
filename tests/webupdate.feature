Feature: Arduino webUpdate
As an esp8266 board with arduino code on it
I want to be able to get updates if needed. 
For this I need the link for the binaries, when update needed.

    Scenario: There is a new version
        Given the server has a folder with binary named 'test'
        And it has a binary with version 0_1
        When I make a request with name: 'test' and version: '0_0'
        Then I get a response: '/static/bin/test/0_1.bin'

    Scenario: There is no new version
        Given the server has a folder with binary named 'test'
        And it has a binary with version 0_1
        When I make a request with name: 'test' and version: '0_1'
        Then I get a response: 'update not needed'

    Scenario: There is no such device name
        Given the server doesn't have a folder with name: 'notexist'
        When I make a request with name: 'notexist' and version: '0_0'
        Then I get a response with status code 404