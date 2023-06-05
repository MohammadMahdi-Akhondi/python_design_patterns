from threading import Thread
from time import sleep


class LoggerMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            sleep(2)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Logger(metaclass=LoggerMeta):
    _text = None

    def __init__(self, text):
        self._text = text

    def show(self):
        print(self._text)


def test_logger(text: int) -> None:
    logger = Logger(text)
    logger.show()


if __name__ == '__main__':

    print(
        'If you see the same text, then logger was reused\n'
        'If you see different texts, '
        'then 2 logger were created\n\n'
    )

    print('Result in multithread case:')
    process1 = Thread(target=test_logger, args=('first logger',))
    process2 = Thread(target=test_logger, args=('second logger',))
    process1.start()
    process2.start()
    sleep(5)

    print('\n\nResult in normal case:')
    logger1 = Logger('first logger')
    logger2 = Logger('second logger')
    print(id(logger1))
    print(id(logger2))
