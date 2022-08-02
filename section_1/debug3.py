import requests
#import pytest

ex_val = {
    expected_values1: {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'},
    expected_values2 = {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'}
expected_values3 = {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'}
expected_values4 = {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'}
expected_values5 = {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}
}

for x in expected_values1:
    print(expected_values1[x])

link = "https://playground.learnqa.ru/ajax/api/user_agent_check"

user_agent = [
'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1',
'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0',
'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
]

for x in user_agent:
    response = requests.get(link, headers={"User-Agent": x})
    parsing_json = response.json()
    print(parsing_json["platform"])
    print(parsing_json["browser"])
    print(parsing_json["device"])

