import random
import string
from core.config import settings


def generate_short_url(length: int = settings.SHORT_CODE_LENGTH) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

