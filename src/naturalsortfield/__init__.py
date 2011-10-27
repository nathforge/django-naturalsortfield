try:
    from naturalsortfield.fields import NaturalSortField
except ImportError:
    try:
        import django.db.models
    except ImportError:
        pass # Django's not installed or configured. Ah well. We can at least expose version info.
    else:
        raise # Django's fine, something else is wrong.


VERSION = (0, 1)

def version_string():
    return '.'.join(str(component) for component in VERSION)
