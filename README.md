# Feeds And Speeds - Backend

## Snippets

* Install Poetry packages in root python

    ```bash
    poetry export -f requirements.txt --without-hashes | pip install -r /dev/stdin
    ```

* Dump / Load data

    ```bash
    ./manage.py dumpdata --format json api > api/fixtures/default.json
    ./manage.py loaddata --app api --format json default.json
    ```

## Links

* https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation
