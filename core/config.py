"""
NOVA Configuration
"""

class Config:
    NAME = "NOVA"
    VERSION = "2.0.0"
    AUTHOR = "Lipper Greem"

    DEBUG = True

    DATA_DIR = "data"
    LOG_DIR = "logs"
    ASSETS_DIR = "assets"

    WAKE_WORD = "hey NOVA"
    LANGUAGE = "en"

    @classmethod
    def info(cls):
        return {
            "name": cls.NAME,
            "version": cls.VERSION,
            "author": cls.AUTHOR,
            "debug": cls.DEBUG,
            "wake_word": cls.WAKE_WORD,
            "language": cls.LANGUAGE,
        }

    @classmethod
    def set_language(cls, language):
        cls.LANGUAGE = language

    @classmethod
    def set_debug(cls, enabled):
        cls.DEBUG = enabled
