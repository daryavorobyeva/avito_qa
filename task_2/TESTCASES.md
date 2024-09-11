## Тест-кейсы для проверки API микросервиса 

### 1. GET Получить объявление
<table>
    <thead>
        <tr>
            <th>№</th>
            <th>Заголовок</th>
            <th>Тестовые данные</th>
            <th>Шаги</th>
            <th>Ожидаемый результат</th>
            <th>Статус прохождения</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="3">1.1</td>
            <td rowspan="3">Успешное получение объявления по корректному id</td>
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
            <td rowspan="3">Попытка получения объекта по несуществующему Id</td>
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

<br>

### 2. GET Получить все объявления по продавцам
<table>
    <thead>
        <tr>
            <th>№</th>
            <th>Заголовок</th>
            <th>Тестовые данные</th>
            <th>Шаги</th>
            <th>Ожидаемый результат</th>
            <th>Статус прохождения</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="3">2.1</td>
            <td rowspan="3">Успешное получение всех объявлений продавца с валидным sellerId</td>
            <td rowspan="3">
                {<br>
                &nbsp;&nbsp;&nbsp;"sellerId": 3452<br>
                }
            </td>
            <td>Отправить GET запрос <br>https://qa-internship.avito.com/api/1/{sellerId}/item</td>
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
            <td rowspan="3">2.2</td>
            <td rowspan="3">Получение всех объявлений для продавца, у которого нет объявлений</td>
            <td rowspan="3">
                {<br>
                &nbsp;&nbsp;&nbsp;"sellerId": 2222<br>
                }
            </td>
            <td>Отправить GET запрос <br>https://qa-internship.avito.com/api/1/{sellerId}/item</td>
            <td>Запрос успешно отправлен на сервер</td>
            <td rowspan="3">Passed</td>
        </tr>
        <tr>
            <td>Проверить код ответа</td>
            <td>HTTP Status: 200 OK</td>
        </tr>
        <tr>
            <td>Проверить тело ответа</td>
            <td>Пустой массив</td>
        </tr>
    </tbody>
</table>

<br>

### 3. POST Сохранить объявление
<table>
    <thead>
        <tr>
            <th>№</th>
            <th>Заголовок</th>
            <th>Тестовые данные</th>
            <th>Шаги</th>
            <th>Ожидаемый результат</th>
            <th>Статус прохождения</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td rowspan="3">3.1</td>
            <td rowspan="3">Создание объявления с существующим sellerId</td>
            <td rowspan="3">
    {<br>
    &nbsp;&nbsp;&nbsp;"name": "Телефон",<br>
    &nbsp;&nbsp;&nbsp;"price": 85566,<br>
    &nbsp;&nbsp;&nbsp;"sellerId": 3452,<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": 32,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": 35,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": 14<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }
</td>
            <td>Отправить POST запрос <br>https://qa-internship.avito.com/api/1/item</td>
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
            <td rowspan="3">3.2</td>
            <td rowspan="3">Создание объявления с несуществующим положительным sellerId</td>
            <td rowspan="3">
    {<br>
    &nbsp;&nbsp;&nbsp;"name": "Телефон",<br>
    &nbsp;&nbsp;&nbsp;"price": 85566,<br>
    &nbsp;&nbsp;&nbsp;"sellerId": 234567,<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": 32,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": 35,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": 14<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }
</td>
            <td>Отправить POST запрос <br>https://qa-internship.avito.com/api/1/item</td>
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
            <td rowspan="3">3.3</td>
            <td rowspan="3">Создание объявления с несуществующим отрицательным sellerID</td>
            <td rowspan="3">
    {<br>
    &nbsp;&nbsp;&nbsp;"name": "",<br>
    &nbsp;&nbsp;&nbsp;"price": 85566,<br>
    &nbsp;&nbsp;&nbsp;"sellerId": -5,<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": 32,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": 35,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": 14<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }
</td>
            <td>Отправить POST запрос <br>https://qa-internship.avito.com/api/1/item</td>
            <td>Запрос успешно отправлен на сервер</td>
            <td rowspan="3">Failed</td>
        </tr>
        <tr>
            <td>Проверить код ответа</td>
            <td>HTTP Status: 400 Bad Request</td>
        </tr>
        <tr>
            <td>Проверить тело ответа</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="3">3.4</td>
            <td rowspan="3">Создание объявления с пустым полем name</td>
            <td rowspan="3">
    {<br>
    &nbsp;&nbsp;&nbsp;"name": "",<br>
    &nbsp;&nbsp;&nbsp;"price": 85566,<br>
    &nbsp;&nbsp;&nbsp;"sellerId": 3452,<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": 32,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": 35,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": 14<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }
</td>
            <td>Отправить POST запрос <br>https://qa-internship.avito.com/api/1/item</td>
            <td>Запрос успешно отправлен на сервер</td>
            <td rowspan="3">Failed</td>
        </tr>
        <tr>
            <td>Проверить код ответа</td>
            <td>HTTP Status: 400 Bad Request</td>
        </tr>
        <tr>
            <td>Проверить тело ответа</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="3">3.5</td>
            <td rowspan="3">Создание объявления с отрицательным полем price</td>
            <td rowspan="3">
    {<br>
    &nbsp;&nbsp;&nbsp;"name": "Телефон",<br>
    &nbsp;&nbsp;&nbsp;"price": -85566,<br>
    &nbsp;&nbsp;&nbsp;"sellerId": 3452,<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": 32,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": 35,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": 14<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }
</td>
            <td>Отправить POST запрос <br>https://qa-internship.avito.com/api/1/item</td>
            <td>Запрос успешно отправлен на сервер</td>
            <td rowspan="3">Failed</td>
        </tr>
        <tr>
            <td>Проверить код ответа</td>
            <td>HTTP Status: 400 Bad Request</td>
        </tr>
        <tr>
            <td>Проверить тело ответа</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="3">3.6</td>
            <td rowspan="3">Создание объявления с отрицательным полем contacts</td>
            <td rowspan="3">
    {<br>
    &nbsp;&nbsp;&nbsp;"name": "Телефон",<br>
    &nbsp;&nbsp;&nbsp;"price": 85566,<br>
    &nbsp;&nbsp;&nbsp;"sellerId": 3452,<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": -32,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": 35,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": 14<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }
</td>
            <td>Отправить POST запрос <br>https://qa-internship.avito.com/api/1/item</td>
            <td>Запрос успешно отправлен на сервер</td>
            <td rowspan="3">Failed</td>
        </tr>
        <tr>
            <td>Проверить код ответа</td>
            <td>HTTP Status: 400 Bad Request</td>
        </tr>
        <tr>
            <td>Проверить тело ответа</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="3">3.7</td>
            <td rowspan="3">Создание объявления с отрицательным полем like</td>
            <td rowspan="3">
    {<br>
    &nbsp;&nbsp;&nbsp;"name": "Телефон",<br>
    &nbsp;&nbsp;&nbsp;"price": 85566,<br>
    &nbsp;&nbsp;&nbsp;"sellerId": 3452,<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": 32,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": -35,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": 14<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }
</td>
            <td>Отправить POST запрос <br>https://qa-internship.avito.com/api/1/item</td>
            <td>Запрос успешно отправлен на сервер</td>
            <td rowspan="3">Failed</td>
        </tr>
        <tr>
            <td>Проверить код ответа</td>
            <td>HTTP Status: 400 Bad Request</td>
        </tr>
        <tr>
            <td>Проверить тело ответа</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="3">3.8</td>
            <td rowspan="3">Создание объявления с отрицательным полем viewCount</td>
            <td rowspan="3">
    {<br>
    &nbsp;&nbsp;&nbsp;"name": "Телефон",<br>
    &nbsp;&nbsp;&nbsp;"price": 85566,<br>
    &nbsp;&nbsp;&nbsp;"sellerId": 3452,<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": 32,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": 35,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": -14<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }
</td>
            <td>Отправить POST запрос <br>https://qa-internship.avito.com/api/1/item</td>
            <td>Запрос успешно отправлен на сервер</td>
            <td rowspan="3">Failed</td>
        </tr>
        <tr>
            <td>Проверить код ответа</td>
            <td>HTTP Status: 400 Bad Request</td>
        </tr>
        <tr>
            <td>Проверить тело ответа</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="3">3.9</td>
            <td rowspan="3">Создание объявления с некорректным типом данных в поле price</td>
            <td rowspan="3">
    {<br>
    &nbsp;&nbsp;&nbsp;"name": "Телефон",<br>
    &nbsp;&nbsp;&nbsp;"price": "abc",<br>
    &nbsp;&nbsp;&nbsp;"sellerId": 3452,<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": 32,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": 35,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": 14<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }
</td>
            <td>Отправить POST запрос <br>https://qa-internship.avito.com/api/1/item</td>
            <td>Запрос успешно отправлен на сервер</td>
            <td rowspan="3">Failed</td>
        </tr>
        <tr>
            <td>Проверить код ответа</td>
            <td>HTTP Status: 400 Bad Request</td>
        </tr>
        <tr>
            <td>Проверить тело ответа</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="3">3.10</td>
            <td rowspan="3">Создание объявления с некорректным типом данных в поле contacts</td>
            <td rowspan="3">
    {<br>
    &nbsp;&nbsp;&nbsp;"name": "Телефон",<br>
    &nbsp;&nbsp;&nbsp;"price": 85566,<br>
    &nbsp;&nbsp;&nbsp;"sellerId": 3452,<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": "abc",<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": 35,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": 14<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }
</td>
            <td>Отправить POST запрос <br>https://qa-internship.avito.com/api/1/item</td>
            <td>Запрос успешно отправлен на сервер</td>
            <td rowspan="3">Failed</td>
        </tr>
        <tr>
            <td>Проверить код ответа</td>
            <td>HTTP Status: 400 Bad Request</td>
        </tr>
        <tr>
            <td>Проверить тело ответа</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="3">3.11</td>
            <td rowspan="3">Создание объявления с некорректным типом данных в поле like</td>
            <td rowspan="3">
    {<br>
    &nbsp;&nbsp;&nbsp;"name": "Телефон",<br>
    &nbsp;&nbsp;&nbsp;"price": 85566,<br>
    &nbsp;&nbsp;&nbsp;"sellerId": 3452,<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": 32,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": "abc",<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": 14<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }
</td>
            <td>Отправить POST запрос <br>https://qa-internship.avito.com/api/1/item</td>
            <td>Запрос успешно отправлен на сервер</td>
            <td rowspan="3">Failed</td>
        </tr>
        <tr>
            <td>Проверить код ответа</td>
            <td>HTTP Status: 400 Bad Request</td>
        </tr>
        <tr>
            <td>Проверить тело ответа</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="3">3.12</td>
            <td rowspan="3">Создание объявления с некорректным типом данных в поле viewCount</td>
            <td rowspan="3">
    {<br>
    &nbsp;&nbsp;&nbsp;"name": "Телефон",<br>
    &nbsp;&nbsp;&nbsp;"price": 85566,<br>
    &nbsp;&nbsp;&nbsp;"sellerId": 3452,<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": 32,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": 35,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": "abc"<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }
</td>
            <td>Отправить POST запрос <br>https://qa-internship.avito.com/api/1/item</td>
            <td>Запрос успешно отправлен на сервер</td>
            <td rowspan="3">Failed</td>
        </tr>
        <tr>
            <td>Проверить код ответа</td>
            <td>HTTP Status: 400 Bad Request</td>
        </tr>
        <tr>
            <td>Проверить тело ответа</td>
            <td></td>
        </tr>
        <tr>
            <td rowspan="3">3.13</td>
            <td rowspan="3">Создание объявления с некорректным типом данных в поле sellerId</td>
            <td rowspan="3">
    {<br>
    &nbsp;&nbsp;&nbsp;"name": "Телефон",<br>
    &nbsp;&nbsp;&nbsp;"price": 85566,<br>
    &nbsp;&nbsp;&nbsp;"sellerId": "abc",<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": 32,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": 35,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": 14<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }
</td>
            <td>Отправить POST запрос <br>https://qa-internship.avito.com/api/1/item</td>
            <td>Запрос успешно отправлен на сервер</td>
            <td rowspan="3">Failed</td>
        </tr>
        <tr>
            <td>Проверить код ответа</td>
            <td>HTTP Status: 400 Bad Request</td>
        </tr>
        <tr>
            <td>Проверить тело ответа</td>
            <td></td>
        </tr>
    </tbody>
</table>
