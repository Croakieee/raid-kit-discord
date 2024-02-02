"""
Discord Raidkit v2.4.4
the-cult-of-integral

Last modified: 2023-04-24 21:08
"""

import inspect
import logging


def init():
    """Initialize the logger."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s - %(asctime)s :: %(message)s',
        filename='raidkit.log',
        filemode='a+',
        datefmt='%d/%m/%Y %H:%M:%S')


def _log_message(level: str, message: str):
    """Log a message at the specified logging level."""
    frame, filename, _, func_name, _, _ = inspect.stack()[2]
    calling_module = inspect.getmodulename(filename)
    class_name = frame.f_locals.get('self', None).__class__.__name__
    if class_name:
        func_name = f'{class_name}.{func_name}'
    getattr(logging, level)(f'{calling_module}.py - {func_name} - {message}')


def sdebug(message: str):
    """Standard debug message format for Discord Raidkit"""
    _log_message('debug', message)


def sinfo(message: str):
    """Standard info message format for Discord Raidkit"""
    _log_message('info', message)


def swarning(message: str):
    """Standard warning message format for Discord Raidkit"""
    _log_message('warning', message)


def serror(message: str):
    """Standard error message format for Discord Raidkit"""
    _log_message('error', message)


def scritical(message: str):
    """Standard critical message format for Discord Raidkit"""
    _log_message('critical', message)
