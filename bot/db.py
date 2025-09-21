import sqlite3
import datetime
import json
from typing import Optional

from pydantic import BaseModel



class Schedule(BaseModel):
    id: int

    course_id: int
    parity: int
    hash_excel: str
    url: str
    files_id: list[str]

    count_updates: int
    date_updated: int
    date_created: int


def get_schedule_info(course: int, parity: int, cur: sqlite3.Cursor) -> Optional[Schedule]:
    sql = """
        SELECT
            *
        FROM
            Schedule
        WHERE
            course_id = ? AND parity = ?
        ORDER BY date_updated DESC
        LIMIT 1;

    """

    cur.execute(
        sql,
        (course, parity)
    )

    founded = cur.fetchone()
    if not founded:
        return None

    return Schedule(
        id=founded[0],

        course_id=founded[1],
        parity=founded[2],
        hash_excel=founded[3],
        url=founded[4],
        files_id=json.loads(founded[5]),

        count_updates=founded[6],
        date_updated=founded[7],
        date_created=founded[8],
    )


