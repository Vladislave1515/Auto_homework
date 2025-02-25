from sqlalchemy import create_engine, text
import pytest


db_connection_string = "postgresql://postgres:1234@localhost:5432/QA"
db = create_engine(db_connection_string)


@pytest.mark.run(order=1)
def test_add_student():
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

    check_sql = text("SELECT * FROM student")
    with db.connect() as connection:
        result = connection.execute(check_sql).fetchall()
        last_entry = result[-1] if result else None
        assert last_entry is not None
        assert last_entry[0] == 1001
        assert last_entry[1] == 'Bachelor'
        assert last_entry[2] == 'Full-time'
        assert last_entry[3] == 10


@pytest.mark.run(order=1)
def test_update_student():
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

    check_sql = text("SELECT * FROM student WHERE user_id = :user_id")
    with db.connect() as connection:
        result = connection.execute(check_sql, {'user_id': 1001}).fetchone()
        assert result is not None
        assert result[1] == 'Master'
        assert result[2] == 'Part-time'
        assert result[3] == 20


@pytest.mark.run(order=1)
def test_delete_student():
    sql = text(
        "DELETE FROM student WHERE user_id = :user_id"
    )
    with db.connect() as connection:
        connection.execute(
            sql, {'user_id': 1001}
        )
        connection.commit()

    check_sql = text("SELECT * FROM student WHERE user_id = :user_id")
    with db.connect() as connection:
        result = connection.execute(check_sql, {'user_id': 1001}).fetchone()
        assert result is None
