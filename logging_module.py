import datetime
import sqlite3
import time

# Function used to document user interactions within the App
def write_log(command, module, accType):
    conn = sqlite3.connect('appLogs.db')
    cur = conn.cursor()

    # Recording of the current date and time
    date = datetime.datetime.today()
    localtime = time.asctime(time.localtime(time.time()))
    cur.execute("INSERT INTO logs VALUES(NULL,?,?,?,?,?)",
                (date.date(),localtime[11:19],command,module,accType))
    conn.commit()
    cur.close()
    conn.close()


