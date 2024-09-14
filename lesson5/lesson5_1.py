import lesson5_2

while True:
    kg=0  #清除變數
    cm=0  #清除變數
    cm,kg = lesson5_2.input_data()

    print(f'身高={cm},體重={kg}')
    BMI = lesson5_2.my_bmi(cm=cm, kg=kg)
    print(f'BMI={BMI}')

    print(lesson5_2.get_status(BMI))

    play_again = input("還要繼續嗎?(y,n)")
    if play_again == "n":
        break
print('程式結束')