import logging
from pathlib import Path
from logging.handlers import TimedRotatingFileHandler
from logging.handlers import TimedRotatingFileHandler, SMTPHandler
import os


def logger():
    """
    Funcion logger.
    """
    path = (Path(__file__).parent / 'log')

    if not path.exists():
        path.mkdir(parents=True, exist_ok=False)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    logHandler = TimedRotatingFileHandler(
        path / 'log_app.log',
        when="midnight",
        interval=1,
        backupCount=90,
        encoding='utf8')
    logHandler.suffix = "%Y-%m-%d"
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)

    # Configurar el StreamHandler para la consola
    streamLogger = logging.StreamHandler()
    streamLogger.setLevel(logging.DEBUG)
    streamLogger.setFormatter(formatter)

    logger.addHandler(logHandler)
    logger.addHandler(streamLogger)

    # Email notifier 
    # mail_handler = SMTPHandler(
    #     mailhost=(os.getenv("SMTP_HOST"), int(os.getenv("SMTP_PORT"))),
    #     fromaddr=os.getenv("EMAIL_FROM"),
    #     toaddrs=[os.getenv("EMAIL_TO")],
    #     subject="Mensaje de Error Actualización de Datos ATTsF",
    #     credentials=(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASSWORD")),
    #     secure=()
    # )

    # mail_handler.setLevel(logging.ERROR)
    # mail_handler.setFormatter(formatter)
    # logger.addHandler(mail_handler)

    return logger


## Optimize logger 



class ContextFilter(logging.Filter):
    """
    Agrega contexto adicional a los logs.
    """
    def __init__(self, schema, process, task):
        super().__init__()
        self.schema = schema
        self.process = process
        self.task = task

    def filter(self, record):
        # Agrega información contextual al registro
        record.schema = self.schema
        record.process = self.process
        record.task = self.task
        return True

def get_logger(schema, process, task):
    """
    Configura y devuelve un logger con contexto adicional.
    """
    path = (Path(__file__).parent / 'log')

    if not path.exists():
        path.mkdir(parents=True, exist_ok=False)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(schema)s - %(process)s - %(task)s - %(levelname)s - %(message)s"
    )

    # Configuración del archivo de log
    logHandler = TimedRotatingFileHandler(
        path / 'log_app.log',
        when="midnight",
        interval=1,
        backupCount=90,
        encoding='utf8'
    )
    logHandler.suffix = "%Y-%m-%d"
    logHandler.setFormatter(formatter)

    # Configuración del log en consola
    streamLogger = logging.StreamHandler()
    streamLogger.setLevel(logging.DEBUG)
    streamLogger.setFormatter(formatter)

    # Agrega los handlers al logger
    logger.addHandler(logHandler)
    logger.addHandler(streamLogger)

    # Agrega el filtro con contexto
    context_filter = ContextFilter(schema, process, task)
    logger.addFilter(context_filter)

    return logger