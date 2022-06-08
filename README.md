***La sélection du Chef***
# Tables à la carte


## tabl
Python implementations of integer sequences dubbed tabl in the OEIS.

## src
```python
def isTablGenerator(
    T: Callable[[int, int | None], int | list[int] | list[list[int]]]
    ) -> bool:
    return (
        isinstance(T, Callable)
        and isinstance(T(0), list)
        and isinstance(T(0, None), list)
        and isinstance(T(0, 0), int)
        and isinstance(T(0)[0], int)
        and isinstance(T(-1)[0], list)
        and isinstance(T(-1)[0][0], int)
    )
```

## docs
For the [user](https://luschny.de/math/seq/oeis/PythonIntegerTriangles.html), 
for the [implementer](https://github.com/PeterLuschny/tabl/blob/main/docs/ImplementationNotes.md).

## install
python -m pip install "tabl @ git+https://github.com/PeterLuschny/tabl.git"
