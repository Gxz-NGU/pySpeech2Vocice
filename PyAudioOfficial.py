#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'PyAudio official usage for recording and playing' 

__author__ = 'Gxz'

import pyaudio
import wave
import sys
import RecorderConfig as config
import os
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORDFILE=os.path.join(config.WAVE_OUTPUT_PATH,config.WAVE_OUTPUT_FILENAME+".wav")

try:
    os.stat(config.WAVE_OUTPUT_PATH)
except:
    os.mkdir(config.WAVE_OUTPUT_PATH)


def myRecord():
    """PyAudio example: Record a few seconds of audio and save to a WAVE file."""
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * config.RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(RECORDFILE, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def play():
    
    """PyAudio Example: Play a WAVE file."""

    # if len(sys.argv) < 2:
    #     print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    #     sys.exit(-1)

    # wf = wave.open(sys.argv[1], 'rb')
    wf = wave.open(RECORDFILE, 'rb')
    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()


if __name__ == '__main__':
    myRecord()
    play()