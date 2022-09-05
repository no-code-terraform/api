from .domain import model

def service(
    data: dict
) -> None:
    kwargs = {}

    for k in [
        'id',
        'provider',
        'type',
        'name',
        'description',
        'url',
        'extra'
    ]:
        kwargs[k] = data[k]

    return model.Service(**kwargs)
