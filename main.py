from PIL import ImageGrab
import numpy as np
import pytesseract
import time
import re
import keyboard


pytesseract.pytesseract.tesseract_cmd = 'F:/Program Files (x86)/tesserat/tesseract.exe'
# print(pytesseract.get_languages(config=''))

col = 0

def read_screen(answers: list):
    print("////////")
    global col
    col += 1
    print(str(col))
    print("////////")

    screen = np.array(ImageGrab.grab(bbox=(5, 100, 1480, 1030)))

    text = pytesseract.image_to_string(screen, lang='rus')

    print("readed from image")
    print(text)
    print("*********************************************")


    result = re.findall(r'([вВ]опрос [\d]*)([\d\D]*)(а.[\d\D]*)([пП]равила[\d\D]*)(\n\n[пП]равильный ответ:)([\d\D]*)([пП]редыдущий)', text)

    print("all groups")
    print(len(result))

    try:
        print(len(result[0]))
    except Exception:
        print("len=0")
        pass
    else:


        # for i in range(len(result[0])):
        #     print(result[0][i])

        print("*********************************************")
        print("needed gropus")

        answer = [result[0][0], result[0][1], result[0][4] + result[0][5]]

        for i in range(len(answer)):
            answer[i] = answer[i].replace("\n", "")
            # print(answer[i])

        print("----------------------------------------------")
        answers.append(answer)



def save_to_file(answers: list, file_name: str):
    for i in answers:
        print(i)

    # with open(file_name+'.csv', 'w') as file:
    #     writer = csv.writer(file)
    #     for i in answers:
    #         writer.writerow(i)

    with open(file_name + '.txt', 'w') as file:
        for i in answers:
            for j in i:
                file.write(j+"\n")

            file.write("\n------------\n")


if __name__ == '__main__':


    while True:

        file_name=input("введите имя файла\n")

        answers = list()

        time.sleep(3)


        while True:  # making a loop

            if keyboard.is_pressed('e'):  # if key 'q' is pressed
                read_screen(answers)
                time.sleep(2)
            elif keyboard.is_pressed('q'):
                print("all saved")
                save_to_file(answers, file_name)
                break
            else:
                pass