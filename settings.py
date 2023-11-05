# "X" is a tile
# "P" is player

level_map = [
    ' XXXXXXXXXXXXXXXXXXXXXXXXXX  ',
    '                             ',
    '                             ',
    ' XX    XXX            XX     ',
    ' XX P                        ',
    ' XXXX        XX          XXX ',
    ' XXXX       XX               ',
    ' XX    X  XXXX    XX  XX     ',
    '       X  XXXX    XX  XXX    ',
    '    XXXX  XXXXXX  XX  XXXX   ',
    'XXXXXXXX  XXXXXX  XX  XXXX   ']

tile_size = 64
screen_width = 1200
screen_height = len(level_map) * tile_size
