from src.service import Service

from config import settings

from web.client import FlaskApplication


def create_app():

    service_settings = settings.get("service")

    app = FlaskApplication(
        recognition_service=Service(service_settings),
    )
    return app


if __name__ == "__main__":
    flask_app_settings = settings.get("flask")

    flask_app = create_app()
    flask_app.run(
        host=flask_app_settings.get("host"), port=flask_app_settings.get("port")
    )
