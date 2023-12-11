#напишите программу для бинарного поиска загаданного числа
def binary_search(min_num, max_num):
    user_num = int(input("Введите целое число:"))
    center = (min_num+max_num)//2
    while True:
        print(f"Ваше число {center}?")
        check = input("Если больше > , если меньше < , если равно =")
        
        if check == ">":
            min_num = center
            center = (min_num+max_num)//2
        elif check == "<":
            max_num = center
            center = (min_num+max_num)//2
        elif check == "=":
            print(f"Я угадал!")
            break
        else:
            print("Я не знаю это число")
            break
binary_search(int(input("Минимальное число:")), int(input("Максимальное число:")))    
             
