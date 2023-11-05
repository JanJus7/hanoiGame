A = []
B = []
C = []
moves = []


def append_the_tower(amount):
    for i in range(amount, 0, -1):
        A.append(i)


def print_the_tower(amount):
    for i in ("A", "B", "C"):
        print(i + " " * (amount * 4 - 1), end="")
    print()
    for i in range(amount, 0, -1):
        a = A[i - 1] if i <= len(A) else None
        b = B[i - 1] if i <= len(B) else None
        c = C[i - 1] if i <= len(C) else None
        if a:
            str_a = str("_" * a + " " * (amount * 4 - a))
        else:
            str_a = str("|" + " " * (amount * 4 - 1))
        if b:
            str_b = str("_" * b + " " * (amount * 4 - b))
        else:
            str_b = str("|" + " " * (amount * 4 - 1))
        if c:
            str_c = str("_" * c + " " * (amount * 4 - c))
        else:
            str_c = str("|" + " " * (amount * 4 - 1))
        print(str_a + str_b + str_c)


def check_the_win(amount, current_move):
    if len(B) == amount:
        print("\nGratulacje! Udało ci się wygrać!")
        print("Tyle wynosiła twoja ilość ruchów: ", current_move)
        print()
        print("Zaraz przekierujemy cię do menu!\n\n\n\n\n\n\n\n\n")
        B.clear()
        A.clear()
        C.clear()
        display_menu()


def wana_play(amount):
    current_move = 0
    print()
    print("Twoim celem jest przenieść całą wieżę na słupek \"B\"")
    print(
        "Żeby wykonać ruch, musisz napisać z jakiego słupka na jaki chcesz przesunąć element. \nNa przykład żeby "
        "wykonać ruch z słupka \"A\" na słupek \"B\" musisz napisać \"AB\".")
    print()
    print("Pamiętaj że w swoim ruchu możesz wpisać \"end\" żeby wyjść z gry :D")
    print_the_tower(amount)
    while True:
        player_move = str(input("Wpisz swój ruch: "))
        current_move = current_move + 1
        if player_move == "end":
            print("No dobrze...")
            exit(777)
        else:
            if len(player_move) != 2:
                print("BŁĄD! Podaj swój ruch jeszcze raz...")
                current_move = current_move - 1
            else:
                if player_move.upper() == "AB":
                    if len(A) == 0:
                        print("Słupek A jest pusty, podaj inny słupek początkowy...")
                        current_move = current_move - 1
                    else:
                        if len(B) != 0 and A[-1] > B[-1]:
                            print("Błąd! Nie możesz położyć większy na mniejszy!")
                            current_move = current_move - 1
                        else:
                            movment_of_the_brick = A.pop()
                            B.append(movment_of_the_brick)
                elif player_move.upper() == "BC":
                    if len(B) == 0:
                        print("Słupek B jest pusty, podaj inny słupek początkowy...")
                        current_move = current_move - 1
                    else:
                        if len(C) != 0 and B[-1] > C[-1]:
                            print("Błąd! Nie możesz położyć większy na mniejszy!")
                            current_move = current_move - 1
                        else:
                            movment_of_the_brick = B.pop()
                            C.append(movment_of_the_brick)
                elif player_move.upper() == "BA":
                    if len(B) == 0:
                        print("Słupek B jest pusty, podaj inny słupek początkowy...")
                        current_move = current_move - 1
                    else:
                        if len(A) != 0 and B[-1] > A[-1]:
                            print("Błąd! Nie możesz położyć większy na mniejszy!")
                            current_move = current_move - 1
                        else:
                            movment_of_the_brick = B.pop()
                            A.append(movment_of_the_brick)
                elif player_move.upper() == "AC":
                    if len(A) == 0:
                        print("Słupek A jest pusty, podaj inny słupek początkowy...")
                        current_move = current_move - 1
                    else:
                        if len(C) != 0 and A[-1] > C[-1]:
                            print("Błąd! Nie możesz położyć większy na mniejszy!")
                            current_move = current_move - 1
                        else:
                            movment_of_the_brick = A.pop()
                            C.append(movment_of_the_brick)
                elif player_move.upper() == "CB":
                    if len(C) == 0:
                        print("Słupek C jest pusty, podaj inny słupek początkowy...")
                        current_move = current_move - 1
                    else:
                        if len(B) != 0 and C[-1] > B[-1]:
                            print("Błąd! Nie możesz położyć większy na mniejszy!")
                            current_move = current_move - 1
                        else:
                            movment_of_the_brick = C.pop()
                            B.append(movment_of_the_brick)
                elif player_move.upper() == "CA":
                    if len(C) == 0:
                        print("Słupek C jest pusty, podaj inny słupek początkowy...")
                        current_move = current_move - 1
                    else:
                        if len(A) != 0 and C[-1] > A[-1]:
                            print("Błąd! Nie możesz położyć większy na mniejszy!")
                            current_move = current_move - 1
                        else:
                            movment_of_the_brick = C.pop()
                            A.append(movment_of_the_brick)
                else:
                    print("BŁĄD! Podaj swój ruch jeszcze raz...")
                    current_move = current_move - 1
            print("Ilość aktualnie wykonanych ruchów wynosi: ", current_move)
            print_the_tower(amount)
            check_the_win(amount, current_move)


def on_my_own(amount):
    wanahelp = str(input("Chcesz żeby program rozwiązał to za ciebie czy próbujesz samemu? (samemu/program) "))
    while True:
        if wanahelp == "samemu":
            print("Wspaniale! Wyzwanie zaraz się rozpocznie! ;D")
            wana_play(amount)
        elif wanahelp == "program":
            print("Dobrze, problem ten za ciebie rozwiąże program :D")
            auto_solve(amount, 'A', 'B', 'C')
            print(moves)
            current_move = 0
            while True:
                player_move = moves.pop(0)
                current_move = current_move + 1
                if player_move.upper() == "AB":
                    movment_of_the_brick = A.pop()
                    B.append(movment_of_the_brick)
                elif player_move.upper() == "BC":
                    movment_of_the_brick = B.pop()
                    C.append(movment_of_the_brick)
                elif player_move.upper() == "BA":
                    movment_of_the_brick = B.pop()
                    A.append(movment_of_the_brick)
                elif player_move.upper() == "AC":
                    movment_of_the_brick = A.pop()
                    C.append(movment_of_the_brick)
                elif player_move.upper() == "CB":
                    movment_of_the_brick = C.pop()
                    B.append(movment_of_the_brick)
                elif player_move.upper() == "CA":
                    movment_of_the_brick = C.pop()
                    A.append(movment_of_the_brick)
                print("Ilość aktualnie wykonanych ruchów wynosi: ", current_move)
                print_the_tower(amount)
                check_the_win(amount, current_move)
        print()
        print("Zaraz przekierujemy cię do menu!\n\n\n\n\n\n\n\n\n")
        A.clear()
        B.clear()
        C.clear()
        display_menu()
        break


def display_menu():
    print("Witaj w grze o wieżach Hanoi!")
    fchoice = str(input("Czy chcesz podjąć wyzwanie? (tak/nie) "))
    while True:
        if fchoice == "tak":
            amount = input("Podaj z ilu klocków chcesz zbudować wieźę: ")
            try:
                amount = int(amount)
            except ValueError:
                print("BŁĄD! Podaj LICZBĘ!")
                continue
            if amount > 0:
                append_the_tower(amount)
                print_the_tower(amount)
                on_my_own(amount)
            elif amount <= 0:
                print("Błąd! Podaj liczbę dodatnią większą od 0.\n")
                continue
        elif fchoice == "nie":
            print("No trudno... Do zobaczenia kiedy indziej.")
            exit(340)
        else:
            print("BŁĄD! Wprowadź wartość jeszcze raz...\n")
            display_menu()


def auto_solve(n, source, destination, auxiliary):
    if n == 1:
        moves.append(source + destination)
        return
    auto_solve(n - 1, source, auxiliary, destination)
    moves.append(source + destination)
    auto_solve(n - 1, auxiliary, destination, source)


display_menu()
