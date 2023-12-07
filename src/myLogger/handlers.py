import glob
import logging.handlers
import os
import time
from logging import LogRecord


class CustomTimedRotatingFileHandler(logging.handlers.TimedRotatingFileHandler):
    def __init__(
        self,
        filename,
        when="h",
        interval=1,
        backup_count=0,
        encoding=None,
        delay=False,
        utc=False,
        at_time=None,
    ):
        super().__init__(
            filename="logs/"
                     + filename
                     + "_"
                     + time.strftime("%Y%m%d%H%M", time.localtime())
                     + "."
                     + "log",
            when=when,
            interval=interval,
            backupCount=backup_count,
            encoding=encoding,
            delay=delay,
            utc=utc,
            atTime=at_time,
        )
        super().setFormatter(
            logging.Formatter(
                fmt="[%(asctime)s] [%(levelname)s] [%(funcName)s()][%(lineno)s]: %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
                style="%",
            )
        )

        print("Current Working Directory: ")
        print(os.getcwd())

        self.delete_old_files()

    def delete_old_files(self):
        files = glob.glob("logs/*.log")
        print("files: ", files)
        files.sort(key=os.path.getmtime)
        while len(files) > 5:
            os.remove(files[0])
            files.pop(0)

    def emit(self, record: LogRecord) -> None:
        super().emit(record)