import datetime
import json
from tkinter import Tk, ttk
from tkinter import *
import requests


class MainScreen(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('325x500+450+150')
        self.title("Todo App")
        self.config(bg='#F1F3F5')
        self.resizable(False, False)

        response = requests.get("http://127.0.0.1:8087/api/notes")
        print(json.loads(response.content))

        self.data = json.loads(response.content)

        create_button = Button(self, text='Создать', font=('Arial', 10, 'bold'), bg='#4CAF50', fg='white',
                               command=self.open_create_note_window)
        create_button.pack(pady=5)

        self.name_entry = None
        self.desc_entry = None

        self.canvas = Canvas(self, bg='#F1F3F5', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)

        self.frame = Frame(self.canvas, bg='#F1F3F5')
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')

        self.scrollbar = ttk.Scrollbar(self.canvas, orient='vertical', command=self.canvas.yview)
        self.scrollbar.pack(side='right', fill='y')

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', self.on_canvas_configure)
        self.canvas.bind_all('<MouseWheel>', self.on_mousewheel)

        self.create_note_cards()

    def on_canvas_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units')

    def create_note_cards(self):
        for i, note in enumerate(self.data):
            frame = Frame(self.frame, bg='white', padx=10, pady=10)
            frame.pack(pady=5)

            name_label = Label(frame, text=note["title"], font=('Arial', 12, 'bold'), bg='white')
            name_label.pack(anchor='center')

            desc_label = Label(frame, text=note["description"], font=('Arial', 10), bg='white')
            desc_label.pack(anchor='w')

            date_label = Label(frame, text=note["date"], font=('Arial', 10), bg='white')
            date_label.pack(anchor='w')

            context_menu = Menu(frame, tearoff=0)
            context_menu.add_command(label="Редактировать", command=lambda note=note: self.edit_note_entry(note))
            context_menu.add_command(label="Удалить", command=lambda note=note: self.delete_note_entry(note))

            frame.bind("<Button-3>", lambda event, menu=context_menu: menu.post(event.x_root, event.y_root))

    def edit_note_entry(self, note):
        edit_note_window = Toplevel(self)
        edit_note_window.title("Редактирование заметки")
        edit_note_window.geometry('325x580+450+150')
        edit_note_window.config(bg='#F1F3F5')
        edit_note_window.resizable(False, False)

        label = Label(edit_note_window, text='Редактирование заметки', font=('Arial', 12, 'bold'), bg='#F1F3F5')
        label.pack(pady=5)

        name_label = Label(edit_note_window, text='Название заметки:', font=('Arial', 10), bg='#F1F3F5')
        name_label.pack(pady=5)

        name_entry = Entry(edit_note_window, font=('Arial', 10))
        name_entry.insert(0, note["title"])
        name_entry.pack(pady=5)

        desc_label = Label(edit_note_window, text='Описание:', font=('Arial', 10), bg='#F1F3F5')
        desc_label.pack(pady=5)

        desc_entry = Text(edit_note_window, font=('Arial', 10), wrap='word')
        desc_entry.insert("1.0", note["description"])
        desc_entry.pack(pady=5, fill='none')

        update_button = Button(edit_note_window, text='Обновить', font=('Arial', 10, 'bold'), bg='#4CAF50', fg='white',
                               command=lambda: self.update_note_entry(edit_note_window, note, name_entry.get(),
                                                                      desc_entry.get("1.0", "end-1c")))
        update_button.pack(pady=5)

    def update_note_entry(self, edit_note_window, note, name, description):
        note["title"] = name
        note["description"] = description
        id = note["id"]

        data = {"title": name, "description": description, "date": f"{datetime.datetime.now().date()}"}
        print(note)
        requests.put(f"http://127.0.0.1:8087/api/notes/{id}", json=data)
        self.update_data()

        edit_note_window.destroy()

    def delete_note_entry(self, note):
        print(f"Deleting note: {note['title']}")
        requests.delete(f"http://127.0.0.1:8087/api/notes/{note['id']}")
        self.update_data()

    def open_create_note_window(self):
        create_note_window = Toplevel(self)
        create_note_window.title("Создание заметки")
        create_note_window.geometry('325x350+450+150')
        create_note_window.config(bg='#F1F3F5')
        create_note_window.resizable(False, False)

        label = Label(create_note_window, text='Создание заметки', font=('Arial', 12, 'bold'), bg='#F1F3F5')
        label.pack(pady=5)

        name_label = Label(create_note_window, text='Название заметки:', font=('Arial', 10), bg='#F1F3F5')
        name_label.pack(pady=5)

        self.name_entry = Entry(create_note_window, font=('Arial', 10))
        self.name_entry.pack(pady=5)

        desc_label = Label(create_note_window, text='Описание:', font=('Arial', 10), bg='#F1F3F5')
        desc_label.pack(pady=5)

        self.desc_entry = Text(create_note_window, font=('Arial', 10), height=10, wrap='word')
        self.desc_entry.pack(pady=5, fill='none', expand=True)

        create_button = Button(create_note_window, text='Создать', font=('Arial', 10, 'bold'), bg='#4CAF50', fg='white',
                               command=lambda: self.create_note_entry(create_note_window, self.name_entry.get(),
                                                                      self.desc_entry.get("1.0", "end-1c")))
        create_button.pack(pady=5)

    def create_note_entry(self, create_note_window, name, description):
        data = {"title": name, "description": description, "date": f"{datetime.datetime.now().date()}"}
        print(data)
        requests.post("http://127.0.0.1:8087/api/notes", json=data)
        self.update_data()
        create_note_window.destroy()

    def get_notes(self):
        response = requests.get("http://127.0.0.1:8087/api/notes")
        self.data = response.json()

    def update_data(self):
        self.frame.destroy()
        self.frame = Frame(self.canvas, bg='#F1F3F5')
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')
        self.get_notes()
        self.create_note_cards()

        self.canvas.update()  # Обновляем состояние скролла
