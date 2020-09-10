import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate
from thinkdsp import read_wave
from thinkdsp import play_wave

import matplotlib.pyplot as plt

frecuencia1336 = SinSignal(freq=1336, amp=1, offset=0)
frecuencia697 = SinSignal(freq=697, amp=1, offset=0)
frecuencia770 = SinSignal(freq=770, amp=1, offset=0)

frecuencia2 = frecuencia697 + frecuencia1336
frecuencia5 = frecuencia770 + frecuencia1336

wave_2 = frecuencia2.make_wave(duration=1.5, start=0, framerate=44100)
wave_5 = frecuencia5.make_wave(duration=0.5, start=1.5, framerate=44100)


wave_sonido = wave_2 + wave_5


wave_sonido.write("output.wav")






