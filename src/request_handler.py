import logging
import re
from datetime import datetime

import clock


def convert_time(numeric_time=None):

    if not numeric_time:
        numeric_time = datetime.now().strftime("%H:%M")
    elif re.search('[a-zA-Z]', numeric_time):
        return {"errorMessage": "Provided time [{}] contains non numeric characters".format(numeric_time)}, 400

    try:
        human_time = clock.talk(numeric_time)
    except ValueError as e:
        logging.error(e)
        return {"errorMessage": "Numeric time [{}] is not in a valid format".format(numeric_time)}, 400

    return {"humanTime": human_time}, 200
