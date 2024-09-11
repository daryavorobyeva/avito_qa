### Bug 1

<table>
  <tbody>
    <tr>
      <td>Заголовок</td>
      <td>Успешное создание объявления с отрицательным значением sellerId</td>
    </tr>
    <tr>
      <td>Описание</td>
      <td>Возникает при выполнении тест-кейса 3.3</td>
    </tr>
    <tr>
      <td>Шаги воспроизведения</td>
      <td>Отправить сервису POST запрос https://qa-internship.avito.com/api/1/item <br>
Тело запроса: <br>
 {<br>
    &nbsp;&nbsp;&nbsp;"name": "",<br>
    &nbsp;&nbsp;&nbsp;"price": 85566,<br>
    &nbsp;&nbsp;&nbsp;"sellerId": -5,<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": 32,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": 35,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": 14<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }</td>
    </tr>
    <tr>
      <td>Фактический результат</td>
      <td>HTTP Status: 200 OK</td>
    </tr>
    <tr>
      <td>Ожидаемый результат</td>
      <td>HTTP Status: 400 Bad Request</td>
    </tr>
    <tr>
      <td>Приоритет</td>
      <td>medium</td>
    </tr>
    <tr>
      <td>Окружение</td>
      <td>Ноутбук Huawei MateBook D 14, Windows 11 <br> Python 3.12.0, Pytest 8.3.2, PyCharm</td>
    </tr>
  </tbody>
</table>

<br>

### Bug 2

<table>
  <tbody>
    <tr>
      <td>Заголовок</td>
      <td>Успешное создание объявления с пустым полем name</td>
    </tr>
    <tr>
      <td>Описание</td>
      <td>Возникает при выполнении тест-кейса 3.4</td>
    </tr>
    <tr>
      <td>Шаги воспроизведения</td>
      <td>Отправить сервису POST запрос https://qa-internship.avito.com/api/1/item <br>
Тело запроса: <br>
 {<br>
    &nbsp;&nbsp;&nbsp;"name": "",<br>
    &nbsp;&nbsp;&nbsp;"price": 85566,<br>
    &nbsp;&nbsp;&nbsp;"sellerId": 3452,<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": 32,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": 35,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": 14<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }</td>
    </tr>
    <tr>
      <td>Фактический результат</td>
      <td>HTTP Status: 200 OK</td>
    </tr>
    <tr>
      <td>Ожидаемый результат</td>
      <td>HTTP Status: 400 Bad Request</td>
    </tr>
    <tr>
      <td>Приоритет</td>
      <td>high</td>
    </tr>
    <tr>
      <td>Окружение</td>
      <td>Ноутбук Huawei MateBook D 14, Windows 11 <br> Python 3.12.0, Pytest 8.3.2, PyCharm</td>
    </tr>
  </tbody>
</table>

<br>

### Bug 3

<table>
  <tbody>
    <tr>
      <td>Заголовок</td>
      <td>Успешное создание объявления с отрицательным полем price</td>
    </tr>
    <tr>
      <td>Описание</td>
      <td>Возникает при выполнении тест-кейса 3.5</td>
    </tr>
    <tr>
      <td>Шаги воспроизведения</td>
      <td>Отправить сервису POST запрос https://qa-internship.avito.com/api/1/item <br>
Тело запроса: <br>
  {<br>
    &nbsp;&nbsp;&nbsp;"name": "Телефон",<br>
    &nbsp;&nbsp;&nbsp;"price": -85566,<br>
    &nbsp;&nbsp;&nbsp;"sellerId": 3452,<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": 32,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": 35,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": 14<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }</td>
    </tr>
    <tr>
      <td>Фактический результат</td>
      <td>HTTP Status: 200 OK</td>
    </tr>
    <tr>
      <td>Ожидаемый результат</td>
      <td>HTTP Status: 400 Bad Request</td>
    </tr>
    <tr>
      <td>Приоритет</td>
      <td>high</td>
    </tr>
    <tr>
      <td>Окружение</td>
      <td>Ноутбук Huawei MateBook D 14, Windows 11 <br> Python 3.12.0, Pytest 8.3.2, PyCharm</td>
    </tr>
  </tbody>
</table>

<br>

### Bug 4

<table>
  <tbody>
    <tr>
      <td>Заголовок</td>
      <td>Успешное создание объявления с отрицательным полем contacts</td>
    </tr>
    <tr>
      <td>Описание</td>
      <td>Возникает при выполнении тест-кейса 3.6</td>
    </tr>
    <tr>
      <td>Шаги воспроизведения</td>
      <td>Отправить сервису POST запрос https://qa-internship.avito.com/api/1/item <br>
Тело запроса: <br>
  {<br>
    &nbsp;&nbsp;&nbsp;"name": "Телефон",<br>
    &nbsp;&nbsp;&nbsp;"price": 85566,<br>
    &nbsp;&nbsp;&nbsp;"sellerId": 3452,<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": -32,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": 35,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": 14<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }</td>
    </tr>
    <tr>
      <td>Фактический результат</td>
      <td>HTTP Status: 200 OK</td>
    </tr>
    <tr>
      <td>Ожидаемый результат</td>
      <td>HTTP Status: 400 Bad Request</td>
    </tr>
    <tr>
      <td>Приоритет</td>
      <td>high</td>
    </tr>
    <tr>
      <td>Окружение</td>
      <td>Ноутбук Huawei MateBook D 14, Windows 11 <br> Python 3.12.0, Pytest 8.3.2, PyCharm</td>
    </tr>
  </tbody>
</table>

<br>

### Bug 5

<table>
  <tbody>
    <tr>
      <td>Заголовок</td>
      <td>Успешное создание объявления с отрицательным полем like</td>
    </tr>
    <tr>
      <td>Описание</td>
      <td>Возникает при выполнении тест-кейса 3.7</td>
    </tr>
    <tr>
      <td>Шаги воспроизведения</td>
      <td>Отправить сервису POST запрос https://qa-internship.avito.com/api/1/item <br>
Тело запроса: <br>
  {<br>
    &nbsp;&nbsp;&nbsp;"name": "Телефон",<br>
    &nbsp;&nbsp;&nbsp;"price": 85566,<br>
    &nbsp;&nbsp;&nbsp;"sellerId": 3452,<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": 32,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": -35,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": 14<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }</td>
    </tr>
    <tr>
      <td>Фактический результат</td>
      <td>HTTP Status: 200 OK</td>
    </tr>
    <tr>
      <td>Ожидаемый результат</td>
      <td>HTTP Status: 400 Bad Request</td>
    </tr>
    <tr>
      <td>Приоритет</td>
      <td>high</td>
    </tr>
    <tr>
      <td>Окружение</td>
      <td>Ноутбук Huawei MateBook D 14, Windows 11 <br> Python 3.12.0, Pytest 8.3.2, PyCharm</td>
    </tr>
  </tbody>
</table>

<br>

### Bug 6

<table>
  <tbody>
    <tr>
      <td>Заголовок</td>
      <td>Успешное создание объявления с отрицательным полем viewCount</td>
    </tr>
    <tr>
      <td>Описание</td>
      <td>Возникает при выполнении тест-кейса 3.8</td>
    </tr>
    <tr>
      <td>Шаги воспроизведения</td>
      <td>Отправить сервису POST запрос https://qa-internship.avito.com/api/1/item <br>
Тело запроса: <br>
  {<br>
    &nbsp;&nbsp;&nbsp;"name": "Телефон",<br>
    &nbsp;&nbsp;&nbsp;"price": 85566,<br>
    &nbsp;&nbsp;&nbsp;"sellerId": 3452,<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": 32,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": 35,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": -14<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }</td>
    </tr>
    <tr>
      <td>Фактический результат</td>
      <td>HTTP Status: 200 OK</td>
    </tr>
    <tr>
      <td>Ожидаемый результат</td>
      <td>HTTP Status: 400 Bad Request</td>
    </tr>
    <tr>
      <td>Приоритет</td>
      <td>high</td>
    </tr>
    <tr>
      <td>Окружение</td>
      <td>Ноутбук Huawei MateBook D 14, Windows 11 <br> Python 3.12.0, Pytest 8.3.2, PyCharm</td>
    </tr>
  </tbody>
</table>

<br>

### Bug 7

<table>
  <tbody>
    <tr>
      <td>Заголовок</td>
      <td>Неправильное создание объявления с некорректным типом данных в поле price</td>
    </tr>
    <tr>
      <td>Описание</td>
      <td>Возникает при выполнении тест-кейса 3.9</td>
    </tr>
    <tr>
      <td>Шаги воспроизведения</td>
      <td>Отправить сервису POST запрос https://qa-internship.avito.com/api/1/item <br>
Тело запроса: <br>
  {<br>
    &nbsp;&nbsp;&nbsp;"name": "Телефон",<br>
    &nbsp;&nbsp;&nbsp;"price": "abc",<br>
    &nbsp;&nbsp;&nbsp;"sellerId": 3452,<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": 32,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": 35,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": 14<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }</td>
    </tr>
    <tr>
      <td>Фактический результат</td>
      <td>HTTP Status: 500 Internal Server Error</td>
    </tr>
    <tr>
      <td>Ожидаемый результат</td>
      <td>HTTP Status: 400 Bad Request</td>
    </tr>
    <tr>
      <td>Приоритет</td>
      <td>high</td>
    </tr>
    <tr>
      <td>Окружение</td>
      <td>Ноутбук Huawei MateBook D 14, Windows 11 <br> Python 3.12.0, Pytest 8.3.2, PyCharm</td>
    </tr>
  </tbody>
</table>

<br>

### Bug 8

<table>
  <tbody>
    <tr>
      <td>Заголовок</td>
      <td>Неправильное создание объявления с некорректным типом данных в поле contacts</td>
    </tr>
    <tr>
      <td>Описание</td>
      <td>Возникает при выполнении тест-кейса 3.10</td>
    </tr>
    <tr>
      <td>Шаги воспроизведения</td>
      <td>Отправить сервису POST запрос https://qa-internship.avito.com/api/1/item <br>
Тело запроса: <br>
  {<br>
    &nbsp;&nbsp;&nbsp;"name": "Телефон",<br>
    &nbsp;&nbsp;&nbsp;"price": 85566,<br>
    &nbsp;&nbsp;&nbsp;"sellerId": 3452,<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": "abc",<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": 35,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": 14<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }</td>
    </tr>
    <tr>
      <td>Фактический результат</td>
      <td>HTTP Status: 500 Internal Server Error</td>
    </tr>
    <tr>
      <td>Ожидаемый результат</td>
      <td>HTTP Status: 400 Bad Request</td>
    </tr>
    <tr>
      <td>Приоритет</td>
      <td>medium</td>
    </tr>
    <tr>
      <td>Окружение</td>
      <td>Ноутбук Huawei MateBook D 14, Windows 11 <br> Python 3.12.0, Pytest 8.3.2, PyCharm</td>
    </tr>
  </tbody>
</table>

<br>

### Bug 9

<table>
  <tbody>
    <tr>
      <td>Заголовок</td>
      <td>Успешное создание объявления с некорректным типом данных в поле like</td>
    </tr>
    <tr>
      <td>Описание</td>
      <td>Возникает при выполнении тест-кейса 3.11</td>
    </tr>
    <tr>
      <td>Шаги воспроизведения</td>
      <td>Отправить сервису POST запрос https://qa-internship.avito.com/api/1/item <br>
Тело запроса: <br>
  {<br>
    &nbsp;&nbsp;&nbsp;"name": "Телефон",<br>
    &nbsp;&nbsp;&nbsp;"price": 85566,<br>
    &nbsp;&nbsp;&nbsp;"sellerId": 3452,<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": 32,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": "abc",<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": 14<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }</td>
    </tr>
    <tr>
      <td>Фактический результат</td>
      <td>HTTP Status: 200 OK</td>
    </tr>
    <tr>
      <td>Ожидаемый результат</td>
      <td>HTTP Status: 400 Bad Request</td>
    </tr>
    <tr>
      <td>Приоритет</td>
      <td>high</td>
    </tr>
    <tr>
      <td>Окружение</td>
      <td>Ноутбук Huawei MateBook D 14, Windows 11 <br> Python 3.12.0, Pytest 8.3.2, PyCharm</td>
    </tr>
  </tbody>
</table>

<br>

### Bug 10

<table>
  <tbody>
    <tr>
      <td>Заголовок</td>
      <td>Неправильное создание объявления с некорректным типом данных в поле viewCount</td>
    </tr>
    <tr>
      <td>Описание</td>
      <td>Возникает при выполнении тест-кейса 3.12</td>
    </tr>
    <tr>
      <td>Шаги воспроизведения</td>
      <td>Отправить сервису POST запрос https://qa-internship.avito.com/api/1/item <br>
Тело запроса: <br>
  {<br>
    &nbsp;&nbsp;&nbsp;"name": "Телефон",<br>
    &nbsp;&nbsp;&nbsp;"price": 85566,<br>
    &nbsp;&nbsp;&nbsp;"sellerId": 3452,<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": 32,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": 35,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": "abc"<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }</td>
    </tr>
    <tr>
      <td>Фактический результат</td>
      <td>HTTP Status: 500 Internal Server Error</td>
    </tr>
    <tr>
      <td>Ожидаемый результат</td>
      <td>HTTP Status: 400 Bad Request</td>
    </tr>
    <tr>
      <td>Приоритет</td>
      <td>high</td>
    </tr>
    <tr>
      <td>Окружение</td>
      <td>Ноутбук Huawei MateBook D 14, Windows 11 <br> Python 3.12.0, Pytest 8.3.2, PyCharm</td>
    </tr>
  </tbody>
</table>

<br>

### Bug 11

<table>
  <tbody>
    <tr>
      <td>Заголовок</td>
      <td>Неправильное создание объявления с некорректным типом данных в поле sellerId</td>
    </tr>
    <tr>
      <td>Описание</td>
      <td>Возникает при выполнении тест-кейса 3.13</td>
    </tr>
    <tr>
      <td>Шаги воспроизведения</td>
      <td>Отправить сервису POST запрос https://qa-internship.avito.com/api/1/item <br>
Тело запроса: <br>
  {<br>
    &nbsp;&nbsp;&nbsp;"name": "Телефон",<br>
    &nbsp;&nbsp;&nbsp;"price": 85566,<br>
    &nbsp;&nbsp;&nbsp;"sellerId": "abc",<br>
    &nbsp;&nbsp;&nbsp;"statistics": {<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"contacts": 32,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"like": 35,<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"viewCount": 14<br>
    &nbsp;&nbsp;&nbsp;}<br>
    }</td>
    </tr>
    <tr>
      <td>Фактический результат</td>
      <td>HTTP Status: 500 Internal Server Error</td>
    </tr>
    <tr>
      <td>Ожидаемый результат</td>
      <td>HTTP Status: 400 Bad Request</td>
    </tr>
    <tr>
      <td>Приоритет</td>
      <td>high</td>
    </tr>
    <tr>
      <td>Окружение</td>
      <td>Ноутбук Huawei MateBook D 14, Windows 11 <br> Python 3.12.0, Pytest 8.3.2, PyCharm</td>
    </tr>
  </tbody>
</table>

<br>
