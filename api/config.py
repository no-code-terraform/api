from api.domain import config as domain_config


def service_extra_item_schema():
    return {
        'type': 'object',
        'properties': {
            'name': {
                'type': 'string',
            },
            'type': {
                'type': 'string',
                'choices': domain_config.SERVICE_EXTRA_TYPES,
            },
            'min': {
                'type': 'interger',
                'required': False,
                'default': None,
            },
            'max': {
                'type': 'interger',
                'required': False,
                'default': None,
            },
            'choices': {
                'type': 'list',
                'items': {
                    'type': 'string',
                },
                'default': None,
                'required': False,
            },
            'is_multiple_choice': {
                'type': 'boolean',
                'default': False,
                'required': False,
            },
            'is_required': {
                'type': 'boolean',
                'default': False,
                'required': False,
            },
            'default': {
                'type': 'string',
                'required': False,
            },
        }
    }
