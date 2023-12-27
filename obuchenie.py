class Layer:
    def __init__(self, next_layer, name="Layer") -> None:
        self.next_layer = next_layer
        self.name = name


class Input:
    def __init__(self, inputs, name) -> None:
        self.inputs = inputs
        self.name = name
