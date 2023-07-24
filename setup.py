import os

if not os.path.exists('installed.txt'):
    print("Запуск установщика...")
    print("Установка начата...")
    
    def setups():
        choice = input("Введите номер выбранного типа: ")
        
        if choice == "1":
            print("Вы выбрали быструю установку.")
            while label:
                if label == 1:
                    print("Метка 1")
                    
                elif choice == "2":
                    def user_installation():
                        print("Добро пожаловать в пользовательскую установку!")
                        print("Вашы параметры = {x}")
                        choice = input("Введите номер выбранного типа: ")
                        # продолжайте код с дополнительными строками

                    # вызовите функцию
                    user_installation()
                    
                else:
                    print("Некорректный выбор. Попробуй еще раз.")
    
    setups()
    
    with open('installed.txt', 'w') as file:
        file.write('Installation complete data a save :).')

    with open('setup_system.ini.txt', 'w') as file:
        file.write('internet_settings=Your_ip Defender_settings=Streng.')
        os.makedirs("Puhist/Desktop")
        
    label = 1
    
else:
    print("Установка уже выполнена.")
    
print("Установка завершена!")