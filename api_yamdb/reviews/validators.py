import datetime as dt
import re

from django.core.exceptions import ValidationError


PATTERN = r'^[\w.@+-]+\z'
SYMBOL_NAMES = {' ': 'пробел', ',': 'запятая', '/': 'слэш', '\\': 'бэк-слэш'}


class validator_username:

    def symbol_name(symbol):
        return SYMBOL_NAMES.get(symbol, symbol)

    def username_validator(value):
        if value == 'me':
            raise ValidationError(
                'Для имени пользователя нельзя использовать "me"'
            )
        forbidden = list(set(''.join(re.findall(PATTERN, value))))
        if forbidden:
            raise ValidationError(
                (f'Символы {", ".join(map(SYMBOL_NAMES, forbidden))} '
                    'нельзя использовать в имени')
            )
        return value


def validate_year(value):
    if 0 > value > dt.datetime.now().year:
        raise ValidationError(
            'Некорректный год выпуска!')
    return
