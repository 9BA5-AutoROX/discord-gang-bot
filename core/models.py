import sqlite3

def init_db():
    conn = sqlite3.connect("data/gang.db")
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users(
        discord_id TEXT PRIMARY KEY,
        game_name TEXT,
        title TEXT,
        tag TEXT,
        role TEXT,
        join_date TEXT
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS items(
        item_name TEXT PRIMARY KEY,
        quantity INTEGER
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS money(
        gang_money_total INTEGER
    )
    """)

    conn.commit()
    conn.close()
