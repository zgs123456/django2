from . import api
import logging
from flask import current_app


@api.route('/test',methods=['GET','POST'])
def index():
    logging.debug("This is a debug log.")
    logging.info("This is a info log.")
    logging.warning("This is a warning log.")
    logging.error("This is a error log.")
    logging.critical("This is a critical log.")

    return 'index'