import boilerplate.logging.initializer as initializer


class Logger:
    def __init__(self, path, filename, level):
        self.path = path
        self.filename = filename
        self.level = level
        self.logger = initializer.init_logger(logging_level=level, path=path, filename=filename)

    def __init__(self, level):
        self.path = None
        self.filename = None
        self.level = level
        self.logger = initializer.init_logger_only_console(logging_level=level)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warn(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)
