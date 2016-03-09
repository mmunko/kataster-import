import logging

class Logger:
    """Trieda zabezpecujuca logovanie do sys.stdout a sys.stderr"""
    def __init__(self):
        self.logging = logging
        self.logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', datefmt='%d/%m/%Y %H:%M:%S', level=logging.DEBUG)

    def info(self,message):
        self.logging.info(message)

    def debug(self,message):
        self.logging.debug(message)

    def warning(self,message):
        self.logging.warning(message)

    def error(self,message):
        self.logging.error(message)

    def critical(self,message):
        self.logging.critical(message)
