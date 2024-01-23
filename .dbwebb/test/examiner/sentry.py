"""
Handles integration to Sentry
"""
from functools import wraps
try:
    import sentry_sdk
    from sentry_sdk.integrations import atexit
except ImportError:
    pass
from examiner.cli_parser import parse

ARGS = parse()

def if_enabled():
    """
    wrapper for sentry functions to block them if sentry is not available
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if ARGS.sentry:
                return f(*args, **kwargs)
            return None

        wrapper.__wrapped__ = f # used to assert that method has been decorated
        return wrapper
    return decorator


@if_enabled()
def activate_sentry(url, release, sample_rate, user, kmom):
    """
    config
    https://docs.sentry.io/platforms/python/configuration/options/
    https://getsentry.github.io/sentry-python/apidocs.html
    """
    def null(*args, **kwargs): # pylint: disable=unused-argument
        """
        Use to silence sentry from printing
        """
    atexit.default_callback = null
    sentry_sdk.init(
        dsn=url,
        send_default_pii=False,
        send_client_reports=False,
        server_name=user,
        release=release,
        sample_rate=sample_rate,
        shutdown_timeout=1.5,
    )

    sentry_sdk.set_user({"id": user})
    sentry_sdk.set_tag("kmom", kmom)



@if_enabled()
def add_exception(value, err):
    """
    unittests suppress exceptions so Sentry does not get them. Therefore we have to manually capture errors from tests.
    Make extinction on if students code crash or if its an assertError. So we can filter on it in sentry.
    """
    if isinstance(value, AssertionError):
        with sentry_sdk.push_scope() as scope:
            scope.level = "warning"
            sentry_sdk.capture_exception(err)
    else:
        sentry_sdk.capture_exception(err)
