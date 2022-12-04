
# #@

from _tabltypes import tabl, trow
from _tabltransforms import diag_tabl, cum_tabl, rev_tabl


def even_sum(r: trow) -> int:
    return sum(r[::2])


def odd_sum(r: trow) -> int:
    return sum(r[1::2])


def alt_sum(r: trow) -> int:
    return even_sum(r) - odd_sum(r)


def tabl_sum(t: tabl) -> trow:
    return [sum(row) for row in t]


def tabl_evensum(t: tabl) -> trow:
    return [even_sum(row) for row in t]


def tabl_oddsum(t: tabl) -> trow:
    return [odd_sum(row) for row in t]


def tabl_altsum(t: tabl) -> trow:
    return [alt_sum(row) for row in t]


def tabl_diagsum(t: tabl) -> trow:
    diagt: tabl = diag_tabl(t)
    return [sum(row) for row in diagt]


def tabl_cumsum(t: tabl) -> trow:
    cumt: tabl = cum_tabl(t)
    return [sum(row) for row in cumt]


def tabl_revcumsum(t: tabl) -> trow:
    revcumt: tabl = cum_tabl(rev_tabl(t))
    return [sum(row) for row in revcumt]
