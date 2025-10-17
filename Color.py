class Color:
    def __init__(self, hexcode):
        self.hexcode = hexcode

    @property
    def hexcode(self):
        return f"{self.r:02X}{self.g:02X}{self.b:02X}"

    @hexcode.setter
    def hexcode(self, value):
        hex_value = value.lstrip('#')
        if len(hex_value) != 6:
            raise ValueError('HEX-код длиннее 6 символов')
        self.r = int(hex_value[0:2], 16)
        self.g = int(hex_value[2:4], 16)
        self.b = int(hex_value[4:6], 16)


color = Color('#0000FF')
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)

color = Color('0000FF')
color.hexcode = 'F5D1A3'
print(color.hexcode)
print(color.r)
print(color.g)
print(color.b)
