# deep_flask
Template of flask application to serve deep learning or machine learning models


### Run

```shell
export HOST="0.0.0.0"
export PORT=4567
gunicorn -w 2 -b $HOST:$PORT "web.app:create_app()"
```

### Tests

```shell
pytest
```

### How to make requests
Check `src.utils.make_request()` function