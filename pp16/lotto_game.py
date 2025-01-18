from lotto import get_user_numbers, draw_numbers, check_user_numbers

print("Witaj w grze Lotto!")
user_numbers = get_user_numbers()
print("Pobrane liczby to: ", user_numbers)

print("\n Naciśnij ENTER aby dokonać losowania liczb!\n")
input()

lucky_numbers = draw_numbers()
print("Wylosowano liczby:", lucky_numbers)
print()

result = check_user_numbers(user_numbers, lucky_numbers)
if result ==6:
    print("Brawo! Jesteś milionerem!")
elif result ==5:
    print("Brawo! Trafiłeś piątkę!")
elif result ==4:
    print("Brawo! trafiłeś czwórke")
elif result ==3:
    print("Brawo! trafiłeś tórjke")
elif result ==2 or result ==1:
    print("Trafiono {} liczbę/y. Było bardzo blisko!".format(result))
else:
    print("NIestety nic nie wygrałeś!")