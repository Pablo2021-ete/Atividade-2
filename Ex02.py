import json

INVENTORY_FILE = "inventory.json"

def load_inventory():
    try:
        with open(INVENTORY_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory, file, indent=4)

def add_product(name, quantity, price):
    inventory = load_inventory()
    inventory.append({
        "name": name,
        "quantity": quantity,
        "price": price
    })
    save_inventory(inventory)
    print("Produto adicionado com sucesso!")

def list_products():
    inventory = load_inventory()
    total_value = sum(item["quantity"] * item["price"] for item in inventory)
    
    print("\nLista de Produtos no Estoque:")
    for i, item in enumerate(inventory, start=1):
        print(f"{i}. {item['name']} - Quantidade: {item['quantity']} - Preço: R${item['price']:.2f}")
    print(f"\nValor total do estoque: R${total_value:.2f}")

def main():
    while True:
        print("\nControle de Estoque")
        print("1. Adicionar Produto")
        print("2. Listar Produtos e Valor Total")
        print("3. Sair")
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            name = input("Nome do produto: ")
            quantity = int(input("Quantidade: "))
            price = float(input("Preço por unidade: "))
            add_product(name, quantity, price)
        elif choice == "2":
            list_products()
        elif choice == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
