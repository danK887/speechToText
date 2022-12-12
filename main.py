import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source: # берет микрофон по умолчанию
    print("Скажите что-нибудь: ")
    audio = r.listen(source)

try:
     print(r.recognize_google(audio, language="ru-RU"))

     """
     Запись в файл. Добавляем новую информацию в файл, а не перезаписываем. 
     Добавление происходит благодаря "а"
     Файл сохраняется в директории проекта.
     """
     try:
         with open("demofile.txt", "a", encoding="utf-8") as file:
            file.write(r.recognize_google(audio, language="ru-RU") + '\n')
     except:
         print("Ошибка при работе с файлом")

except sr.UnknownValueError:
    print("Робот не расслышал фразу")
except sr.RequestError as e:
    print("Ошибка сервиса; {0}".format(e))

