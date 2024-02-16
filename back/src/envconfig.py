from typing import Final
import os


class BaseConfig:
    """Shared configuration"""

    def __init__(self):
        # Flask
        self.MIGRATION: Final[str] = os.getenv("MIGRATION")

        # Database
        self.USER: Final[str] = os.getenv("DB_USER")
        self.DB_PASS: Final[str] = os.getenv("DB_PASS")
        self.DB_NAME: Final[str] = os.getenv("DB_NAME")
        self.DB_IP: Final[str] = os.getenv("DB_IP")
        self.SQLALCHEMY_DATABASE_URI: Final[str] = \
            f"postgresql://{self.USER}:{self.DB_PASS}@{self.DB_IP}:5432/{self.DB_NAME}"


class Development(BaseConfig):
    def __init__(self):
        super().__init__()
        self.DEBUG = True
        self.ENV = "dev"