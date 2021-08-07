class Config(dict):
    """Dictionary but without possibility to add new keys."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__dict__ = self

    def __setattr__(self, key, value):
        if key not in [*self.keys(), "__dict__"]:
            raise KeyError("No new keys allowed")
        else:
            super().__setattr__(key, value)

    def __setitem__(self, key, value):
        if key not in self:
            raise KeyError("No new keys allowed")
        else:
            super().__setitem__(key, value)
