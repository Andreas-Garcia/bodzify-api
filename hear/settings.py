# Standard library imports
import datetime
import os
import sys
import tomllib
from pathlib import Path
from typing import Any

import dj_database_url
from corsheaders.defaults import default_headers
from the_music_tree_api_kit.utils.allowed_hosts import add_loopback_hosts

# Third-party imports
from hear.CiStartupTraceEnabled import CiStartupTraceEnabled
from hear.utils.AppStaticFileStates import StaticFileStates
from hear.utils.env_var_loader import (
    load_env_vars_from_file_if_exists,
    load_optional_secret_env_var,
    load_optional_str_env_var,
    load_required_bool_env_var,
    load_required_path_env_var,
    load_required_secret_env_var,
    load_required_str_env_var,
)
from hear.utils.utils import is_django_startup_verbose, mask_oauth_client_id, print_django

TEST_USER_LIBRARIES_DIR_NAME_PREFIXE: str
USER_MAX_NUMBER: str
UUID_LEN: int
LANGUAGE_LEN_MAX: int
FILE_PATH_MAX_LENGTH: int
UPLOADED_TRACK_FILE_SIZE_MIN_IN_MO: int
UPLOADED_TRACK_FILE_SIZE_MAX_IN_MO: int
UPLOADED_TRACK_FILE_EXTENSIONS: list[str] = []
UPLOADED_TRACK_FILE_CONTENT_TYPES: list[str] = []
UPLOADED_TRACK_FILENAME_LEN_MAX: int
UPLOADED_TRACK_FILENAME_GENERATED_WITHOUT_EXTENSION_LENGTH: int
UPLOADED_TRACK_TITLE_LEN_MAX: int
UPLOADED_TRACK_TITLE_LEN_MAX_ID3V1: int
UPLOADED_TRACK_TRACK_NUMBER_MAX: int
UPLOADED_TRACK_FILENAME_EXPRESSIONS_TO_EXCLUDE_GENERATING_TITLE: list[str] = []
UPLOADED_TRACK_GENERATED_TITLE_LENGTH: int
UPLOADED_TRACK_GENERATED_TITLE_PREFIXE: str
UPLOADED_TRACK_RATING_VALUE_MAX: int
MINE_TRACK_TITLE_LEN_MAX: int
MINE_TRACK_RELEASED_ON_LEN_MAX: int
MINE_TRACK_URL_LEN_MAX: int
ALBUM_NAME_LEN_MAX: int
ALBUM_NAME_LEN_MAX_ID3V1: int
ALBUM_ARTISTS_NAMES_FIELD_LEN_MAX: int
ARTIST_NAME_LEN_MAX: int
ARTIST_NAME_LEN_MAX_ID3V1: int
ARTISTS_NAMES_LEN_MAX: int
CRITERIA_TYPE_LABEL_LEN_MAX: int
CRITERIA_NAME_LEN_MAX: int
MANUAL_PLAYLIST_NAME_LEN_MAX: int
FINGERPRINTING_ERROR_MESSAGE_LEN_MAX: int
FINGERPRINTING_ERROR_CODE_LABEL_LEN_MAX: int
MB_BASE_URL: str
MB_ID_LEN_MAX: int
MB_RECORDING_URL: str
MB_RECORDING_TITLE_LEN_MAX: int
MB_RECORDING_MISSING_CAUSE_CODE_LABEL_LEN_MAX: int
MB_RECORDING_MISSING_CAUSE_MESSAGE_LEN_MAX: int
MB_ARTIST_URL: str
MB_ARTIST_NAME_LEN_MAX: int
PAGINATION_PAGE_SIZE_DEFAULT: int
PAGINATION_PAGE_SIZE_MULTIMODEL_DEFAULT: int
PAGINATION_PAGE_SIZE_MAX: int  # Security measure to avoid a DoS attack if a user requests a huge page size
CRITERIA_TREE_IMPORT_MAX_ROOT_COUNT: int
CRITERIA_TREE_IMPORT_MAX_TOTAL_COUNT: int
CRITERIA_TREE_IMPORT_STALE_DELETE_MAX_FRACTION: float

# AFP Connection
AFP_BASE_URL: str
AFP_POST_ENDPOINT: str

# Static Files
STATIC_ROOT: Path
STATIC_URL: str

INSTALLED_APPS: list[str] = []
CACHES: dict[str, Any] = {}
MIDDLEWARE: list[str] = []
TEMPLATES: list[dict[str, Any]] = []

# Django Constants
WSGI_APPLICATION: str
AUTH_USER_MODEL: str
CRITERIA_MODEL: str
TRACK_MODEL: str
ARTIST_MODEL: str
ALBUM_MODEL: str
TRACK_TITLE_LEN_MAX: int
TRACK_TRACK_NUMBER_MAX: int
TRACK_RATING_VALUE_MAX: int
AUTH_PASSWORD_VALIDATORS: list[dict[str, Any]] = []
LANGUAGE_CODE: str
TIME_ZONE: str
USE_I18N: bool
USE_TZ: bool
DEFAULT_AUTO_FIELD: str
REST_FRAMEWORK: dict[str, Any] = {}
SPECTACULAR_SETTINGS: dict[str, Any] = {}
SIMPLE_JWT: dict[str, Any] = {}

# Media
ACOUSTID_API_KEY: str
AFP_ENABLED: bool
MUSICBRAINZ_LOOKUP_ENABLED: bool
MEDIA_ROOT: Path
MEDIA_URL: str
LIBRARIES_DIR: Path

# Spotify
SPOTIFY_ENABLED: bool
SPOTIFY_CLIENT_ID: str
SPOTIFY_CLIENT_SECRET: str
SPOTIFY_REDIRECT_URI: str
SPOTIFY_SCOPES: str

# Google OAuth
GOOGLE_OAUTH_ENABLED: bool
GOOGLE_CLIENT_ID: str
GOOGLE_CLIENT_SECRET: str
GOOGLE_REDIRECT_URI: str

# Secret Key
SECRET_KEY: str

# File Upload
FILE_UPLOAD_TEMP_DIR: str | None
FILE_UPLOAD_ENABLED: bool
METADATA_SESSION_DIR: Path | None


def init_logs_if_needed():
    from hear.logging.LoggersName import LoggersName

    LOG_DIR_STR = os.getenv("DJANGO_LOG_DIR")
    if not LOG_DIR_STR:
        print_django("The DJANGO_LOG_DIR variable is not set. Logs will not be set up.")
    else:
        print_django("LOG_DIR is set. Setting up logs...")

        LOG_DIR = Path(LOG_DIR_STR)
        if not LOG_DIR.exists():
            raise OSError(f"The log directory {LOG_DIR} does not exist.")
        print_django(f"The log dir {LOG_DIR} exists.")

        LOG_GENERAL_FILENAME = load_required_str_env_var("DJANGO_LOG_GENERAL_FILENAME")
        LOG_GENERAL_FILE = LOG_DIR / LOG_GENERAL_FILENAME
        if not LOG_GENERAL_FILE.exists():
            raise OSError(f"The log general file {LOG_GENERAL_FILE} does not exist.")
        print_django("The log general file {LOG_GENERAL_FILE} exists.")

        LOG_INFO_FILENAME = load_required_str_env_var("DJANGO_LOG_INFO_FILENAME")
        LOG_INFO_FILE = LOG_DIR / LOG_INFO_FILENAME
        if not LOG_INFO_FILE.exists():
            raise OSError(f"The log info file {LOG_INFO_FILE} does not exist.")
        print_django(f"The log info file {LOG_INFO_FILE} exists.")

        LOG_REQUESTS_FILENAME = load_required_str_env_var("DJANGO_LOG_REQUESTS_FILENAME")
        LOG_REQUESTS_FILE = LOG_DIR / LOG_REQUESTS_FILENAME
        if not LOG_REQUESTS_FILE.exists():
            raise OSError(f"The log requests file {LOG_REQUESTS_FILE} does not exist.")
        print_django(f"The log info file {LOG_REQUESTS_FILE} exists.")

        LOG_REQUESTS_DEBUG_FILENAME = load_required_str_env_var("DJANGO_LOG_REQUESTS_DEBUG_FILENAME")
        LOG_REQUESTS_DEBUG_FILE = LOG_DIR / LOG_REQUESTS_DEBUG_FILENAME
        if not LOG_REQUESTS_DEBUG_FILE.exists():
            raise OSError(f"The log requests debug file {LOG_REQUESTS_DEBUG_FILE} does not exist.")
        print_django(f"The log info file {LOG_REQUESTS_DEBUG_FILE} exists.")

        LOG_EXCEPTIONS_FILENAME = load_required_str_env_var("DJANGO_LOG_EXCEPTIONS_FILENAME")
        LOG_EXCEPTIONS_FILE = LOG_DIR / LOG_EXCEPTIONS_FILENAME
        if not LOG_EXCEPTIONS_FILE.exists():
            raise OSError(f"The log exceptions file {LOG_EXCEPTIONS_FILE} does not exist.")
        print_django(f"The log info file {LOG_EXCEPTIONS_FILE} exists.")

        LOG_DJANGO_FILENAME = load_required_str_env_var("DJANGO_LOG_DJANGO_FILENAME")
        LOG_DJANGO_FILE = LOG_DIR / LOG_DJANGO_FILENAME
        if not LOG_DJANGO_FILE.exists():
            raise OSError(f"The log django file {LOG_DJANGO_FILE} does not exist.")
        print_django(f"The log info file {LOG_DJANGO_FILE} exists.")

        LOG_APP_FILENAME = load_required_str_env_var("DJANGO_LOG_APP_FILENAME")
        LOG_APP_FILE = LOG_DIR / LOG_APP_FILENAME
        if not LOG_APP_FILE.exists():
            raise OSError(f"The log app file {LOG_APP_FILE} does not exist.")
        print_django(f"The log info file {LOG_APP_FILE} exists.")

        class LOGGERS_NAME:
            INFO = "info"
            REQUEST = "request"
            REQUEST_DJANGO = "django.request"
            EXCEPTIONS = "exceptions"
            DJANGO = "django"
            APP = APP_NAME

        global LOGGING
        LOGGING = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {"standard": {"format": "%(asctime)s [%(levelname)s]- %(message)s"}},
            "handlers": {
                "general": {
                    "level": "DEBUG",
                    "class": "logging.handlers.RotatingFileHandler",
                    "filename": LOG_GENERAL_FILE,
                    "maxBytes": 1024 * 1024 * 15,  # 15MB
                    "backupCount": 10,
                    "formatter": "standard",
                },
                "info": {
                    "level": "DEBUG",
                    "class": "logging.handlers.RotatingFileHandler",
                    "filename": LOG_INFO_FILE,
                    "maxBytes": 1024 * 1024 * 15,  # 15MB
                    "backupCount": 10,
                    "formatter": "standard",
                },
                "requests": {
                    "level": "INFO",
                    "class": "logging.handlers.RotatingFileHandler",
                    "filename": LOG_REQUESTS_FILE,
                    "maxBytes": 1024 * 1024 * 15,  # 15MB
                    "backupCount": 10,
                    "formatter": "standard",
                },
                "requests_with_trace": {
                    "level": "DEBUG",
                    "class": "logging.handlers.RotatingFileHandler",
                    "filename": LOG_REQUESTS_DEBUG_FILE,
                    "maxBytes": 1024 * 1024 * 15,  # 15MB
                    "backupCount": 10,
                    "formatter": "standard",
                },
                "exceptions": {
                    "level": "DEBUG",
                    "class": "logging.handlers.RotatingFileHandler",
                    "filename": LOG_EXCEPTIONS_FILE,
                    "maxBytes": 1024 * 1024 * 15,  # 15MB
                    "backupCount": 10,
                    "formatter": "standard",
                },
                "django": {
                    "level": "DEBUG",
                    "class": "logging.handlers.RotatingFileHandler",
                    "filename": LOG_DJANGO_FILE,
                    "maxBytes": 1024 * 1024 * 15,  # 15MB
                    "backupCount": 10,
                    "formatter": "standard",
                },
                APP_NAME: {
                    "level": "DEBUG",
                    "class": "logging.handlers.RotatingFileHandler",
                    "filename": LOG_APP_FILE,
                    "maxBytes": 1024 * 1024 * 15,  # 15MB
                    "backupCount": 10,
                    "formatter": "standard",
                },
                "console": {"level": "DEBUG", "class": "logging.StreamHandler", "formatter": "standard"},
            },
            "loggers": {
                "": {"handlers": ["general"], "level": "DEBUG", "propagate": True},
                LoggersName.INFO: {"handlers": ["info"], "level": "DEBUG", "propagate": True},
                LoggersName.REQUEST: {
                    "handlers": ["requests", "console"],
                    "level": "INFO",
                    "propagate": True,
                },
                LoggersName.REQUEST_DJANGO: {
                    "handlers": ["requests_with_trace"],
                    "level": "DEBUG",
                    "propagate": False,
                },
                LoggersName.EXCEPTIONS: {
                    "handlers": ["exceptions", "console"],
                    "level": "DEBUG",
                    "propagate": False,
                },
                LoggersName.DJANGO: {"handlers": ["django"], "level": "INFO", "propagate": True},
                APP_NAME: {"handlers": [APP_NAME, "console"], "level": "DEBUG", "propagate": True},
            },
        }
        print_django("Logs are set up.")


def setup_app_exposure_if_needed():
    global ALLOWED_HOSTS
    global API_ROOT_BASE
    API_ROOT_BASE = f"{API_VERSION}/"
    print_django("API_ROOT_BASE: " + API_ROOT_BASE)

    global ROOT_URLCONF
    ROOT_URLCONF = "hear.urls"

    # Sentry's browser SDK auto-attaches these to outgoing fetch/XHR calls for distributed
    # tracing; not in corsheaders' default_headers, so preflight rejects them otherwise.
    global CORS_ALLOW_HEADERS
    CORS_ALLOW_HEADERS = [*default_headers, "sentry-trace", "baggage"]

    # Browsers only expose a small safe list of response headers to JS by default; the session
    # download flow reads Content-Disposition for the filename and needs it exposed explicitly.
    global CORS_EXPOSE_HEADERS
    CORS_EXPOSE_HEADERS = ["Content-Length", "Content-Range", "Content-Disposition"]

    if APP_IS_EXPOSED:
        print_django("APP_IS_EXPOSED is true. Setting up security.")
        global SECURE_SSL_REDIRECT
        SECURE_SSL_REDIRECT = False
        print_django(f"SECURE_SSL_REDIRECT: {SECURE_SSL_REDIRECT}")
        global SESSION_COOKIE_SECURE
        SESSION_COOKIE_SECURE = True
        print_django(f"SESSION_COOKIE_SECURE: {SESSION_COOKIE_SECURE}")
        global CSRF_COOKIE_SECURE
        CSRF_COOKIE_SECURE = True
        print_django(f"CSRF_COOKIE_SECURE: {CSRF_COOKIE_SECURE}")

        CSRF_TRUSTED_ORIGINS_STR = load_required_str_env_var("CSRF_TRUSTED_ORIGINS")
        print_django(f"CSRF_TRUSTED_ORIGINS env variable: {CSRF_TRUSTED_ORIGINS_STR}")
        global CSRF_TRUSTED_ORIGINS
        CSRF_TRUSTED_ORIGINS = CSRF_TRUSTED_ORIGINS_STR.split(",")
        for csrf_trusted_origin in CSRF_TRUSTED_ORIGINS:
            csrf_trusted_origin = csrf_trusted_origin.strip()
            if csrf_trusted_origin == "":
                raise ValueError("An CSRF trusted origin is empty.")
        if len(CSRF_TRUSTED_ORIGINS) > 0:
            print_django("The app is exposed to the following origin(s):")
            for csrf_trusted_origin in CSRF_TRUSTED_ORIGINS:
                print_django(str(csrf_trusted_origin))
        else:
            raise OSError("The app is exposed but no trusted origins are set.")

        ALLOWED_HOSTS_STR = load_required_str_env_var("ALLOWED_HOSTS")
        ALLOWED_HOSTS = ALLOWED_HOSTS_STR.split(",")
        for csrf_trusted_origin in ALLOWED_HOSTS:
            csrf_trusted_origin = csrf_trusted_origin.strip()
            if csrf_trusted_origin == "":
                raise ValueError("An allowed host is empty.")
        if len(ALLOWED_HOSTS) > 0:
            print_django("Allowed host(s): ")
            for csrf_trusted_origin in ALLOWED_HOSTS:
                print_django(str(csrf_trusted_origin))
        else:
            raise OSError("The app is exposed but no allowed hosts are set.")

        add_loopback_hosts(ALLOWED_HOSTS, load_optional_str_env_var("APP_PORT", "8000"))

        CORS_ALLOWED_ORIGINS_STR = load_required_str_env_var("CORS_ALLOWED_ORIGINS")
        print_django(f"CORS_ALLOWED_ORIGINS env variable: {CORS_ALLOWED_ORIGINS_STR}")
        global CORS_ALLOWED_ORIGINS
        CORS_ALLOWED_ORIGINS = CORS_ALLOWED_ORIGINS_STR.split(",")
        for cors_allowed_origin in CORS_ALLOWED_ORIGINS:
            cors_allowed_origin = cors_allowed_origin.strip()
            if cors_allowed_origin == "":
                raise ValueError("A CORS allowed origin is empty.")
        if len(CORS_ALLOWED_ORIGINS) > 0:
            print_django("CORS is allowed for the following origin(s):")
            for cors_allowed_origin in CORS_ALLOWED_ORIGINS:
                print_django(str(cors_allowed_origin))
        else:
            raise OSError("The app is exposed but no CORS allowed origins are set.")

        CORS_ALLOWED_ORIGIN_REGEXES_STR = load_optional_str_env_var("CORS_ALLOWED_ORIGIN_REGEXES")
        global CORS_ALLOWED_ORIGIN_REGEXES
        CORS_ALLOWED_ORIGIN_REGEXES = (
            [p.strip() for p in CORS_ALLOWED_ORIGIN_REGEXES_STR.split(",") if p.strip()]
            if CORS_ALLOWED_ORIGIN_REGEXES_STR
            else []
        )
        if CORS_ALLOWED_ORIGIN_REGEXES:
            print_django("CORS is also allowed via regex pattern(s):")
            for pattern in CORS_ALLOWED_ORIGIN_REGEXES:
                print_django(pattern)
    else:
        ALLOWED_HOSTS = [
            "127.0.0.1",
            "127.0.0.1:8000",
            "127.0.0.1:8888",
            "localhost",
            "localhost:8000",
            "localhost:8888",
        ]
        global CORS_ALLOW_ALL_ORIGINS
        CORS_ALLOW_ALL_ORIGINS = True
        print_django(f"CORS_ALLOW_ALL_ORIGINS is set to: {CORS_ALLOW_ALL_ORIGINS}")

    print_django(f"ALLOWED_HOSTS is set to {ALLOWED_HOSTS}")


def setup_app_constants():
    # Before calling a view function, Django starts a transaction.
    # If the response is produced without problems, Django commits the transaction.
    # If the view produces an exception, Django rolls back the transaction.
    global ATOMIC_REQUESTS
    ATOMIC_REQUESTS = True

    # SECURITY WARNING: don't run with debug turned on in production!
    global DEBUG
    if "pytest" not in sys.argv[0]:  # Skip loading DEBUG from env in test mode
        DEBUG = load_required_bool_env_var("DEBUG")
        if APP_IS_EXPOSED and DEBUG:
            print_django(
                "SECURITY WARNING: DEBUG is True while APP_IS_EXPOSED — disable DEBUG in production/staging servers."
            )
    # else: keep the module-level DEBUG value (False by default, can be set to True by conftest)

    global USER_LIBRARIES_DIR_NAME_PREFIXE
    USER_LIBRARIES_DIR_NAME_PREFIXE = "user_"
    global TEST_USER_LIBRARIES_DIR_NAME_PREFIXE
    TEST_USER_LIBRARIES_DIR_NAME_PREFIXE = "test_user_"
    global USER_MAX_NUMBER
    USER_MAX_NUMBER = "10000000"  # hehe

    global UUID_LEN
    UUID_LEN = 36

    global LANGUAGE_LEN_MAX
    LANGUAGE_LEN_MAX = 3

    global FILE_PATH_MAX_LENGTH
    FILE_PATH_MAX_LENGTH = 256
    global UPLOADED_TRACK_FILE_SIZE_MIN_IN_MO
    UPLOADED_TRACK_FILE_SIZE_MIN_IN_MO = 0
    global UPLOADED_TRACK_FILE_SIZE_MAX_IN_MO
    UPLOADED_TRACK_FILE_SIZE_MAX_IN_MO = 300
    # Force all uploads to be written to disk by setting memory size to 0
    global FILE_UPLOAD_MAX_MEMORY_SIZE
    FILE_UPLOAD_MAX_MEMORY_SIZE = 0  # Force all uploads to disk
    # Set max upload size limit
    global DATA_UPLOAD_MAX_MEMORY_SIZE
    DATA_UPLOAD_MAX_MEMORY_SIZE = UPLOADED_TRACK_FILE_SIZE_MAX_IN_MO * 1024 * 1024  # Convert MB to bytes

    global UPLOADED_TRACK_FILE_EXTENSIONS
    UPLOADED_TRACK_FILE_EXTENSIONS = [".mp3", ".flac", ".wav"]
    global UPLOADED_TRACK_FILE_CONTENT_TYPES
    UPLOADED_TRACK_FILE_CONTENT_TYPES = ["audio/mpeg", "audio/flac", "audio/wav"]
    global UPLOADED_TRACK_FILENAME_LEN_MAX
    UPLOADED_TRACK_FILENAME_LEN_MAX = 150
    global UPLOADED_TRACK_FILENAME_GENERATED_WITHOUT_EXTENSION_LENGTH
    UPLOADED_TRACK_FILENAME_GENERATED_WITHOUT_EXTENSION_LENGTH = 20
    global UPLOADED_TRACK_TITLE_LEN_MAX
    UPLOADED_TRACK_TITLE_LEN_MAX = 256
    global UPLOADED_TRACK_TITLE_LEN_MAX_ID3V1
    UPLOADED_TRACK_TITLE_LEN_MAX_ID3V1 = 30
    global UPLOADED_TRACK_TRACK_NUMBER_MAX
    UPLOADED_TRACK_TRACK_NUMBER_MAX = 1000
    global UPLOADED_TRACK_FILENAME_EXPRESSIONS_TO_EXCLUDE_GENERATING_TITLE
    UPLOADED_TRACK_FILENAME_EXPRESSIONS_TO_EXCLUDE_GENERATING_TITLE = [
        "myfreemp3.vip",
        "myfreemp3",
    ]  # The order matters
    global UPLOADED_TRACK_GENERATED_TITLE_LENGTH
    UPLOADED_TRACK_GENERATED_TITLE_LENGTH = 20
    global UPLOADED_TRACK_GENERATED_TITLE_PREFIXE
    UPLOADED_TRACK_GENERATED_TITLE_PREFIXE = "htmt_"
    global UPLOADED_TRACK_RATING_VALUE_MAX
    UPLOADED_TRACK_RATING_VALUE_MAX = 10

    global TRACK_TITLE_LEN_MAX
    TRACK_TITLE_LEN_MAX = 2048
    global TRACK_TRACK_NUMBER_MAX
    TRACK_TRACK_NUMBER_MAX = 1000
    global TRACK_RATING_VALUE_MAX
    TRACK_RATING_VALUE_MAX = 10

    global MINE_TRACK_TITLE_LEN_MAX
    MINE_TRACK_TITLE_LEN_MAX = 256
    global MINE_TRACK_RELEASED_ON_LEN_MAX
    MINE_TRACK_RELEASED_ON_LEN_MAX = 20
    global MINE_TRACK_URL_LEN_MAX
    MINE_TRACK_URL_LEN_MAX = 1000

    global ALBUM_NAME_LEN_MAX
    ALBUM_NAME_LEN_MAX = 256
    global ALBUM_NAME_LEN_MAX_ID3V1
    ALBUM_NAME_LEN_MAX_ID3V1 = 30
    global ALBUM_ARTISTS_NAMES_FIELD_LEN_MAX
    ALBUM_ARTISTS_NAMES_FIELD_LEN_MAX = 256
    global ARTIST_NAME_LEN_MAX
    ARTIST_NAME_LEN_MAX = 256
    global ARTIST_NAME_LEN_MAX_ID3V1
    ARTIST_NAME_LEN_MAX_ID3V1 = 30
    global ARTISTS_NAMES_LEN_MAX
    ARTISTS_NAMES_LEN_MAX = 256
    global CRITERIA_TYPE_LABEL_LEN_MAX
    CRITERIA_TYPE_LABEL_LEN_MAX = 255
    global CRITERIA_NAME_LEN_MAX
    CRITERIA_NAME_LEN_MAX = 256
    global MANUAL_PLAYLIST_NAME_LEN_MAX
    MANUAL_PLAYLIST_NAME_LEN_MAX = 256

    global FINGERPRINTING_ERROR_MESSAGE_LEN_MAX
    FINGERPRINTING_ERROR_MESSAGE_LEN_MAX = 256
    global FINGERPRINTING_ERROR_CODE_LABEL_LEN_MAX
    FINGERPRINTING_ERROR_CODE_LABEL_LEN_MAX = 256

    MUSICBRAINZ_BASE_URL = "https://musicbrainz.org/"
    global MB_ID_LEN_MAX
    MB_ID_LEN_MAX = 36
    global MB_RECORDING_URL
    MB_RECORDING_URL = MUSICBRAINZ_BASE_URL + "recording/"
    global MB_RECORDING_TITLE_LEN_MAX
    MB_RECORDING_TITLE_LEN_MAX = 256
    global MB_RECORDING_MISSING_CAUSE_CODE_LABEL_LEN_MAX
    MB_RECORDING_MISSING_CAUSE_CODE_LABEL_LEN_MAX = 256

    # Needs a large text for messages like:
    # "HTTP request failed: HTTPConnectionPool(host='api.acoustid.org', port=80): Max retries exceeded with url:
    # /v2/lookup (Caused by NameResolutionError(\"<urllib3.connection.HTTPConnection object at 0x10a884170>: Failed to
    # resolve 'api.acoustid.org' ([Errno 8] nodename nor servname provided, or not known)\"))"
    global MB_RECORDING_MISSING_CAUSE_MESSAGE_LEN_MAX
    MB_RECORDING_MISSING_CAUSE_MESSAGE_LEN_MAX = 400
    global MB_ARTIST_URL
    MB_ARTIST_URL = MUSICBRAINZ_BASE_URL + "artist/"
    global MB_ARTIST_NAME_LEN_MAX
    MB_ARTIST_NAME_LEN_MAX = 256

    global PAGINATION_PAGE_SIZE_DEFAULT
    PAGINATION_PAGE_SIZE_DEFAULT = 30
    global PAGINATION_PAGE_SIZE_MULTIMODEL_DEFAULT
    PAGINATION_PAGE_SIZE_MULTIMODEL_DEFAULT = PAGINATION_PAGE_SIZE_DEFAULT
    global PAGINATION_PAGE_SIZE_MAX
    PAGINATION_PAGE_SIZE_MAX = 100

    global CRITERIA_TREE_IMPORT_MAX_ROOT_COUNT
    CRITERIA_TREE_IMPORT_MAX_ROOT_COUNT = 1000
    global CRITERIA_TREE_IMPORT_MAX_TOTAL_COUNT
    CRITERIA_TREE_IMPORT_MAX_TOTAL_COUNT = 30000
    global CRITERIA_TREE_IMPORT_STALE_DELETE_MAX_FRACTION
    CRITERIA_TREE_IMPORT_STALE_DELETE_MAX_FRACTION = 0.5


def setup_afp_connection():
    global AFP_BASE_URL
    global AFP_POST_ENDPOINT
    if APP_IS_EXPOSED:
        print_django("The app is exposed. AFP is reached at its public URL over HTTPS.")
        AFP_BASE_URL = load_required_str_env_var("AFP_URL")
    else:
        print_django("The app is not exposed. AFP is reached at its url and port over HTTP.")
        AFP_BASE_URL = f"http://{load_required_str_env_var('AFP_URL')}:{load_required_str_env_var('AFP_PORT')}"

    AFP_POST_ENDPOINT = load_required_str_env_var("AFP_POST_ENDPOINT")

    print_django(f"AFP: {AFP_BASE_URL}/{AFP_POST_ENDPOINT}")


def setup_static_files():
    print_django(f"The app is using static files for {STATIC_FILES_STATE}")

    # Django constant, do not rename.
    global STATIC_ROOT
    STATIC_ROOT = Path(STATIC_FILES)  # type: ignore
    print_django("STATIC_ROOT: " + str(STATIC_ROOT))
    if not STATIC_ROOT.exists():
        raise OSError(f"The static root {STATIC_ROOT} does not exist.")
    print_django(f"The dir {STATIC_ROOT} exists.")

    global STATIC_URL
    STATIC_URL = load_required_str_env_var("STATIC_FILES_URL")
    # STATICFILES_DIRS = [] # No additional static files directories are needed.


def setup_installed_apps_and_caches():
    global INSTALLED_APPS
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django_extensions",
        "polymorphic",
        "corsheaders",
        "drf_spectacular",
        "rest_framework",
        "rest_framework.authtoken",
        "drf_multiple_model",
        "the_music_tree_genre_kit",
        "hear",
    ]

    if APP_IS_EXPOSED:
        INSTALLED_APPS.append("rest_framework_simplejwt")

    if STATIC_FILES_STATE in [StaticFileStates.COLLECTING, StaticFileStates.SERVING]:
        INSTALLED_APPS.append("django.contrib.staticfiles")

    global CACHES
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
            "LOCATION": "unique-snowflake",
        }
    }


def setup_middlewares():
    """Setup Django middleware classes. Top middleware classes are executed first."""
    global MIDDLEWARE
    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "corsheaders.middleware.CorsMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "the_music_tree_api_kit.view.middleware.HostValidationMiddleware.HostValidationMiddleware",
        "django.middleware.common.CommonMiddleware",
        "hear.middleware.ContentTypeValidationMiddleware.ContentTypeValidationMiddleware",
        "the_music_tree_api_kit.view.middleware.CamelToSnakeMiddleware.CamelToSnakeMiddleware",
        "hear.middleware.content_validity.middleware.ContentValidityMiddleware",
        "hear.middleware.test_client.middleware.TestClientEmptyListMiddleware",
        "hear.middleware.list_value_validation.middleware.ListValueValidationMiddleware",
        "hear.middleware.duplicate_fields.middleware.DuplicateFieldsMiddleware",
        "hear.middleware.RequestLoggingMiddleware.RequestLoggingMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]


def setup_db_connection():
    global DATABASES
    DATABASES = {
        "default": {
            **dj_database_url.parse(os.environ["DATABASE_URL"], conn_max_age=600),
            "DISABLE_SERVER_SIDE_CURSORS": True,
        }
    }


def setup_templates():
    global TEMPLATES
    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]


def setup_django_constants():
    global APP_TITLE
    APP_TITLE = load_required_str_env_var("APP_TITLE")

    global WSGI_APPLICATION
    WSGI_APPLICATION = "hear.wsgi.application"

    global AUTH_USER_MODEL
    AUTH_USER_MODEL = "hear.User"

    global CRITERIA_MODEL
    CRITERIA_MODEL = "hear.Criteria"

    global TRACK_MODEL
    TRACK_MODEL = "hear.UploadedTrack"

    global ARTIST_MODEL
    ARTIST_MODEL = "hear.Artist"

    global ALBUM_MODEL
    ALBUM_MODEL = "hear.Album"

    global AUTH_PASSWORD_VALIDATORS
    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
        },
        {
            "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
        },
    ]
    global LANGUAGE_CODE
    LANGUAGE_CODE = "en-us"
    global TIME_ZONE
    TIME_ZONE = "UTC"
    global USE_I18N
    USE_I18N = True
    global USE_TZ
    USE_TZ = True
    global DEFAULT_AUTO_FIELD
    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
    global REST_FRAMEWORK
    REST_FRAMEWORK = {
        "DEFAULT_RENDERER_CLASSES": ("djangorestframework_camel_case.render.CamelCaseJSONRenderer",),
        "DEFAULT_PARSER_CLASSES": (
            "djangorestframework_camel_case.parser.CamelCaseJSONParser",
            "djangorestframework_camel_case.parser.CamelCaseMultiPartParser",
            "djangorestframework_camel_case.parser.CamelCaseFormParser",
        ),
        "DEFAULT_PAGINATION_CLASS": "the_music_tree_api_kit.view.pagination.AppPagination.AppPagination",
        "PAGE_SIZE": 30,
        "DEFAULT_AUTHENTICATION_CLASSES": ("rest_framework_simplejwt.authentication.JWTAuthentication",),
        "DEFAULT_PERMISSION_CLASSES": [
            "rest_framework.permissions.AllowAny",
        ],
        "DEFAULT_METADATA_CLASS": "rest_framework.metadata.SimpleMetadata",
        "DEFAULT_SCHEMA_CLASS": "hear.view.schema.AppAutoSchema.AppAutoSchema",
        "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.URLPathVersioning",
        "DEFAULT_VERSION": "v1",
        "ALLOWED_VERSIONS": "v1",
        "EXCEPTION_HANDLER": "hear.view.error.exception_handler.custom_exception_handler",
    }

    global SPECTACULAR_SETTINGS
    SPECTACULAR_SETTINGS = {
        "TITLE": APP_TITLE,
        "DESCRIPTION": "API to handle genre oriented music libraries",
        "VERSION": APP_VERSION,
        "SERVE_INCLUDE_SCHEMA": False,
        "SCHEMA_PATH_PREFIX": r"/v[\d.]+",
        "COMPONENT_SPLIT_REQUEST": True,
        "COMPONENT_NO_READ_ONLY_REQUIRED": True,
        "APPEND_COMPONENTS": {
            "securitySchemes": {
                "Bearer": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT",
                }
            }
        },
        "SECURITY": [{"Bearer": []}],
    }

    global SIMPLE_JWT
    SIMPLE_JWT = {
        "ACCESS_TOKEN_LIFETIME": datetime.timedelta(minutes=100),
        "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=1),
        "AUTH_HEADER_TYPES": ("Bearer",),
    }


def _load_service_feature_flags():
    global AFP_ENABLED
    global MUSICBRAINZ_LOOKUP_ENABLED
    AFP_ENABLED = load_required_bool_env_var("AFP_ENABLED")
    MUSICBRAINZ_LOOKUP_ENABLED = load_required_bool_env_var("MUSICBRAINZ_LOOKUP_ENABLED")
    if MUSICBRAINZ_LOOKUP_ENABLED and not AFP_ENABLED:
        raise OSError(
            "MUSICBRAINZ_LOOKUP_ENABLED cannot be true when AFP_ENABLED is false (MusicBrainz lookup requires fingerprinting)."
        )
    print_django("AFP is enabled." if AFP_ENABLED else "AFP is disabled.")
    print_django("MusicBrainz lookup is enabled." if MUSICBRAINZ_LOOKUP_ENABLED else "MusicBrainz lookup is disabled.")


def _load_optional_service_credentials():
    """Load ACOUSTID, Spotify and Google OAuth env; call after _load_service_feature_flags()."""
    global ACOUSTID_API_KEY
    global SPOTIFY_ENABLED
    global SPOTIFY_CLIENT_ID
    global SPOTIFY_CLIENT_SECRET
    global SPOTIFY_REDIRECT_URI
    global SPOTIFY_SCOPES
    global GOOGLE_OAUTH_ENABLED
    global GOOGLE_CLIENT_ID
    global GOOGLE_CLIENT_SECRET
    global GOOGLE_REDIRECT_URI

    if MUSICBRAINZ_LOOKUP_ENABLED:
        ACOUSTID_API_KEY = load_required_secret_env_var("ACOUSTID_API_KEY")
        print_django("MusicBrainz lookup enabled; ACOUSTID_API_KEY loaded.")
    else:
        ACOUSTID_API_KEY = load_optional_secret_env_var("ACOUSTID_API_KEY")
        print_django("MusicBrainz lookup disabled; ACOUSTID_API_KEY not required.")

    SPOTIFY_ENABLED = load_required_bool_env_var("SPOTIFY_ENABLED")
    if SPOTIFY_ENABLED:
        SPOTIFY_CLIENT_ID = load_required_str_env_var("SPOTIFY_CLIENT_ID", silent=True)
        SPOTIFY_CLIENT_SECRET = load_required_secret_env_var("SPOTIFY_CLIENT_SECRET", silent=True)
        SPOTIFY_REDIRECT_URI = load_required_str_env_var("SPOTIFY_REDIRECT_URI", silent=True)
        SPOTIFY_SCOPES = load_required_str_env_var("SPOTIFY_SCOPES", silent=True)
        if is_django_startup_verbose():
            print_django(f"SPOTIFY_CLIENT_ID = {SPOTIFY_CLIENT_ID}")
            print_django("SPOTIFY_CLIENT_SECRET is set.")
            print_django(f"SPOTIFY_REDIRECT_URI = {SPOTIFY_REDIRECT_URI}")
            print_django(f"SPOTIFY_SCOPES = {SPOTIFY_SCOPES}")
        else:
            print_django(f"SPOTIFY_CLIENT_ID: {mask_oauth_client_id(SPOTIFY_CLIENT_ID)} (set)")
            print_django("SPOTIFY_CLIENT_SECRET is set.")
            print_django("SPOTIFY_REDIRECT_URI and SPOTIFY_SCOPES are set.")
        print_django("Spotify API credentials loaded.")
    else:
        SPOTIFY_CLIENT_ID = load_optional_str_env_var("SPOTIFY_CLIENT_ID")
        SPOTIFY_CLIENT_SECRET = load_optional_secret_env_var("SPOTIFY_CLIENT_SECRET")
        SPOTIFY_REDIRECT_URI = load_optional_str_env_var("SPOTIFY_REDIRECT_URI")
        SPOTIFY_SCOPES = load_optional_str_env_var("SPOTIFY_SCOPES")
        print_django("Spotify disabled; credentials not loaded.")

    GOOGLE_OAUTH_ENABLED = load_required_bool_env_var("GOOGLE_OAUTH_ENABLED")
    if GOOGLE_OAUTH_ENABLED:
        GOOGLE_CLIENT_ID = load_required_str_env_var("GOOGLE_CLIENT_ID", silent=True)
        GOOGLE_CLIENT_SECRET = load_required_secret_env_var("GOOGLE_CLIENT_SECRET", silent=True)
        GOOGLE_REDIRECT_URI = load_required_str_env_var("GOOGLE_REDIRECT_URI", silent=True)
        if is_django_startup_verbose():
            print_django(f"GOOGLE_CLIENT_ID = {GOOGLE_CLIENT_ID}")
            print_django("GOOGLE_CLIENT_SECRET is set.")
            print_django(f"GOOGLE_REDIRECT_URI = {GOOGLE_REDIRECT_URI}")
        else:
            print_django(f"GOOGLE_CLIENT_ID: {mask_oauth_client_id(GOOGLE_CLIENT_ID)} (set)")
            print_django("GOOGLE_CLIENT_SECRET is set.")
            print_django("GOOGLE_REDIRECT_URI is set.")
        print_django("Google OAuth credentials loaded.")
    else:
        GOOGLE_CLIENT_ID = load_optional_str_env_var("GOOGLE_CLIENT_ID")
        GOOGLE_CLIENT_SECRET = load_optional_secret_env_var("GOOGLE_CLIENT_SECRET")
        GOOGLE_REDIRECT_URI = load_optional_str_env_var("GOOGLE_REDIRECT_URI")
        print_django("Google OAuth disabled; credentials not loaded.")


def setup_media_dirs():
    print_django("FILE_UPLOAD_TEMP_DIR is set. Setting up the media variables...")

    global MEDIA_ROOT  # Django constant, do not rename.
    MEDIA_ROOT = load_required_path_env_var("MEDIA_DIR")

    if APP_IS_EXPOSED:
        global MEDIA_URL
        MEDIA_URL = load_required_str_env_var("MEDIA_URL")

    global LIBRARIES_DIR
    LIBRARIES_DIR = load_required_path_env_var("LIBRARIES_DIR")
    print_django("LIBRARIES_DIR: " + str(LIBRARIES_DIR))
    if not LIBRARIES_DIR.is_dir():
        raise OSError(
            f"The libraries directory {LIBRARIES_DIR} does not exist. "
            "Run filesystem setup (e.g. scripts/setup-filesystem.sh in the container entrypoint) before starting Django."
        )
    print_django("The LIBRARIES_DIR directory exists.")
    print_django("Media variables are set.")


def set_secret_key():
    global SECRET_KEY
    if APP_IS_EXPOSED:
        # SECURITY WARNING: keep the secret key used in production secret!
        # SECRET_KET is a Django constant, do not rename.
        SECRET_KEY = load_required_secret_env_var("DJANGO_SECRET_KEY")
    else:
        SECRET_KEY = "django_default_secret_when_not_exposed"


BASE_DIR = Path(__file__).resolve().parent.parent

# URL prefix is an API contract, deliberately independent of the release version.
API_VERSION = "v2"
with open(BASE_DIR / "pyproject.toml", "rb") as pyproject_file:
    APP_VERSION: str = tomllib.load(pyproject_file)["project"]["version"]

APP_ENV_FILE_RELATIVE_PATH = os.getenv("ENV_FILE", "env/.env")
APP_ENV_FILE = BASE_DIR / APP_ENV_FILE_RELATIVE_PATH
load_env_vars_from_file_if_exists(APP_ENV_FILE)
GIT_COMMIT = load_optional_str_env_var("GIT_COMMIT") or None

ENV = load_required_str_env_var("ENV")
APP_NAME = load_required_str_env_var("APP_NAME")
APP_IS_EXPOSED = load_required_bool_env_var("APP_IS_EXPOSED")

set_secret_key()

if "pytest" in sys.argv[0]:
    print_django("settings.py is being executed because of a pytest command.")
    PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]  # Less secured to speed up tests

if "loaddata" in sys.argv:
    print_django("settings.py is being executed because of a loaddata command.")
    STATIC_FILES_STATE = StaticFileStates.NOT_NEEDED
    _load_service_feature_flags()
    _load_optional_service_credentials()
    setup_app_constants()
    setup_installed_apps_and_caches()
    setup_middlewares()
    setup_django_constants()
    setup_db_connection()
    setup_templates()  # Needed to use the admin application
    setup_media_dirs()  # Needed for the User model library path field
else:
    _load_service_feature_flags()
    _load_optional_service_credentials()
    setup_app_exposure_if_needed()
    setup_app_constants()

    STATIC_FILES = os.getenv("STATIC_FILES")
    if ENV == "collect_static":
        STATIC_FILES_STATE = StaticFileStates.COLLECTING
        LIBRARIES_DIR = Path()  # Needed to setup the database (User model)
        setup_static_files()
    elif not STATIC_FILES:
        print_django("Static files are not needed.")
        STATIC_FILES_STATE = StaticFileStates.NOT_NEEDED
    else:
        print_django("Static files are being served.")
        STATIC_FILES_STATE = StaticFileStates.SERVING
        setup_static_files()

    setup_installed_apps_and_caches()
    setup_middlewares()
    setup_templates()
    setup_django_constants()
    init_logs_if_needed()

    if os.environ.get("DATABASE_URL"):
        setup_db_connection()

    # FILE_UPLOAD_TEMP_DIR is a Django constant, do not rename.
    FILE_UPLOAD_TEMP_DIR = os.getenv("TMP_UPLOADED_FILES")
    print_django(f"FILE_UPLOAD_TEMP_DIR: {FILE_UPLOAD_TEMP_DIR}")

    FILE_UPLOAD_ENABLED = load_required_bool_env_var("FILE_UPLOAD_ENABLED")

    if not FILE_UPLOAD_ENABLED:
        print_django("FILE_UPLOAD_ENABLED is false. The app will not handle media files.")
        METADATA_SESSION_DIR = None
        if os.getenv("AFP_ENABLED", "").lower() == "true":
            raise OSError("The AFP_ENABLED env variable cannot be true when FILE_UPLOAD_ENABLED is false.")
        for var_name in [
            "AFP_PORT",
            "AFP_URL",
            "AFP_POST_ENDPOINT",
            "ACOUSTID_API_KEY",
            "MEDIA_DIR",
            "METADATA_SESSION_DIR",
            "LIBRARIES_DIR",
            "TMP_UPLOADED_FILES",
        ]:
            if os.getenv(var_name):
                raise OSError(f"The {var_name} env variable cannot be set as FILE_UPLOAD_ENABLED is false.")
    else:
        if not FILE_UPLOAD_TEMP_DIR:
            raise OSError("TMP_UPLOADED_FILES/FILE_UPLOAD_TEMP_DIR must be set when FILE_UPLOAD_ENABLED is true.")
        METADATA_SESSION_DIR = Path(load_required_str_env_var("METADATA_SESSION_DIR")).resolve()
        setup_media_dirs()
        if AFP_ENABLED:  # pyright: ignore[reportUnboundVariable]
            setup_afp_connection()

print_django("Finished loading settings.")
if CiStartupTraceEnabled.is_tracer_active():
    from hear.CiPytestStartupTracer import CiPytestStartupTracer

    CiPytestStartupTracer.install_ci_startup_tracers()
    print(
        "[Django] Next: django.setup() → apps.populate() → get_resolver() on demand imports hear.urls. "
        "Long gaps: last printed phase before silence = where it is stuck.",
        flush=True,
    )
