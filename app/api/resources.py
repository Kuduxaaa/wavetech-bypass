# -*- coding: utf-8 -*-
# Coded By Kuduxaaa

from flask_restful import Resource
from flask import request, jsonify, Response

from app.service import get_audio
from base64 import b64decode

from pydub import AudioSegment

import io
import uuid
import os

def get_data(fname):
    with open(fname, 'rb') as fwav:
        data = fwav.read(1024)
        while data:
            yield data
            data = fwav.read(1024)
        
    os.remove(fname)

# TTS Engine
class TTS(Resource):
    def get(self):
        
        if 'text' not in request.args:
            return jsonify({
                'message': 'required data is missing',
                'success': False,
                'code': 400
            })
            
            
        limit = 250
        version = 'ge_m0'
        text = request.args.get('text')
        splitted = [text[i:i+limit] for i in range(0, len(text), limit)]
        
        if 'version' in request.args:
            version = request.args.get('version')
            
        if len(splitted) == 1:
            data = get_audio(text, version)
            
            if data is not None and 'file' in data:
                encoded_audio = data.get('file')
                audio = b64decode(encoded_audio)
                
                return Response(audio, mimetype='audio/wav')
            
            return data

        combined = AudioSegment.empty()
        
        for text in splitted:
            data = get_audio(text, version)
            audio = b64decode(data.get('file'))
            
            as_file = io.BytesIO(audio)
            audio_segment = AudioSegment.from_file(as_file)
            combined += audio_segment
        
        fname = f'/tmp/{str(uuid.uuid4())}.wav'
        combined.export(fname, format='wav')
        
        return Response(get_data(fname), mimetype="audio/wav")

    def post(self):
        """
        Route post method
        type something :)
        happy coding
        """

        pass


    def delete(self):
        """
        Route delete method
        type something :)
        happy coding
        """

        pass