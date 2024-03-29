# Тестовая задача – «Посылка данных»

> Задача – реализовать прием синтетических данных.
**Требования к результату:**
- Имитация генератора посылок данных (локально);
- Регистрация пользователя в Django;
- Прием данных для залогиненного пользователя;
- Сохранение посылки данных в БД типа SQL (локально);
- Отображение посылки данных для заданного id посылки, при этом посылки можно отображать только те, которые пришли для залогированного пользователя.

> Сохранить для какого пользователя пришли посылки.
> Если нет входа пользователя, то не сохранять посылки.
---
Пример посылки данных:
```
{
    id: <1-999>; # int в заданном диапазоне
    cam_id: <1-99>; # int в заданном диапазоне
    VideoColor: {
        Brightness: <0-100>; # int в заданном диапазоне
        Contrast: <0-100>; # int в заданном диапазоне
        Hue: <0-100>; # int в заданном диапазоне
        Saturation: <0-100>; # int в заданном диапазоне
    };
    TimeSection: <00:00:00-24:00:00>; # время приема в формате dd-mm-yyyy:hh-mm-ss
    ChannelNo: <1-2>; # int в заданном диапазоне
    ConfigNo: <0-1>; # int в заданном диапазоне
}
```
---
## Запуск сервиса
```
cp .env.example .env
rm -rf ./nginx/static && cp -r ./nginx/static_defaults/ ./nginx/static
rm -rf ./db && mkdir db
make run
make makemigrations && make migrate
```

## Запуск источника данных
```
make data-gen # отправить запросы на создание пользователей, авторизацию и создание посылок данных
make data-gen-users # отправить запросы на создание пользователей
make data-gen-logins # отправить запросы на авторизацию
make data-gen-frames # отправить запросы на создание посылок данных
```

## Документация swagger
http://localhost/api/swagger

## Тестирование
`make tests`

## Black linter
`make black`
