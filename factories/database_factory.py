class DatabaseFactory:
    _registry = {}

    @classmethod
    def register(cls, db_type: str, creator):
        cls._registry[db_type.lower()] = creator

    @classmethod
    def create_database(cls, db_type: str):
        db_type = db_type.strip().lower()

        if db_type not in cls._registry:
            raise ValueError(f"Unknown database type: {db_type}")

        return cls._registry[db_type]()