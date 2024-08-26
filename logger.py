import logging

class Logger:
    '''
    Класс отвечающий за логгирование в файл log.log
    В каждый экземпляр необходимо передать имя логгера
    '''
    __log_file = 'log.log'

    def __init__(self, name_logger:str) -> None:
        '''
        инициализация базовых формата лога и формата времени, 
        инициализация логгера
        '''
        self.__base_format = '[%(asctime)s] [%(name)s] [%(levelname)s] =>> %(message)s'
        self.date_format = '%Y-%m-%d %H:%M:%S'
        logging.basicConfig(filename=self.__log_file,
                            filemode='w', level=logging.INFO, 
                            format=self.__base_format, 
                            datefmt=self.date_format,
                            encoding='utf-8')
        self.logger = logging.getLogger(name_logger)

    def log_info(self, msg:str):
        '''записать лог уровня INFO'''
        self.logger.info(msg)
    
    def log_warning(self, msg:str):
        '''записать лог уровня WARNING'''
        self.logger.warning(msg)
    

        


        
