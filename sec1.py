import logging
import logging.config

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(app)s]:[%(levelname)s] %(name)s: %(message)s:%(funcName)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
}

def d():
    logging.config.dictConfig(LOGGING_CONFIG)
    log = logging.getLogger(__name__)
    log=logging.LoggerAdapter(log,{"app":"test"})
    log.info("hello world")

# if __name__ == "__main__":
# 