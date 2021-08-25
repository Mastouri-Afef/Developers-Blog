from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import ugettext_lazy as _


class DomainUnicodeUsernameValidator(UnicodeUsernameValidator):
    """Allows \."""
    regex = r'^[\w.@+-\\]+$'
    message = _(
        'Enter a valid username. This value may contain only letters, '
        'numbers, and \/@/./+/-/_ characters.'
    )

