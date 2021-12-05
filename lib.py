

from const import SCREEN_WIDTH, SCREEN_HEIGHT


def coord_to_draw(row, col, total_cols, m):
    total_rows = len(m.sounds)
    if total_cols is None:
        total_cols = len(m.sounds[row])
    rowpercent = row/total_rows
    colpercent = col/total_cols
    return (SCREEN_WIDTH*colpercent, SCREEN_HEIGHT*rowpercent)


def coord_subtract(lhs, rhs):
    return (lhs[0]-rhs[0], lhs[1]-rhs[1])


def rect_to_draw(row, col, w, h, m):
    left_coord = coord_to_draw(row, col, len(m.sounds[row]), m)
    right_coord = coord_to_draw(row+h, col+w, len(m.sounds[row]), m)
    size_coord = coord_subtract(right_coord, left_coord)
    return (left_coord, size_coord)
