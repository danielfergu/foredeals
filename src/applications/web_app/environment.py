import os
from dataclasses import dataclass
from dotenv import load_dotenv


@dataclass
class Environment:
    port: int
    secret_key: str
    host_url: str
    database_url: str
    use_flask_debug_mode: bool

    @classmethod
    def from_env(cls) -> "Environment":

        load_dotenv(os.path.abspath('.env'))
        #print(f"DEBUG: Environment Variables = {os.environ}")

        return cls(
            port=int(os.environ.get("PORT", 8080)),
            secret_key=cls.require_env("SECRET_KEY"),
            host_url=cls.require_env("HOST_URL"),
            database_url=cls.require_env("DATABASE_URL"),
            use_flask_debug_mode=os.environ.get("USE_FLASK_DEBUG_MODE", "true")
            == "true",
        )

    @classmethod
    def require_env(cls, name: str) -> str:
        value = os.environ.get(name)
        if value is None:
            raise Exception(f"Unable to read {name} from the environment")
        return value
