import logging

from flask import Flask

from frontend.views.app import uapp as user_app
from frontend.views.plannings import uuapp as plannings_app

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.DEBUG)
    logger.info("application started")
    app = Flask(__name__)
    app.register_blueprint(plannings_app)
    app.register_blueprint(user_app)
    app.run()


if __name__ == '__main__':
    main()
