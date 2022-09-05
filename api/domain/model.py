class Service:
    def __init__(
        self,
        id: str,
        name: str,
        provider: str,
        type: str,
        description: str,
        url: str,
        extra: dict,
    ):
        self.id = id
        self.name = name
        self.provider = provider
        self.type = type
        self.description = description
        self.url = url
        self.extra = extra
