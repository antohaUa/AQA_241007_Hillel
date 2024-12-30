import dbm
import pytest


def db_operations_handler(func):
    def wrapper(*args, **kwargs):
        try:
            db_session = dbm.open()
            result = func(db_session)
            return result
        except Exception:
            pass
        finally:
            db.close()

    return wrapper


class Test:

    @pytest.fixture(scope="class")
    def database(self):
        session = db.open()
        yield session
        db.close()

    def test_1(self, database):
        database.exec_query()
        database.add()

    def __init__(self, db_name):
        db.open()

    def __del__(self):
        print("DB closed")

    @db_operations_handler
    def db_transaction1(self, db_connection):
        pass

    def db_transaction2(self):
        try:
            dbm.open()
            db.close()
        except Exception as g_exc:
            pass
