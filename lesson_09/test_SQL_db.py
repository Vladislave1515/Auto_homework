from sqlalchemy import create_engine, text


db_connection_string = "postgresql://postgres:1234@localhost:5432/QA"
db = create_engine(db_connection_string)


def add_student():
    sql = text(
        "INSERT INTO student (user_id, level, education_form, subject_id) "
        "VALUES (:user_id, :level, :education_form, :subject_id)"
    )
    with db.connect() as connection:
        connection.execute(
            sql, {
                'user_id': 1001,
                'level': 'Bachelor',
                'education_form': 'Full-time',
                'subject_id': 10
            }
        )
        connection.commit()


def update_student():
    sql = text(
        "UPDATE student SET level = :level, education_form = :education_form, "
        "subject_id = :subject_id WHERE user_id = :user_id"
    )
    with db.connect() as connection:
        connection.execute(
            sql, {
                'level': 'Master',
                'education_form': 'Part-time',
                'subject_id': 20,
                'user_id': 1001
            }
        )
        connection.commit()


def delete_student():
    sql = text(
        "DELETE FROM student WHERE user_id = :user_id"
    )
    with db.connect() as connection:
        connection.execute(
            sql, {'user_id': 1001}
        )
        connection.commit()


add_student()
update_student()
delete_student()
