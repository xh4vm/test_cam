import os

DATABASES_AVAILABLE = {
    "PROD": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.environ.get("DB_BASE"),
    },
    "TEST": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.environ.get("TEST_DB_BASE"),
    },
}

DATABASES = {"default": DATABASES_AVAILABLE[os.environ.get("PROFILE", "PROD").upper()]}
