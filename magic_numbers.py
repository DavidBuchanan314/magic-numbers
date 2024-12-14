import sys
from typing import Union

_orig_module = sys.modules[__name__]

# https://stackoverflow.com/a/493788/4454877
def _text2int(textnum: str, numwords={}) -> int | None:
	if not numwords:
		units = [
			"zero", "one", "two", "three", "four", "five", "six", "seven",
			"eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
			"fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
		]
		tens = [
			"", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
			"eighty", "ninety",
		]
		scales = [
			"hundred", "thousand", "million", "billion", "trillion", "quadrillion",
			"quintillion", "sextillion", "septillion", "octillion", "nonillion",
			"decillion", "undecillion", "duodecillion", "tredecillion",
			"quattuordecillion", "quindecillion", "sexdecillion", "septemdecillion",
			"octodecillion", "novemdecillion", "vigintillion", "unvigintillion",
			"duovigintillion", "tresvigintillion", "quattuorvigintillion", "quinvigintillion",
			"sesvigintillion", "septemvigintillion", "octovigintillion", "novemvigintillion",
			"trigintillion", "untrigintillion", "duotrigintillion", "trestrigintillion",
			"quattuortrigintillion", "quintrigintillion", "sestrigintillion", "septentrigintillion",
			"octotrigintillion", "noventrigintillion", "quadragintillion", "unquadragintillion",
			"duoquadragintillion", "tresquadragintillion", "quattuorquadragintillion", "quinquadragintillion",
			"sesquadragintillion", "septenquadragintillion", "octoquadragintillion", "novenquadragintillion",
			"quinquagintillion", "unquinquagintillion", "duoquinquagintillion", "trequinquagintillion",
			"quattuorquinquagintillion", "quinquinquagintillion", "sesquinquagintillion", "septenquinquagintillion",
			"octoquinquagintillion", "novenquinquagintillion", "sexagintillion", "unsexagintillion", "duosexagintillion",
			"tresexagintillion", "quattuorsexagintillion", "quinsexagintillion", "sesexagintillion", "septensexagintillion",
			"octosexagintillion", "novensexagintillion", "septuagintillion", "unseptuagintillion", "duoseptuagintillion",
			"treseptuagintillion", "quattuorseptuagintillion", "quinseptuagintillion", "seseptuagintillion",
			"septenseptuagintillion", "octoseptuagintillion", "novenseptuagintillion", "octogintillion", "unoctogintillion",
			"duooctogintillion", "tresoctogintillion", "quattuoroctogintillion", "quinoctogintillion", "sexoctogintillion",
			"septemoctogintillion", "octooctogintillion", "novemoctogintillion", "nonagintillion", "unnonagintillion", 
			"duononagintillion", "trenonagintillion", "quattuornonagintillion", "quinnonagintillion", "senonagintillion", 
			"septenonagintillion", "octononagintillion", "novenonagintillion", "centillion", # PRs welcome (seriously)
		]
		numwords["and"] = (1, 0)
		for idx, word in enumerate(units):  numwords[word] = (1, idx)
		for idx, word in enumerate(tens):   numwords[word] = (1, idx * 10)
		for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)

	current = result = 0
	for word in textnum.split():
		if word not in numwords:
			return None
		scale, increment = numwords[word]
		current = current * scale + increment
		if scale > 100:
			result += current
			current = 0

	return result + current

def _parse_float_name(name: str) -> Union[float, None]:
	parts = name.split('_POINT_')
	if len(parts) != 2:
		return None

	# Parse integer part
	int_part = _text2int(parts[0].lower().replace('_', ' '))
	if int_part is None:
		return None

	# Parse the decimal part
	decimal_parts = parts[1].split('_')
	decimal_str = ''

	for part in decimal_parts:
		val = _text2int(part.lower())
		if val is None or val > 9: # Each part must be a single digit
			return None
		decimal_str += str(val)

	# Combine the parts
	return float(f"{int_part}.{decimal_str}")

def __getattr__(name: str) -> Union[int, float]:
	# First try to parse as float (if it contains _POINT_)
	if '_POINT_' in name:
		val = _parse_float_name(name)
		if val is not None:
			return val
	# fall back to integer parsing
	val = _text2int(name.lower().replace('_', ' '))
	if val is None: # should raise an appropriate AttributeError
		return object.__getattribute__(_orig_module, name)
	return val
