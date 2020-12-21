#name = input("Enter your name: ")
#test

#! /usr/local/bin/python
import re
import os
print __file__
RELATIVE_PATH = os.path.dirname(__file__)
log_path = RELATIVE_PATH + '/log' if RELATIVE_PATH is not None and RELATIVE_PATH else './log'
print log_path


DPS = 'dps'
ELS = 'elasticsearch'
KAFKA = 'kafka'
old_service_keys = [DPS, ELS, KAFKA]
services_with_version = {}
lines = [
"logmgr                  1.0.0.20201214233206          c1ced486edc849e00412208cf1a35fd99244b2e7",
"daemon                  1.0.0.20201214233206          c1ced486edc849e00412208cf1a35fd99244b2e7",
"osc                     1.0.0.20201214233206          c1ced486edc849e00412208cf1a35fd99244b2e7",
"cache                   1.0.0.20201214233206          c1ced486edc849e00412208cf1a35fd99244b2e7",
"dns                     1.0.0.20201214233206          c1ced486edc849e00412208cf1a35fd99244b2e7",
"ls                      1.0.0.20201214233206          c1ced486edc849e00412208cf1a35fd99244b2e7",
"elasticsearch           1.0.0.20201217130608          f9d0fd84ecd1f78ccd5c793f08d69dc141c8c532",
"kafka                   1.0.0.20201217130608          f9d0fd84ecd1f78ccd5c793f08d69dc141c8c532",
"dps                     1.0.0.20201217130608          f9d0fd84ecd1f78ccd5c793f08d69dc141c8c532"]

def test_dps():
	tmpdict = dict()
	tmpdict['key1'] = 'value1'
	tmpdict['key2'] = 'value2'
	tmpdict['key3'] = 'value3'
	print tmpdict
	tmpdict['key2'] = 'value22'
	print tmpdict
	tmpdict['key1'] = 'value111'
	print tmpdict

if __name__ == '__main__':
	print __name__
