from .domain import model

def service(
    data: dict
) -> None:
    kwargs = {}

    for k in [
        'provider',
        'type',
        'name',
        'description',
        'url',
        'tf_key',
        'extra'
    ]:
        kwargs[k] = data[k]

    return model.Service(**kwargs)
