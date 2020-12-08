import subprocess
import json

data = subprocess.check_output(
    ['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

wifis = [line.split(':')[1][1:-1]
         for line in data if 'All User Profile' in line]

wifi_arr = []

for wifi in wifis:
    results = subprocess.check_output(
        ['netsh', 'wlan', 'show', 'profile', wifi, 'key=clear']).decode('utf-8').split('\n')
    results = [line.split(':')[1][1:-1]
               for line in results if 'Key Content' in line]
    try:
        wifi_arr.append({'name': wifi, 'password': results[0]})
    except IndexError:
        wifi_arr.append({'name': wifi, 'password': 'Cannot be read!'})

with open('wifi password.json', 'w') as outfile:
    json.dump(wifi_arr, outfile)
