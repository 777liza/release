# finance/context_processors.py
from .text_constants import SITE_TEXT

def global_text_constants(request):
    return {'site_text': SITE_TEXT}

