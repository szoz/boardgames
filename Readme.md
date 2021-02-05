# boardgames

boardgames is backend application with REST API created with [Flask](https://flask.palletsprojects.com/). Application
contains data about top 100 boardgames from [BoardGameGeek](https://boardgamegeek.com/browse/boardgame)
stored in PostgreSQL database.

## Installation

Use the package manager [PipEnv](https://pypi.org/project/pipenv/) to install application dependencies.

```bash
pipenv install
```

Application can be deployed on Heroku - [Gunicorn](https://gunicorn.org/) webserver runs application based on `Procfile`
content. Application uses data with specific structure stored in the database.

## Usage

All endpoints are described in Open API documentation available on root `/` endpoint.

## License

[MIT](https://choosealicense.com/licenses/mit/)