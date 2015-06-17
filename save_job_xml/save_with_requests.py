import requests


response = requests.get('http://localhost:8080/job/Trigger_test/config.xml')
print response.text
