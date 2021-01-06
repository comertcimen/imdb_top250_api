# Imdb Top 250 API

Imdb Top 250 is an API created with Fastapi and Beautifulsoup 4. It crawls the data from [imdb](https://www.imdb.com/chart/top/).

[LIVE](http://34.70.181.65/)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip install - r requirements.txt
```

## Usage on Windows

```bash
py -m uvicorn main:app --host 0.0.0.0 --port 80
```

## Usage on Linux/MacOS

```bash
python3 -m uvicorn main:app --host 0.0.0.0 --port 80
```

## Open browser to see the API

```bash
127.0.0.1
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://github.com/comertcimen/imdb_top250_api/blob/main/LICENSE)
