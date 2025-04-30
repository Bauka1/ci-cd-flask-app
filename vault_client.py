import hvac
client = hvac.Client(url='http://localhost:8200', token='SONAR_TOKEN')
secret = client.secrets.kv.read_secret_version(path='secret/flask-api')
api_key = secret['data']['data']['api_key']
