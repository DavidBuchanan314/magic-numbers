# magic-numbers

Magically import magic number constants. Like so:

```py
from magic_numbers import FORTY_TWO, SIXTY_NINE, FOUR_HUNDRED_AND_TWENTY
from magic_numbers import ONE_THOUSAND_THREE_HUNDRED_AND_TWELVE
from magic_numbers import THREE_POINT_ONE_FOUR_ONE_FIVE_NINE_TWO as PI

print(f"{FORTY_TWO = }")  # 42
print(f"{SIXTY_NINE = }")  # 69
print(f"{FOUR_HUNDRED_AND_TWENTY = }")  # 420
print(f"{ONE_THOUSAND_THREE_HUNDRED_AND_TWELVE = }")  # 1312
print(f"{PI = }")  # 3.141592
```

Note: Floats can only be specified using "point", there is no support (yet) for fractions like `THREE_AND_A_HALF` or `TWO_THIRDS`

## Installation

```sh
python3 -m pip install magic-numbers
```
