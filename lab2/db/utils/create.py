def get_command():
    return '''\
    CREATE TABLE employees(id INTEGER PRIMARY KEY, name TEXT, age INTEGER, sex TEXT, address TEXT, phone TEXT, \
    paassport TEXT, position_id INTEGER, rank_id INTEGER)
    '''