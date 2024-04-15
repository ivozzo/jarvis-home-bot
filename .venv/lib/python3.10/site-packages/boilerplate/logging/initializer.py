import logging


def init_logger_with_file(logging_level, path, filename):
    global logger

    loggerDictionary = {"INFO": logging.INFO, "WARN": logging.WARN, "DEBUG": logging.DEBUG, "ERROR": logging.ERROR}

    logging.basicConfig(
        level=loggerDictionary[logging_level],
        format="%(asctime)s|[%(threadName)-12.12s]|[%(levelname)-5.5s]| %(message)s",
        handlers=[
            logging.FileHandler("{0}/{1}".format(path, filename)),
            logging.StreamHandler()
        ])

    return logging.getLogger()

def init_logger_only_console(logging_level):
    global logger

    loggerDictionary = {"INFO": logging.INFO, "WARN": logging.WARN, "DEBUG": logging.DEBUG, "ERROR": logging.ERROR}

    logging.basicConfig(
        level=loggerDictionary[logging_level],
        format="%(asctime)s|[%(threadName)-12.12s]|[%(levelname)-5.5s]| %(message)s",
        handlers=[
            logging.StreamHandler()
        ])

    return logging.getLogger()
