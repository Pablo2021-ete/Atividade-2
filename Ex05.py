import json

CONTACTS_FILE = "contacts.json"

def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(name, phone, email):
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contato adicionado com sucesso!")

def search_contact(name):
    contacts = load_contacts()
    results = [c for c in contacts if name.lower() in c["name"].lower()]
    if results:
        print("\nContatos encontrados:")
        for contact in results:
            print(f"Nome: {contact['name']}, Telefone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("Nenhum contato encontrado.")

def main():
    while True:
        print("\nGerenciador de Contatos")
        print("1. Adicionar Contato")
        print("2. Buscar Contato")
        print("3. Sair")
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            name = input("Nome: ")
            phone = input("Telefone: ")
            email = input("Email: ")
            add_contact(name, phone, email)
        elif choice == "2":
            name = input("Nome para busca: ")
            search_contact(name)
        elif choice == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
