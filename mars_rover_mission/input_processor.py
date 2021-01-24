class InputProcessor:
    def __init__(self):
        pass

    def is_valid_heading(self, heading):
        return heading in ['N', 'E', 'S', 'W']
