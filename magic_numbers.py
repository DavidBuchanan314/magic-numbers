import sys

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
			"octodecillion", "novemdecillion", "vigintillion", # PRs welcome (seriously)
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

def __getattr__(name: str) -> int:
	val = _text2int(name.lower().replace("_", " "))
	if val is None: # should raise an appropriate AttributeError
		return object.__getattribute__(_orig_module, name)
	return val
