import datetime
import os
from log_type import LogType
from log_state import LogState

class Logger:

    def __init__(self):
        self.current_timestamp = 0
        self.get_timestamp()
        self.log_file = f'{self.current_timestamp}'
        self.content = ""
        

    def log(self, message = "This is a log"):
        self.putLog(0, message, 0)

    def f_log(self, message = "This is a file log"):
        self.putLog(0, message, 1)

    def error(self, message = "This is an error"):
        self.putLog(1, message, 0)

    def f_error(self, message = "This is a file error"):
        self.putLog(1, message, 1)

    def get_timestamp(self):
        self.current_timestamp = datetime.datetime.now()
        self.current_timestamp = self.current_timestamp.strftime("%d:%m:%Y %H:%m:%S %p")

    def putLog(self, log_type, message, log_state):
        self.get_timestamp()

        if log_type == LogType.LOG:

           self.content = f'[LOG {self.current_timestamp}] : {message}\n'
        elif log_type == LogType.ERROR:
               self.content = f'[ERROR {self.current_timestamp}] : {message}\n'
        else:
           return

        if log_state == LogState.CONSOLE:
            
            print(self.content)
        else:
            if not self.file_exists(self.log_file):
                self.create_log_file()

            self.log_to_file()

    def file_exists(self, filepath):
        return os.path.exists(filepath)

    def create_log_file(self):

        try:
            
            fh = open(f'logs/{self.log_file}.txt', 'x')
            fh.close()
        except:
            self.putLog(0, f'File, {self.log_file} creation failed!')
            return

    def log_to_file(self):

        try:
            g
            fh = open(f'logs/{self.log_file}.txt', 'a')
            fh.write(self.content)
            fh.close()
        except:
            self.putLog(0, 'Filed to log into file')
            return





