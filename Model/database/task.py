from datetime import datetime
from dataclasses import dataclass


@dataclass
class Task:
    __table__ = 'task'

    id: int = None
    title: str = None
    description: str = None
    expire_date: datetime = None
    user_id: int = None
