# Markov-Text-Generator

Программа для создания случайного текста на основе корпуса текстов с использованием марковских цепей.

Решение состоит в выборе следующего слова по двум предыдущим, исходя из частоты встречаемости слов
в некотором корпусе текстов. Частота пропорциональна тому, сколько раз данная тройка слов
(два предыдущих и одно последующее) была встречена в большом наборе текстов (корпусе).  

Процесс подсчета частот встречаемости можно назвать обучением алгоритма.
Написанная программа умеет обучаться на текстах (метод **train_from_text()**), текстовых файлах
(метод **train_from_file()**) и рекурсивно на директориях текстовых файлов (метод **train_from_corpus()**).
В один обученый объект генератора текстов можно добавлять данные из другого объекта ( **+=**)

Точка считается отдельным словом, так же как и запятая. Почти вся остальная пунктуация удалена 
(! и ? осталены, но как части слов, закоторыми они идут). Первое слово предложения герерируется на основе последнего
слова предыдущего предложения либо на основе случайно выбранного слова (для этого слова проверяется что можно сгенерировать следующие,
но дальше не проверяется есть ли варианты и может возникнуть ошибка).

Пример сгенерированного текстав представлен в файле **example.txt**.
Вариант кода для тестирования представлен в файле **main.py** 
(нужно раскоментировать соответствующие строки в функции **main()**).

