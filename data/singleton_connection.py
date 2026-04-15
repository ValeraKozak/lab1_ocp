class SingletonConnection:
    _instances = {}

    def __new__(cls, connection_string=None):
        key = connection_string or "__default__"
        if key not in cls._instances:
            instance = super(SingletonConnection, cls).__new__(cls)
            instance.connection_string = connection_string
            cls._instances[key] = instance
        return cls._instances[key]
