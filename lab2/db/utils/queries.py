def get_create():
    queries = [
        '''\
        CREATE TABLE IF NOT EXISTS position(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT,
          salary INT,
          responsibility TEXT,
          demands TEXT
        );
        ''',
        '''\
        CREATE TABLE IF NOT EXISTS rank(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT,
          surcharges INTEGER,
          responsibility TEXT,
          demands TEXT
        );
        ''',
        '''\
        CREATE TABLE IF NOT EXISTS crime_type(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT,
          law_article TEXT,
          punishment TEXT,
          term INTEGER
        );
        ''',
        '''\
        CREATE TABLE IF NOT EXISTS victim(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT,
          birthdate TEXT,
          sex TEXT,
          address TEXT
        );
        ''',
        '''\
        CREATE TABLE IF NOT EXISTS employee(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT,
          age INTEGER,
          sex TEXT,
          address TEXT,
          phone TEXT,
          passport TEXT,
          position_id INTEGER,
          rank_id INTEGER,
          FOREIGN KEY(position_id) REFERENCES position(id),
          FOREIGN KEY(rank_id) REFERENCES rank(id)
        );
        ''',
        '''\
        CREATE TABLE IF NOT EXISTS criminal(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT,
          birthdate TEXT,
          sex TEXT,
          address TEXT,
          status TEXT,
          crime_type_id INTEGER,
          victim_id INTEGER,
          employee_id INTEGER,
          FOREIGN KEY(crime_type_id) REFERENCES crime_type(id),
          FOREIGN KEY(victim_id) REFERENCES victim(id),
          FOREIGN KEY(employee_id) REFERENCES employee(id)
        );
        '''
    ]

    return queries


def get_insert():
    queries = [
        '''\
        INSERT INTO position (name, salary, responsibility, demands)
        VALUES
         ("", 0, "", ""),
         ("", 0, "", ""),
         ("", 0, "", ""),
         ("", 0, "", ""),
         ("", 0, "", "");
        ''',
        '''\
        INSERT INTO rank (name, surcharges, responsibility, demands)
        VALUES
         ("", 0, "", ""),
         ("", 0, "", ""),
         ("", 0, "", ""),
         ("", 0, "", ""),
         ("", 0, "", "");
        ''',
        '''\
        INSERT INTO crime_type (name, law_article, punishment, term)
        VALUES
         ("", "", "", 0),
         ("", "", "", 0),
         ("", "", "", 0),
         ("", "", "", 0),
         ("", "", "", 0);
        ''',
        '''\
        INSERT INTO victim (name, birthdate, sex, address)
        VALUES
         ("", "", "", ""),
         ("", "", "", ""),
         ("", "", "", ""),
         ("", "", "", ""),
         ("", "", "", "");
        ''',
        '''\
        INSERT INTO employee (name, age, sex, address, phone, passport, position_id, rank_id)
        VALUES
         ("", 0, "", "", "", "", 1, 1),
         ("", 0, "", "", "", "", 1, 3),
         ("", 0, "", "", "", "", 2, 2),
         ("", 0, "", "", "", "", 2, 4),
         ("", 0, "", "", "", "", 3, 3),
         ("", 0, "", "", "", "", 3, 5),
         ("", 0, "", "", "", "", 4, 1),
         ("", 0, "", "", "", "", 4, 3),
         ("", 0, "", "", "", "", 5, 2),
         ("", 0, "", "", "", "", 5, 4);
        ''',
        '''\
        INSERT INTO criminal (name, birthdate, sex, address, status, crime_type_id, victim_id, employee_id)
        VALUES
         ("", "", "", "", "", 1, 1, 1),
         ("", "", "", "", "", 2, 1, 2),
         ("", "", "", "", "", 3, 2, 3),
         ("", "", "", "", "", 4, 2, 4),
         ("", "", "", "", "", 5, 3, 5),
         ("", "", "", "", "", 1, 3, 6),
         ("", "", "", "", "", 2, 4, 7),
         ("", "", "", "", "", 3, 4, 8),
         ("", "", "", "", "", 4, 5, 9),
         ("", "", "", "", "", 5, 5, 10);
        '''
    ]

    return queries
