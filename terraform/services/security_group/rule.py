class Rule:
    def __init__(self, from_port, to, protocol="tcp", block=["0.0.0.0/0"]):
        self.form = from_port
        self.to = to
        self.protocol = protocol
        self.block = block

    def get_rule(self):
        return {
            "from": self.form,
            "to": self.to,
            "protocol": self.protocol,
            "block": self.block
        }
