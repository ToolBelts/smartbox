import sqlite3


class Ideas:

    def __init__(self, _id, title, description, vote):
        self.id = _id
        self.title = title
        self.description = description
        self.vote = vote

    @classmethod
    def save(cls, title, description):
        conn = sqlite3.connect("config/data.db")
        cursor = conn.cursor()
        query = "insert into ideas(title, description) values (?,?)"
        cursor.execute(query, (title, description))
        conn.commit()

    @classmethod
    def find_by_id(cls, _id):
        conn = sqlite3.connect("config/data.db")
        cursor = conn.cursor()
        query = "select * from ideas where id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        return cls(*row)

    @classmethod
    def find_all(cls):
        conn = sqlite3.connect("config/data.db")
        cursor = conn.cursor()
        query = "select * from ideas"
        results = cursor.execute(query)
        return list(map(lambda x: cls(*x), results))

    @classmethod
    def make_vote(cls, item):
        conn = sqlite3.connect("config/data.db")
        cursor = conn.cursor()
        vote = item.vote + 1
        query = "update ideas set vote=? where id=?"
        cursor.execute(query, (vote, item.id))
        conn.commit()
