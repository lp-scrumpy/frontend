import logging

from flask import Flask
from frontend import config
from frontend.views import plannings
from frontend.views.app import view
logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info("application started")
    app = Flask(__name__)
    app.secret_key = config.SECRET_KEY
    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(plannings.view, url_prefix='/plannings')
    app.run()


if __name__ == '__main__':
    main()
