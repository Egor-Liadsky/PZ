import sqlite3


class DatabaseManager:
    def __init__(self, db_name='notes.db'):
        self.db_name = db_name
        self.create_table()

    def create_table(self):
        conn = self.get_connection()
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT)")
        conn.commit()
        conn.close()

    def get_connection(self):
        return sqlite3.connect(self.db_name)

    def get_all_notes(self):
        conn = self.get_connection()
        c = conn.cursor()
        c.execute("SELECT id, title FROM notes")
        result = c.fetchall()
        conn.close()
        return result

    def get_note_by_id(self, note_id):
        conn = self.get_connection()
        c = conn.cursor()
        c.execute("SELECT title, content FROM notes WHERE id=?", (note_id,))
        result = c.fetchone()
        conn.close()
        return result

    def save_note(self, note_id, title, content):
        conn = self.get_connection()
        c = conn.cursor()

        if note_id:
            # Редактирование существующей заметки
            c.execute("UPDATE notes SET title=?, content=? WHERE id=?", (title, content, note_id))
        else:
            # Создание новой заметки
            c.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
            note_id = c.lastrowid

        conn.commit()
        conn.close()
        return note_id

    def delete_note_by_id(self, note_id):
        conn = self.get_connection()
        c = conn.cursor()
        c.execute("DELETE FROM notes WHERE id=?", (note_id,))
        conn.commit()
        conn.close()