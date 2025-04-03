import json

SEATS_FILE = "seats.json"
ROWS, COLS = 5, 5  # Define o tamanho do mapa de assentos

def load_seats():
    try:
        with open(SEATS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return [["O" for _ in range(COLS)] for _ in range(ROWS)]  # 'O' representa assento livre

def save_seats(seats):
    with open(SEATS_FILE, "w") as file:
        json.dump(seats, file)

def display_seats(seats):
    print("\nMapa de Assentos:")
    print("  " + " ".join(str(i) for i in range(COLS)))
    for i, row in enumerate(seats):
        print(str(i) + " " + " ".join(row))

def reserve_seat(row, col):
    seats = load_seats()
    if seats[row][col] == "O":
        seats[row][col] = "X"  # 'X' representa assento reservado
        save_seats(seats)
        print("Reserva efetuada com sucesso!")
    else:
        print("Este assento já está reservado.")

def cancel_reservation(row, col):
    seats = load_seats()
    if seats[row][col] == "X":
        seats[row][col] = "O"
        save_seats(seats)
        print("Reserva cancelada com sucesso!")
    else:
        print("Este assento não está reservado.")

def main():
    while True:
        print("\nSistema de Reservas de Eventos")
        print("1. Visualizar mapa de assentos")
        print("2. Reservar um assento")
        print("3. Cancelar uma reserva")
        print("4. Sair")
        choice = input("Escolha uma opção: ")
        
        if choice == "1":
            display_seats(load_seats())
        elif choice == "2":
            display_seats(load_seats())
            row = int(input("Informe a linha do assento: "))
            col = int(input("Informe a coluna do assento: "))
            reserve_seat(row, col)
        elif choice == "3":
            display_seats(load_seats())
            row = int(input("Informe a linha do assento: "))
            col = int(input("Informe a coluna do assento: "))
            cancel_reservation(row, col)
        elif choice == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
