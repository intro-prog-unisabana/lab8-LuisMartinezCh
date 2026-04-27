"""Laboratorio 8 - CLI del gestor de tareas."""

import sys
from todo_manager import read_todo_file, write_todo_file

def main():
    try:
        # Validación inicial de argumentos
        if len(sys.argv) < 2:
            raise IndexError("Insufficient arguments provided!")

        # Manejo del comando --help
        if sys.argv[1] == "--help":
            print("""Usage: python main.py <file_path> <command> [arguments]...
Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.
Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view""")
            return
# El primer argumento es la ruta del archivo
        file_path = sys.argv[1]
        tasks = read_todo_file(file_path)
        
        # Procesar comandos a partir del índice 2
        i = 2
        modified = False # Para saber si debemos guardar el archivo al final

        while i < len(sys.argv):
            command = sys.argv[i]

            if command == "view":
                print("Tasks:")
                for t in tasks:
                    print(t)
                i += 1

            elif command == "add":
                if i + 1 >= len(sys.argv):
                    raise IndexError('Task description required for "add".')
                new_task = sys.argv[i+1]
                tasks.append(new_task)
                print(f'Task "{new_task}" added.')
                modified = True
                i += 2 # Saltar el comando y su argumento
            elif command == "remove":
                if i + 1 >= len(sys.argv):
                    raise IndexError('Task description required for "remove".')
                task_to_remove = sys.argv[i+1]
                if task_to_remove in tasks:
                    tasks.remove(task_to_remove)
                    print(f'Task "{task_to_remove}" removed.')
                    modified = True
                else:
                    print(f'Task "{task_to_remove}" not found.')
                i += 2 # Saltar el comando y su argumento

            else:
                raise ValueError("Command not found!")

        # Escritura optimizada (una sola vez al final)
        if modified:
            write_todo_file(file_path, tasks)