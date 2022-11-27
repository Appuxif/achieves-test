import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "postgresdb"),
        "USER": os.environ.get("POSTGRES_USER", "postgresuser"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "postgrespassword"),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    },
}
