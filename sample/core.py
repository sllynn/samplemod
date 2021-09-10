# -*- coding: utf-8 -*-
from . import helpers

def get_hmm():
    """Get a thought."""
    return 'hmmm...'
  
def get_huh():
    """Question your existence."""
    return 'huh...'

def hmm():
    """Contemplation..."""
    answer = helpers.get_answer()
    if answer:
      print(get_hmm())
    else:
      print(get_huh())