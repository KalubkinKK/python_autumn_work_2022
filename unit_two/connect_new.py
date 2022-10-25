import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="task",
    user="postgres",
    password="263024")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
id_student = input('Введите id студента: ')

SQL_GET_TASK_BY_STUDENT = f"""SELECT s.surname, t.name, t.condition
                                FROM student s, student_task st, task t
                                WHERE s.id = st.id_student
                                AND st.id_task = t.id
                                AND s.id = {id_student}"""

cur.execute(SQL_GET_TASK_BY_STUDENT)

# Retrieve query results
records = cur.fetchall()

for row in records:
    print(row)

conn.close()
