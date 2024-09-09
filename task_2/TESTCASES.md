## Тест-кейсы для проверки API микросервиса 

### 1. GET Получить объявление
<table>
    <thead>
        <tr>
            <th>№</th>
            <th>Заголовок</th>
            <th>Предусловия</th>
            <th>Тестовые данные</th>
            <th>Шаги</th>
            <th>Ожидаемый результат</th>
            <th>Статус прохождения</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="3">1.1</td>
            <td rowspan="3">Успешное получение объявления по корректному ID</td>
            <td rowspan="3">В системе должно существовать объявление с ID, которое будет использовано в тесте</td>
            <td rowspan="3">
                {<br>
                &nbsp;&nbsp;&nbsp;"id": "07d2b4fc-4e4c-4427-bbb0-74a67fa5ce38"<br>
                }
            </td>
            <td>Отправить GET запрос <br>https://qa-internship.avito.com/api/1/item/{id}</td>
            <td>Запрос успешно отправлен на сервер</td>
            <td rowspan="3">Passed</td>
        </tr>
        <tr>
            <td>Проверить код ответа</td>
            <td>HTTP Status: 200 OK</td>
        </tr>
        <tr>
            <td>Проверить тело ответа</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="3">1.2</td>
            <td rowspan="3">Попытка получения объекта по несуществующему ID</td>
            <td rowspan="3">ID, который используется в тесте, не должен существовать в системе</td>
            <td rowspan="3">
                {<br>
                &nbsp;&nbsp;&nbsp;"id": "07d2b4fc-4e4c-4427-bbb0-74a67fa5ce13"<br>
                }
            </td>
            <td>Отправить GET запрос <br>https://qa-internship.avito.com/api/1/item/{id}</td>
            <td>Запрос успешно отправлен на сервер</td>
            <td rowspan="3">Passed</td>
        </tr>
        <tr>
            <td>Проверить код ответа</td>
            <td>HTTP Status: 404 Not Found</td>
        </tr>
        <tr>
            <td>Проверить тело ответа</td>
            <td></td>
        </tr>
    </tbody>
</table>
