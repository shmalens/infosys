import pymysql


class DBConnector:
    """
    config is a data, which uses for connect to database
    config have to allow next fields
    host - ip of host with db
    user - your connection username
    password - password of this user on db
    database - database name

    sample:
    {'host': 'localhost',
     'user': 'root',
     'password': 'very_secret',
     'database': 'schema_name'}
    """

    def __init__(self, config: dict):
        self.config = config

    def __enter__(self):
        try:
            self.connection = pymysql.connect(**self.config)
            self.cursor = self.connection.cursor()
            return self.cursor
        except pymysql.InterfaceError as err:
            return None
        except pymysql.OperationalError as err:
            if err.args[0] == 1049:
                print('Wrong data base name')
            if err.args[0] == 1045:
                print('Wrong username or password')
            if err.args[0] == 2003:
                print('Wrong host name')
            return None

    def __exit__(self, exc_type, exc_value, exc_trace):
        if exc_value is None:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
        elif exc_value == 'empty_cursor':
            print('Cursor not created')
        elif exc_value.args[0] == 1046:
            print('Syntax error in sql request')
        elif exc_value.args[0] == 1146:
            print('Wrong table name')
        elif exc_value.args[0] == 1054:
            print('Wrong field name')
        return True


if __name__ == '__main__':
    test_config = {'host': 'localhost',
                   'user': 'root',
                   'password': 'CoWeNt11',
                   'database': 'banquet_order'}

    _SQL = 'SELECT * FROM `banquet_order`.`menu`'
    with DBConnector(test_config) as cursor:
        if cursor is None:
            raise ValueError('empty_cursor')
        cursor.execute(_SQL)
        for row in cursor.fetchall():
            print(row)
