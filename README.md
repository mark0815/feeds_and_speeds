# Feeds And Speeds - Backend

## Snippets

* Install Poetry packages in root python

    ```bash
    poetry export --dev -f requirements.txt --without-hashes | pip install -r /dev/stdin
    ```

* Dump / Load data

    ```bash
    ./manage.py dumpdata --format json materials > materials/fixtures/default.json
    ./manage.py dumpdata --format json milling > milling/fixtures/default.json
    ./manage.py loaddata --app materials --format json default.json
    ./manage.py loaddata --app milling --format json default.json
    ```

## Links

* https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation
