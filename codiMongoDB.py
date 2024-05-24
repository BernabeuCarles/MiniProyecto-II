import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Conectar a la base de datos MongoDB
def connect_to_mongo():
    try:
        client = MongoClient('mongodb://admin:admin@localhost:27017/')
        client.admin.command('ping')  # Ping the server to check connection
        print("Conexión a MongoDB exitosa")
        return client
    except ConnectionFailure as e:
        print(f"No se puede conectar a MongoDB: {e}")
        messagebox.showerror('Error', 'No se puede conectar a MongoDB')
        raise SystemExit(e)

client = connect_to_mongo()
db = client['mydatabase']
agencia_collection = db['agencia']
manager_collection = db['manager']
model_collection = db['model']

# Función para insertar datos en la colección AGENCIA
def insert_agencia():
    nom = agencia_nom.get()
    email = agencia_email.get()
    
    if nom and email:
        data = {'nom': nom, 'email': email}
        try:
            agencia_collection.insert_one(data)
            messagebox.showinfo('Éxito', 'Datos insertados en AGENCIA')
        except Exception as e:
            messagebox.showerror('Error', f'Error insertando datos en AGENCIA: {e}')
    else:
        messagebox.showerror('Error', 'Por favor, introduce el nombre y el email de la agencia')

# Función para insertar datos en la colección MANAGER
def insert_manager():
    agencia_id = manager_agencia_id.get()
    nom = manager_nom.get()
    email = manager_email.get()
    nacionalitat = manager_nacionalitat.get()
    benefici = manager_benefici.get()
    
    if nom and email and nacionalitat and benefici:
        data = {
            'agencia_id': agencia_id if agencia_id else None,
            'nom': nom,
            'email': email,
            'nacionalitat': nacionalitat,
            'benefici': benefici
        }
        try:
            manager_collection.insert_one(data)
            messagebox.showinfo('Éxito', 'Datos insertados en MANAGER')
        except Exception as e:
            messagebox.showerror('Error', f'Error insertando datos en MANAGER: {e}')
    else:
        messagebox.showerror('Error', 'Por favor, introduce todos los datos del manager')

# Función para insertar datos en la colección MODEL
def insert_model():
    manager_id = model_manager_id.get()
    edat = model_edat.get()
    nom = model_nom.get()
    email = model_email.get()
    nacionalitat = model_nacionalitat.get()
    benefici = model_benefici.get()
    subscriptors = model_subscriptors.get()
    
    if edat and nom and email and nacionalitat and benefici and subscriptors:
        data = {
            'manager_id': manager_id if manager_id else None,
            'edat': int(edat),
            'nom': nom,
            'email': email,
            'nacionalitat': nacionalitat,
            'benefici': benefici,
            'subscriptors': int(subscriptors)
        }
        try:
            model_collection.insert_one(data)
            messagebox.showinfo('Éxito', 'Datos insertados en MODEL')
        except Exception as e:
            messagebox.showerror('Error', f'Error insertando datos en MODEL: {e}')
    else:
        messagebox.showerror('Error', 'Por favor, introduce todos los datos del modelo')

# Función para mostrar todas las agencias
def show_all_agencies():
    try:
        data = agencia_collection.find()
        
        show_window = tk.Toplevel()
        show_window.title("Todas las Agencias")
        
        text_widget = tk.Text(show_window)
        text_widget.pack()
        
        for row in data:
            text_widget.insert(tk.END, f"{row}\n")
    except Exception as e:
        messagebox.showerror('Error', f'Error mostrando agencias: {e}')

# Función para mostrar todos los modelos
def show_all_models():
    try:
        data = model_collection.find()
        
        show_window = tk.Toplevel()
        show_window.title("Todos los Modelos")
        
        text_widget = tk.Text(show_window)
        text_widget.pack()
        
        for row in data:
            text_widget.insert(tk.END, f"{row}\n")
    except Exception as e:
        messagebox.showerror('Error', f'Error mostrando modelos: {e}')

# Función para mostrar todos los managers
def show_all_managers():
    try:
        data = manager_collection.find()
        
        show_window = tk.Toplevel()
        show_window.title("Todos los Managers")
        
        text_widget = tk.Text(show_window)
        text_widget.pack()
        
        for row in data:
            text_widget.insert(tk.END, f"{row}\n")
    except Exception as e:
        messagebox.showerror('Error', f'Error mostrando managers: {e}')

# Función para mostrar los modelos sin manager asignado
def show_models_without_manager():
    try:
        data = model_collection.find({'manager_id': None})
        
        show_window = tk.Toplevel()
        show_window.title("Modelos sin Manager")
        
        text_widget = tk.Text(show_window)
        text_widget.pack()
        
        for row in data:
            text_widget.insert(tk.END, f"{row}\n")
    except Exception as e:
        messagebox.showerror('Error', f'Error mostrando modelos sin manager: {e}')

# Función para mostrar los managers sin agencia asignada
def show_managers_without_agency():
    try:
        data = manager_collection.find({'agencia_id': None})
        
        show_window = tk.Toplevel()
        show_window.title("Managers sin Agencia")
        
        text_widget = tk.Text(show_window)
        text_widget.pack()
        
        for row in data:
            text_widget.insert(tk.END, f"{row}\n")
    except Exception as e:
        messagebox.showerror('Error', f'Error mostrando managers sin agencia: {e}')

# Función para mostrar el menú principal
def show_main_menu(role):
    root = tk.Tk()
    root.title("OnlyData")

    # Sección para insertar agencias (solo para admin)
    if role == 'admin':
        tk.Label(root, text="Nombre Agencia:").grid(row=0, column=0)
        global agencia_nom
        agencia_nom = tk.Entry(root)
        agencia_nom.grid(row=0, column=1)
        tk.Label(root, text="Email Agencia:").grid(row=1, column=0)
        global agencia_email
        agencia_email = tk.Entry(root)
        agencia_email.grid(row=1, column=1)

        insert_agencia_btn = tk.Button(root, text="Insertar Agencia", command=insert_agencia)
        insert_agencia_btn.grid(row=2, column=0, columnspan=2)

        # Sección para insertar managers
        tk.Label(root, text="ID Agencia Manager:").grid(row=3, column=0)
        global manager_agencia_id
        manager_agencia_id = tk.Entry(root)
        manager_agencia_id.grid(row=3, column=1)
        tk.Label(root, text="Nombre Manager:").grid(row=4, column=0)
        global manager_nom
        manager_nom = tk.Entry(root)
        manager_nom.grid(row=4, column=1)
        tk.Label(root, text="Email Manager:").grid(row=5, column=0)
        global manager_email
        manager_email = tk.Entry(root)
        manager_email.grid(row=5, column=1)
        tk.Label(root, text="Nacionalidad Manager:").grid(row=6, column=0)
        global manager_nacionalitat
        manager_nacionalitat = tk.Entry(root)
        manager_nacionalitat.grid(row=6, column=1)
        tk.Label(root, text="Beneficio Manager:").grid(row=7, column=0)
        global manager_benefici
        manager_benefici = tk.Entry(root)
        manager_benefici.grid(row=7, column=1)

        insert_manager_btn = tk.Button(root, text="Insertar Manager", command=insert_manager)
        insert_manager_btn.grid(row=8, column=0, columnspan=2)

        # Sección para insertar modelos
        tk.Label(root, text="ID Manager Modelo:").grid(row=9, column=0)
        global model_manager_id
        model_manager_id = tk.Entry(root)
        model_manager_id.grid(row=9, column=1)
        tk.Label(root, text="Edad Modelo:").grid(row=10, column=0)
        global model_edat
        model_edat = tk.Entry(root)
        model_edat.grid(row=10, column=1)
        tk.Label(root, text="Nombre Modelo:").grid(row=11, column=0)
        global model_nom
        model_nom = tk.Entry(root)
        model_nom.grid(row=11, column=1)
        tk.Label(root, text="Email Modelo:").grid(row=12, column=0)
        global model_email
        model_email = tk.Entry(root)
        model_email.grid(row=12, column=1)
        tk.Label(root, text="Nacionalidad Modelo:").grid(row=13, column=0)
        global model_nacionalitat
        model_nacionalitat = tk.Entry(root)
        model_nacionalitat.grid(row=13, column=1)
        tk.Label(root, text="Beneficio Modelo:").grid(row=14, column=0)
        global model_benefici
        model_benefici = tk.Entry(root)
        model_benefici.grid(row=14, column=1)
        tk.Label(root, text="Suscriptores Modelo:").grid(row=15, column=0)
        global model_subscriptors
        model_subscriptors = tk.Entry(root)
        model_subscriptors.grid(row=15, column=1)

        insert_model_btn = tk.Button(root, text="Insertar Modelo", command=insert_model)
        insert_model_btn.grid(row=16, column=0, columnspan=2)

    # Sección para mostrar "sin"
    tk.Label(root, text="Mostrar Sin:", font=('Helvetica', 12, 'bold')).grid(row=17, column=0, columnspan=2)

    show_models_without_manager_btn = tk.Button(root, text="Modelos sin Manager", command=show_models_without_manager)
    show_models_without_manager_btn.grid(row=18, column=0, columnspan=2)

    show_managers_without_agency_btn = tk.Button(root, text="Managers sin Agencia", command=show_managers_without_agency)
    show_managers_without_agency_btn.grid(row=19, column=0, columnspan=2)

    # Sección para mostrar "todos"
    tk.Label(root, text="Mostrar Todos:", font=('Helvetica', 12, 'bold')).grid(row=20, column=0, columnspan=2)

    show_all_agencies_btn = tk.Button(root, text="Todas las Agencias", command=show_all_agencies)
    show_all_agencies_btn.grid(row=21, column=0, columnspan=2)

    show_all_models_btn = tk.Button(root, text="Todos los Modelos", command=show_all_models)
    show_all_models_btn.grid(row=22, column=0, columnspan=2)

    show_all_managers_btn = tk.Button(root, text="Todos los Managers", command=show_all_managers)
    show_all_managers_btn.grid(row=23, column=0, columnspan=2)

    root.mainloop()

# Función para validar las credenciales
def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    if username == 'admin' and password == 'admin':
        login_window.destroy()
        show_main_menu('admin')
    elif username == 'user' and password == 'user':
        login_window.destroy()
        show_main_menu('user')
    else:
        messagebox.showerror('Error', 'Credenciales incorrectas')

# Ventana de inicio de sesión
login_window = tk.Tk()
login_window.title("Inicio de Sesión")

tk.Label(login_window, text="Usuario:").grid(row=0, column=0)
username_entry = tk.Entry(login_window)
username_entry.grid(row=0, column=1)

tk.Label(login_window, text="Contraseña:").grid(row=1, column=0)
password_entry = tk.Entry(login_window, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(login_window, text="Iniciar Sesión", command=validate_login)
login_button.grid(row=2, column=0, columnspan=2)

login_window.mainloop()
