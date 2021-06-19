# Description

Template of flask application to serve deep learning or machine learning models.

Flask application implemented via class based approach. This implementation solves the following problems:

1. Models don't start when you import file where the application is. It could be useful when you want to test your web layer. In this approach, you can just import `create_app` function and mock your service.

2. Single entry point of the application. 

3. The application is configurable


### 


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
