import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 8,
    "D": 12,
}

symbol_value = {
    "A": 10,
    "B": 6,
    "C": 4,
    "D": 2,
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], "| ", end="")
            else:
                print(column[row])


def deposit(balance):
    while True:
        amount = input("How much money to deposit?\n$")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero")
        else:
            print("Please enter a number.")
    balance += amount
    return balance


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?""\n")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")
    return lines


def get_bet():
    while True:
        amount = input("How much money to bet on each line?\n")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def spin(balance):
    if balance == 0 or balance is None:
        print("Add more money to the slot machine to play, or quit")
        return
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        if bet == 0:
            break
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines.\nTotal bet is equal to: ${total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings}.")
    print(f"you won on lines:", end="")
    if not winning_lines:
        print("None")
    else:
        for _ in range(len(winning_lines)):
            print(f" {winning_lines[_]}")
    balance += winnings - total_bet
    return int(balance)


def main():
    balance = 0
    balance = deposit(balance)
    flag = 0
    while True:
        print(f"Current balance is ${balance}")
        print("Do you want to spin the machine? (Yes/No)")
        yes_or_no = input()
        if yes_or_no == "Yes":
            balance = spin(balance)
            if balance is None:
                balance = 0
                flag = 1
            if flag == 0:
                print(f"Your new balance is: ${balance}")
        if yes_or_no == "No" or flag == 1:
            quit_machine = input("Do you want to quit? (Yes/No)\n")
            if quit_machine == "Yes":
                print(f"you are withdrawing ${balance}, thank you and goodbye!")
                break
            else:
                more_money = input("Deposit more money?(Yes/No)\n")
                if more_money == "Yes":
                    balance = deposit(balance)
                    flag = 0


main()
