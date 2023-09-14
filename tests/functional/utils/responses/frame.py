from string import Template


class CreateVideoFrame:
    SUCCESS = Template('Successfully creating "$count" records')
    FORBIDDEN = "Authentication credentials were not provided."
    CAM_ID_ERROR = "Cam id value must be into interval (0, 100)"
    CHANNEL_ID_ERROR = "Channel No value must be into interval [1,2])"
    CONFIG_ID_ERROR = "Config No value must be into interval [0,1])"
    VIDEO_COLOR_ERROR = Template(
        "$number is greater than the maximum of 100\n\nFailed validating 'maximum' in schema['properties']['$key']:\n    {'maximum': 100, 'minimum': 0, 'type': 'number'}\n\nOn instance['$key']:\n    $number"
    )
