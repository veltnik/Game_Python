import random

def guess_the_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    number_to_guess = random.randint(1, 100)  # Загадать число от 1 до 100
    attempts = 0

    while True:
        try:
            user_guess = int(input("Введите ваше предположение (от 1 до 100): "))
            attempts += 1
            
            if user_guess < 1 or user_guess > 100:
                print("Пожалуйста, введите число в пределах от 1 до 100.")
                continue
            
            if user_guess < number_to_guess:
                print("Слишком маленькое число! Попробуйте еще раз.")
            elif user_guess > number_to_guess:
                print("Слишком большое число! Попробуйте еще раз.")
            else:
                print(f"Поздравляю! Вы угадали число {number_to_guess} за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, введите целое число.")

if __name__ == "__main__":
    guess_the_number()
