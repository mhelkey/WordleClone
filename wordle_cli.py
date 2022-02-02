import enchant

def verifyWord(string: str) -> bool:
  d = enchant.Dict("en_US")
  return d.check(string) and len(string) == 5 and string.isalpha()

def getPositionsArray(usr: str, ans: str): # O(2n) time
  # add all char in ans to alphabet arr
  arr = [0] * 26
  pos = [0] * 5
  for i in range(0,5): # hash all the letters in the ans
    arr[ord(ans[i]) - 97] += 1
  for i in range(0,5): # check for correct position
    if(usr[i] == ans[i]):
      pos[i] = 2
      arr[ord(usr[i]) - 97] -= 1
  for i in range(0,5): # check for correct letters, incorrect position
    if(arr[ord(usr[i]) - 97] > 0 and pos[i] == 0):
      arr[ord(usr[i]) - 97] -= 1
      pos[i] = 1
  return pos

def victoryCondition(pos):
  for i in range(0,5):
    if pos[i] != 2:
      return False
  return True

def positionToString(pos):
  string = ""
  for i in range(0,5):
    string += str(pos[i])
  return string

def run(ans: str):
  num = 0
  pos = [0] * 5
  while(num < 6 and not victoryCondition(pos) ):
    guess = input("\nEnter a 5 letter word as your attempt #" + str(num) + "\n")
    if not(verifyWord(guess)):
      print("Invalid word. Words must be 5 letter, real words, with no numbers")
      continue
    pos = getPositionsArray(guess, ans)
    print(positionToString(pos))
    num += 1
    

def main():
  run("bears")

if __name__ == "__main__":
    main()


