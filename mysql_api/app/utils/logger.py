import logging


def logging_info(_from='', msg=''):
    logging.basicConfig(format='INFO:     %(message)s', level=logging.INFO)
    logging.info(f"{_from}:  {msg}")