# <img src="https://www.svgrepo.com/show/303231/docker-logo.svg" width="89"/>

## Проект "Docker"

#### Проект реализовать запуск проекта [Django REST framework "Сервис Atomic Habits"](https://github.com/4byra6ka/AtomicHabitsService.git)
***
#### Реализованы задачи:
* Для разных сервисов созданы отдельные контейнеры (django, postgresql, redis, celery).
* Всё оформлено в файле docker-compose и Dockerfiles.
* Проект готов на размещение на удаленном сервере: 
  * можно запустить по инструкции, приложенной в Readme-файл;
  * для запуска не требуется дополнительных настроек.

***
### Прежде чем начать использовать проект нужно:
* Установить на ПК пакет docker и docker-compose
* Создать файл `.env` для переменного окружения.

### `.env`
    ALLOWED_HOSTS=*
    LANGUAGE_CODE=ru-ru
    TIME_ZONE=Europe/Moscow
    POSTGRES_DB=<DATABASES_NAME>
    POSTGRES_USER=<DATABASES_USER>
    POSTGRES_PASSWORD=<DATABASES_PASSWORD>
    DATABASES_HOST=db
    TG_API_KEY=<TG_API_KEY>
    CELERY=redis://redis:6379

***
### Запуск Docker проекта
    git cline https://github.com/4byra6ka/DockerStartup.git
    cd DockerStartup
    vi .env
    docker-compose build
    docker-compose up
***
#### P.S:
* будет добавлена учетная запись `admin 12345` что бы войти в админку
* если команды будут выполняться с ошибкой прошу использовать повышение прав `sudo`
