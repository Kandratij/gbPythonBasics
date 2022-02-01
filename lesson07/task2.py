# 2. * Написать скрипт, создающий из config.yaml стартер для проекта
import json
import os


def create_structure(obj, obj_path='./'):
    if obj['type'] == 'file' and not os.path.exists(obj_path+obj['name']):
        open(obj_path+obj['name'], 'tw', encoding='utf-8')
    elif obj['type'] == 'dir':
        if not os.path.exists(obj_path + obj['name']):
            os.mkdir(obj_path + obj['name'])
    if 'child' in obj:
        for child in obj['child']:
            create_structure(child, obj_path+obj['name']+'/')


with open('config.yaml', 'r') as cfg:
    create_structure(json.load(cfg))
