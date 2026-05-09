import threading

from pymongo import MongoClient


class SQLServerConnectionManager:
    """
    Thread-safe singleton for SQL Server connection settings.
    Responsibility: keep exactly one shared SQL Server configuration object
    and create pyodbc connections from that configuration when needed.

    Simple Pythonic singleton in 2-3 lines:
    # if not hasattr(cls, "_instance"):
    #     cls._instance = super().__new__(cls)
    # return cls._instance
    """

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, connection_string):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    instance = super().__new__(cls)
                    instance.connection_string = connection_string
                    cls._instance = instance
        return cls._instance


class MongoClientSingleton:
    """
    Thread-safe singleton for MongoDB client.
    Responsibility: keep exactly one shared MongoClient for MongoDB.
    """

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, uri):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    instance = super().__new__(cls)
                    instance.uri = uri
                    instance.client = MongoClient(uri)
                    cls._instance = instance
        return cls._instance
