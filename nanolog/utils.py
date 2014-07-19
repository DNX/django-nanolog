from django.conf import settings
from nanolog.models import Nanolog


def nanolog(user, log_type, details, note=None, object=None):
    """
    Write into Nanolog the received data.

    <log_type>  - string
    <details>   - string
    <note>      - string
    """
    Nanolog.objects.create(user=user,
                            log_type=log_type,
                            details=details,
                            note=note)
