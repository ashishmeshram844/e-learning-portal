import logging 

class CustomLogger():
    def __init__(self,logger_name = "root",logger_level = logging.INFO,file_name = "root.log"):
        self.formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s:%(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
        self.new_logger = logging.getLogger(logger_name)
        self.new_logger.setLevel(logger_level)
        fileHandler = logging.FileHandler('log_files/'+file_name,mode='a+')
        fileHandler.setLevel(logging.INFO)
        fileHandler.setFormatter(self.formatter)
        self.new_logger.addHandler(fileHandler)

    def get_logger(self):
        return self.new_logger



