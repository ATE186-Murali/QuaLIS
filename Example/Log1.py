import logging


class log:
    def logInfo(info):
        logging.basicConfig(filename="info.log", format='%(asctime)s:%(levelname)s: %(message)s',
                            datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.INFO)
        log = logging.getLogger()

        log.info(info)

    def logError(error):
        logging.basicConfig(filename="Error.log", format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt="%m/%d/%Y %I:%M:%S %p", level=logging.ERROR)
        log = logging.getLogger()

        log.error(error)
