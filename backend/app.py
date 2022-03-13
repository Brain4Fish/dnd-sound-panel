from flask import Flask, request, send_file
import glob
import json

app = Flask(__name__)

ROOT_PATH = 'backend/sounds'

# TODO: allow to change sounds dir


@app.route('/api/v1/get_sound_dirs')
def get_sound_dirs():
    return parse_dirs()


def parse_dirs(path=ROOT_PATH):
    dirs_json = {}
    dirs = glob.glob(f'{path}/*')
    dirs_json['dirs'] = dirs
    return json.dumps(dirs_json)


@app.route('/api/v1/get_sounds/<dir>')
def get_sounds(dir, path=ROOT_PATH):
    sounds_json = {}
    sounds = glob.glob(f'{path}/{dir}/*')
    sounds_json['sounds'] = sounds
    return json.dumps(sounds_json)


@app.route('/api/v1/play_sound')
def play_sound():
    sound = request.args.get('sound')
    splitted_path = sound.split('/')
    relative_path = '/'.join(splitted_path[1:])
    return send_file(relative_path)
