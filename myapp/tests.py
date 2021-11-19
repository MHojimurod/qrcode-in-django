
from django.core.exceptions import ValidationError

val = URLValidator()
try:
    val('https://kun.uz')
except ValidationError as e:
    print("aA")