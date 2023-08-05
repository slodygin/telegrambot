import logging
from enum import IntEnum

from app.controls import sqlite

logger = logging.getLogger(__name__)

class CoffeeStatus(IntEnum):
    OFF = 0
    ON = 1


def change_status(user_id: int, status: CoffeeStatus) -> bool:
    res = sqlite.execute("UPDATE users set cur_status = ? where id = ?", (status, user_id,))
    if res == 0:
        res = sqlite.execute("INSERT INTO users VALUES (?, ?)", (user_id, status))
    logger.debug(f"Меняем coffee status на {status.name}.")
    return res != 0


def get_status(user_id: int) -> CoffeeStatus:
    record = sqlite.fetchone("SELECT cur_status FROM users WHERE id = ?", (user_id,))
    return CoffeeStatus(record[0]) if record is not None else CoffeeStatus.OFF
