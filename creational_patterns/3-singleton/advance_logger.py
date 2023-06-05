from threading import Lock, Thread
from time import sleep


class LoggerMeta(type):

    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                sleep(2)
                instance = super().__call__(*args, **kwargs)
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
        'RESULT:\n'
    )

    process1 = Thread(target=test_logger, args=('first logger',))
    process2 = Thread(target=test_logger, args=('second logger',))
    process1.start()
    process2.start()
