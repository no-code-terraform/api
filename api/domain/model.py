class Service:
    def __init__(
        self,
        name: str,
        provider: str,
        type: str,
        description: str,
        url: str,
        tf_key: str,
        extra: list,
    ):
        self.name = name
        self.provider = provider
        self.type = type
        self.description = description
        self.url = url
        self.tf_key = tf_key
        self.extra = [
            {
                k: (v if v else None) for k, v in i.items()
            } for i in extra
        ]
