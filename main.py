#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'main file to start the program '

__author__ = 'Gxz'

import weblfasr_python3_demo as KDXFweb
import RecorderConfig as config
import PyAudioOfficial as audio
import json

if __name__ == '__main__':
    audio.myRecord()
    api =KDXFweb.RequestApi(appid="your appid", secret_key="your secretary key", upload_file_path=audio.RECORDFILE)
    api.all_api_request()
