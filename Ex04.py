import json

USERS_FILE = "users.json"

# Função para carregar usuários

def load_users():
    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)

def create_account(username, password):
    users = load_users()
    if username in users:
        print("Nome de usuário já existe!")
        return False
    users[username] = {"password": password, "balance": 0.0, "transactions": []}
    save_users(users)
    print("Conta criada com sucesso!")
    return True

def login(username, password):
    users = load_users()
    if username in users and users[username]["password"] == password:
        return users[username]
    print("Login falhou! Verifique suas credenciais.")
    return None

def deposit(username, amount):
    users = load_users()
    users[username]["balance"] += amount
    users[username]["transactions"].append(f"Depósito de R${amount:.2f}")
    save_users(users)
    print(f"Depósito de R${amount:.2f} realizado!")

def withdraw(username, amount):
    users = load_users()
    if users[username]["balance"] >= amount:
        users[username]["balance"] -= amount
        users[username]["transactions"].append(f"Saque de R${amount:.2f}")
        save_users(users)
        print(f"Saque de R${amount:.2f} realizado!")
    else:
        print("Saldo insuficiente!")

def view_transactions(username):
    users = load_users()
    print("\nHistórico de Transações:")
    for transaction in users[username]["transactions"]:
        print(transaction)

def main():
    while True:
        print("\nSistema Bancário")
        print("1. Criar Conta")
        print("2. Login")
        print("3. Sair")
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            username = input("Nome de usuário: ")
            password = input("Senha: ")
            create_account(username, password)
        elif choice == "2":
            username = input("Nome de usuário: ")
            password = input("Senha: ")
            user = login(username, password)
            if user:
                while True:
                    print("\n1. Depositar")
                    print("2. Sacar")
                    print("3. Ver Transações")
                    print("4. Sair")
                    option = input("Escolha uma opção: ")
                    if option == "1":
                        amount = float(input("Valor do depósito: "))
                        deposit(username, amount)
                    elif option == "2":
                        amount = float(input("Valor do saque: "))
                        withdraw(username, amount)
                    elif option == "3":
                        view_transactions(username)
                    elif option == "4":
                        break
                    else:
                        print("Opção inválida!")
        elif choice == "3":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
