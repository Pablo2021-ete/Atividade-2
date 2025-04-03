import json
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description, deadline):
    tasks = load_tasks()
    tasks.append({
        "description": description,
        "deadline": deadline,
        "completed": False
    })
    save_tasks(tasks)
    print("Tarefa adicionada com sucesso!")

def list_tasks():
    tasks = load_tasks()
    tasks.sort(key=lambda t: datetime.strptime(t["deadline"], "%Y-%m-%d"))
    for i, task in enumerate(tasks, start=1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{i}. {task['description']} - Prazo: {task['deadline']} [{status}]")

def mark_completed(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1]["completed"] = True
        save_tasks(tasks)
        print("Tarefa marcada como concluída!")
    else:
        print("Índice inválido.")

def main():
    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Sair")
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            desc = input("Descrição da tarefa: ")
            deadline = input("Prazo (YYYY-MM-DD): ")
            add_task(desc, deadline)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()
            index = int(input("Número da tarefa para concluir: "))
            mark_completed(index)
        elif choice == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
