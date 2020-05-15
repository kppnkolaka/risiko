from .kemungkinan import Kemungkinan
from .dampak import Dampak

def referensi(kategori):
  if kategori == 'kemungkinan':
    return Kemungkinan()
  elif kategori == 'dampak':
    return Dampak()