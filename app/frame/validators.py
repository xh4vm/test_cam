from typing import Any
from jsonschema import validate


def video_color_schema_validator(video_frame : dict[str, Any]):
    schema = {
        'type': 'object',
        'properties': {
            'Brightness': {'type': 'number', 'minimum': 0, 'maximum': 100},
            'Contrast': {'type': 'number', 'minimum': 0, 'maximum': 100},
            'Hue': {'type': 'number', 'minimum': 0, 'maximum': 100},
            'Saturation': {'type': 'number', 'minimum': 0, 'maximum': 100}
        },
        'required': ['Brightness', 'Contrast', 'Hue', 'Saturation']
    }
    validate(instance=video_frame, schema=schema)

def frame_id_validator(id: int):
    if not 0 < id < 1000:
        raise ValueError('Frame id value must be into interval (0, 1000)')

def cam_id_validator(id : int):
    if not 0 < id < 100:
        raise ValueError('Cam id value must be into interval (0, 100)')

def channel_validator(channel: int):
    if not 1 <= channel <= 2:
        raise ValueError('Channel No value must be into interval [1,2])')

def config_validator(config: int):
    if not 0 <= config <= 1:
        raise ValueError('Config No value must be into interval [0,1])')
