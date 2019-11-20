import click
import requests
from pprint import pprint
from bitmax.util.auth import *


@click.command()
@click.option("--symbol", type=str, default=None)
@click.option("--account", type=str, default="cash", help="cash/margin")
@click.option("--config", type=str, default="config.json", help="path to the config file")
def run(symbol, account, config):
    btmx_cfg = load_config(config)['bitmax']

    host = btmx_cfg['https']
    group = btmx_cfg['group']
    apikey = btmx_cfg['apikey']
    secret = btmx_cfg['secret']

    ts = utc_timestamp()
    headers = make_auth_headers(ts, "order/open", apikey, secret)
    url = f"{host}/{group}/api/pro/{account}/order/open"

    params = dict(symbol=symbol)

    res = requests.get(url, headers=headers, params=params)
    pprint(res.headers)
    pprint(parse_response(res))


if __name__ == "__main__":
    run()