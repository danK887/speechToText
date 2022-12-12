# speechToText

>***Файл mail - программа для перевода голоса в текст. Запускаете код, диктуете предложение и программа сразу его переводит и записывает в файл***

Для работы потребуется 2 библиотеки: SpeechRecognition и PyAudio.

***<h3>pip install SpeechRecognition</h3>***

***<h3>pip install PyAudio</h3>***

PyAudio служит для работы с микрофоном.
SpeechRecognition преобразует речь в текст по средосвам интегарции с Google Speech Recognition.
Так же для работы важно подключение к интернету.

После запуска кода нужно сказать фразу Громко и Четко для лучшего распознования.
Вывод фразы организован в консоль и записывается в файл "demofile.txt". Файл создается в той же директирии, что и проект.
Так же файл сохраняет все фразы и предложения. 


==============================================================================

>***Файл voice_from_file - программа для перевода голоса(ИЗ ФАЙЛА) в текст.***

Для работы потребуется библиотека vosk
***<h3>VOSK - pip install vosk</h3>***

Так же необходима модель, которую нужно скачать https://alphacephei.com/vosk/models (надо выбрать ru)и разархивировать в папку с проектом
**Для работы программы нужен файл с расширением .WAV и записанный в МОНО канале.**
Можно использовать прикрепленный файл test_voice для тестов.
