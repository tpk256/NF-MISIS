import sqlite3



conn = sqlite3.connect('db_bot.data')

cur = conn.cursor()



cur.execute(f"""UPDATE Schedule
    SET 
    hash_excel = 123
WHERE course_id = 3;"""
            )


conn.commit()
conn.close()