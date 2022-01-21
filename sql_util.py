import sqlite3
from dataclasses import dataclass
import pandas as pd


@dataclass
class Row:
    kor: str
    eng: str


def create_db():
    name = "koreng"

    conn = sqlite3.connect(f"./dbs/{name}.db")
    conn.execute(f"""CREATE TABLE {name} (
        kor text,
        eng text
    )""")

    conn.commit()
    conn.close()


def read_db():
    """
    reads entire koreng table
    """
    name = "koreng"

    conn = sqlite3.connect(f"./dbs/{name}.db")
    df = pd.read_sql_query(f"SELECT * FROM {name}", conn)
    conn.close()

    return df


def add_row(row: Row):
    """
    Does not do any logic or decision making, just adds the row to the db
    """
    name = "koreng"
    conn = sqlite3.connect(f"./dbs/{name}.db")
    conn.execute(
        f"INSERT INTO {name} (kor, eng) VALUES ('{row.kor}', '{row.eng}')")
    conn.commit()
    conn.close()
