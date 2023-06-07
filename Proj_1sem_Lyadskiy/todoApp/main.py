import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, \
    QTextEdit, QPushButton, QListWidget, QListWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from database import DatabaseManager


class NoteWidget(QWidget):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.note_id = None  # Идентификатор текущей заметки
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.title_label = QLabel('Заголовок:')
        self.title_edit = QLineEdit()

        self.content_label = QLabel('Содержимое:')
        self.content_edit = QTextEdit()

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.save_note)

        self.delete_button = QPushButton('Удалить')
        self.delete_button.clicked.connect(self.delete_note)

        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.title_edit)
        self.layout.addWidget(self.content_label)
        self.layout.addWidget(self.content_edit)
        self.layout.addWidget(self.save_button)
        self.layout.addWidget(self.delete_button)

        self.setLayout(self.layout)

    def load_note(self, note_id):
        # Загрузка заметки из базы данных
        self.note_id = note_id
        result = self.db_manager.get_note_by_id(note_id)

        if result:
            self.title_edit.setText(result[0])
            self.content_edit.setPlainText(result[1])

    def save_note(self):
        # Сохранение заметки в базу данных
        title = self.title_edit.text()
        content = self.content_edit.toPlainText()

        note_id = self.db_manager.save_note(self.note_id, title, content)
        self.note_id = note_id

        # Update note list in the NotesWindow
        self.window().load_notes()

        QMessageBox.information(self, 'Сохранение', 'Заметка сохранена успешно.')

        # Очищает поля после создания/редактирования заметки
        self.note_id = None
        self.title_edit.clear()
        self.content_edit.clear()
        self.window().load_notes()

    def delete_note(self):
        # Удаление заметки из базы данных
        if self.note_id:
            self.db_manager.delete_note_by_id(self.note_id)

            # Очищает поля после создания/редактирования заметки
            self.note_id = None
            self.title_edit.clear()
            self.content_edit.clear()

            # Обновление списка с заметками
            self.window().load_notes()

            QMessageBox.information(self, 'Удаление', 'Заметка удалена успешно.')


class NotesWindow(QMainWindow):
    def __init__(self, db_manager):
        super().__init__()
        self.db_manager = db_manager
        self.setWindowTitle('Менеджер заметок')
        self.setFixedSize(600, 400)
        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.layout = QHBoxLayout()

        self.note_list = QListWidget()
        self.note_list.setMaximumWidth(200)
        self.note_list.itemSelectionChanged.connect(self.load_note)

        self.note_widget = NoteWidget(self.db_manager)

        self.layout.addWidget(self.note_list)
        self.layout.addWidget(self.note_widget)

        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.load_notes()

    def load_notes(self):
        # Загрузка списка заметок из базы данных
        self.note_list.clear()

        result = self.db_manager.get_all_notes()

        for note in result:
            item = QListWidgetItem(note[1])
            item.setData(Qt.UserRole, note[0])
            self.note_list.addItem(item)

    def load_note(self):
        # Загрузка выбранной заметки
        selected_item = self.note_list.currentItem()
        if selected_item:
            note_id = selected_item.data(Qt.UserRole)
            self.note_widget.load_note(note_id)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    db_manager = DatabaseManager()

    window = NotesWindow(db_manager)
    window.show()

    sys.exit(app.exec_())