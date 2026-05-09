import importlib
import pkgutil


class DatabaseFactory:
    _registry = {}
    _discovered = False

    @classmethod
    def register(cls, db_type: str, creator):
        cls._registry[db_type.lower()] = creator

    @classmethod
    def discover_databases(cls):
        if cls._discovered:
            return

        import data

        for module_info in pkgutil.iter_modules(data.__path__):
            if module_info.name in {"__init__", "database_base", "singleton_connection"}:
                continue
            if module_info.name.endswith("_db"):
                importlib.import_module(f"data.{module_info.name}")

        cls._discovered = True

    @classmethod
    def create_database(cls, db_type: str, **kwargs):
        cls.discover_databases()
        db_type = db_type.strip().lower()

        if db_type not in cls._registry:
            raise ValueError(f"Unknown database type: {db_type}")

        return cls._registry[db_type](**kwargs)

    @classmethod
    def available_databases(cls):
        cls.discover_databases()
        return tuple(sorted(cls._registry.keys()))
