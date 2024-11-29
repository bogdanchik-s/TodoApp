from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    __table__ = 'user'

    id: int = None
    username: str = None
    email: str = None
    name: str = None
    surname: str = None
    is_admin: bool = None
    register_date: datetime = None
    last_login: datetime = None
