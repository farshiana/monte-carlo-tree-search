def get_empty_copy(obj):
    # pylint: disable=attribute-defined-outside-init, too-few-public-methods
    class Empty(obj.__class__):
        def __init__(self):
            pass

    copy = Empty()
    copy.__class__ = obj.__class__
    return copy

# Not an Enum as peformance is slow
PLAYER_ONE = 1
PLAYER_TWO = -1
