def calculate():
    print("Добро пожаловать в калькулятор!")
    while True:
        operation = input("Выберите операцию (сложение +, вычитание -, умножение *, деление /) или 'выход' для завершения: ")
        if operation == 'выход':
            print("Спасибо за использование калькулятора!")
            break
        if operation not in ['+', '-', '*', '/']:
            print("Неверная операция. Пожалуйста, попробуйте снова.")
            continue

        try:
            number1 = float(input("Введите первое число: "))
            number2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка ввода! Пожалуйста, введите число.")
            continue

        if operation == '+':
            print("Результат:", number1 + number2)
        elif operation == '-':
            print("Результат:", number1 - number2)
        elif operation == '*':
            print("Результат:", number1 * number2)
        elif operation == '/':
            if number2 == 0:
                print("Ошибка: Деление на ноль!")
            else:
                print("Результат:", number1 / number2)

# Запуск калькулятора
calculate()
