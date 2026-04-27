"""Laboratorio 8 - Módulo de persistencia para lista de tareas."""

def read_todo_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        print(f"File {file_path} not found! Returning an empty to-do list.")
        # Creamos el archivo vacío para que el test pueda leerlo después
        open(file_path, 'w').close() 
        return []

def write_todo_file(file_path, tasks):
    """Writes the list of tasks to the file."""
    with open(file_path, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")
