import hvac

def get_secret_key():
    client = hvac.Client(url="http://vault:8200", token="root")
    secret = client.secrets.kv.read_secret_version(path='myapp')
    return secret['data']['data']['SECRET_KEY']
