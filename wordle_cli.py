import enchant

def verifyWord(string: str) -> bool:
  d = enchant.Dict("en_US")
  return d.check(string) and len(string) == 5

def compareWordLinearly(usr: str, ans: str): # O(2n) time
  # add all char in ans to alphabet arr
  arr = [0] * 26
  pos = [0] * 5
  for i in range(0,5):
    arr[ord(ans[i]) - 97] += 1
  for i in range(0,5):
    if(usr[i] == ans[i]):
      pos[i] = 2
      arr[ord(usr[i]) - 97] -= 1
  for i in range(0,5):
    if(arr[ord(usr[i]) - 97] > 0):
      arr[ord(usr[i]) - 97] -= 1
      pos[i] = 1

  return pos
def main():
    answer = compareWordLinearly("evill", "fivel")
    print(answer)

if __name__ == "__main__":
    main()


