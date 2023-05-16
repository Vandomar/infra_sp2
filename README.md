# Проект YaMDb
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Title). Произведения делятся на категории: "Книги", "Фильмы", "Музыка". Список к
# Ресурсы API YaMDb
**AUTH**: аутентификация.

**USERS**: пользователи.

**TITLES**: произведения, к которым пишут отзывы (определённый фильм, книга или песенка).

**CATEGORIES**: категории (типы) произведений ("Фильмы", "Книги", "Музыка").

**GENRES**: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.

**REVIEWS**: отзывы на произведения. Отзыв привязан к определённому произведению.

**COMMENTS**: комментарии к отзывам. Комментарий привязан к определённому отзыву.


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:vandomar/infra_sp2.git
cd infra_sp2
cd infra
```
Создайте в клонированной директории файл .env. Ниже приведен пример его наполнения:
```
SECRET_KEY = 'some_secret_key'
DB_ENGINE=django.db.backends.postgresql #указываем что работаем с postgresql
DB_NAME=postgres #указываем имя базы данных
POSTGRES_USER=set_your_username #логин для подключения к БД
POSTGRES_PASSWORD=set_your_pwd #пароль для подключения к БД
DB_HOST=db #название контейнера
DB_PORT=5432 #порт для подключения к БД
```

Запустите docker-compose.
```
docker-compose up -d --build
```
В контейнере web выполнить миграции:
```
docker-compose exec web python manage.py makemigrations reviews
docker-compose exec web python manage.py makemigrations users
docker-compose exec web python manage.py migrate
```

Создать суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```

Собрать статику
```
docker-compose exec web python manage.py collectstatic --no-input
```
Заполните базу данными:
```
docker-compose exec web python manage.py loaddata fixtures.json
```

Проверьте работоспособность приложения, для этого перейдите на страницу:
```
 http://localhost/admin/
```