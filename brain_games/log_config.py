"""Settings for logging."""

import logging

ERROR_LOG_FILENAME = '.brain-games-errors.log'

LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s:%(name)s:%(process)d:%(lineno)d ' '%(levelname)s %(message)s',  # noqa: E501
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(message)s',
        },
    },
    'handlers': {
        'logfile': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'filename': ERROR_LOG_FILENAME,
            'formatter': 'default',
            'backupCount': 2,
        },
        'verbose_output': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout',
        },
    },
    'loggers': {
        'brain-games-info': {
            'level': 'INFO',
            'handlers': [
                'verbose_output',
            ],
        },
        'brain-games-error': {
            'level': 'ERROR',
            'handlers': [
                'logfile',
            ],
        },
    },
}

log_error = logging.getLogger('brain-games-error')
log_info = logging.getLogger('brain-games-info')
