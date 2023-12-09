from dataclasses import dataclass


@dataclass
class BotConfig:
    token: str


@dataclass
class DBConfig:
    path: str

    @property
    def full_url(self) -> str:
        return "sqlite+aiosqlite:///{}".format(self.path)
