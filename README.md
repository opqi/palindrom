REST сервис на FastAPI.

Пример входного json-а:

{
"word": "aabb"
}

Пример выходного запроса:

curl -X POST https://reqbin.com/echo/post/palindrome
-H 'Content-Type: application/json'
-d '{"word":"aabb"}

Метод должен определить, можно ли из символов в заданной строке построить
палиндром, и определить палиндром с минимальным количеством замен букв исходной
строки. Если таких палиндромов можно создать несколько, вывести необходимо
минимальный в лексикографическом смысле.

В случае, если палиндром построить нельзя, поле "palindrome" должно содержать пустую строку.

Пример выходного json-а:

{
"palindrome": "abba"
}

Пример ответа от сервиса:

HTTP/1.1 200 OK<br/>
Content-Type: application/json<br/>
Content-Length: 22

{"palindrome":"abba"}

Запустить

bash start.sh

Тест

python test.py
