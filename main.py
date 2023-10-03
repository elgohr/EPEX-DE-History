from urllib.request import urlopen
from datetime import datetime


def collect():
    with urlopen('https://api.awattar.de/v1/marketdata/current.yaml') as response:
        with open('data/' + datetime.today().strftime('%Y-%m-%d') + '.yaml', 'wb') as data_file:
            data_file.write(response.read())


if __name__ == '__main__':
    collect()
