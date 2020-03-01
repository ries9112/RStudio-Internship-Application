import shrimpy

public_key = secret_shrimpy_key
secret_key = shrimpy_secret
client = shrimpy.ShrimpyApiClient(public_key, secret_key)
ticker = client.get_ticker('binance')
print(ticker)


client.get_asset_dominance()


# function documentation: https://pypi.org/project/shrimpy-python/
