import enchant

def spellCheck(string: str) -> bool:
  d = enchant.Dict("en_US")
  return d.check(string)

def lengthCheck(string: str) -> bool:
  return len(string) == 5

