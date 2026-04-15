from database.connection import connect_db
# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files,
# tool windows, actions, and settings.


def mainProgram():
    while input("Digite um número: ") > "10":
        print("Iniciando o programa...")
        connect_db()


if __name__ == '__main__':
    mainProgram()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
