import enchant

def verifyWord(string: str) -> bool:
  d = enchant.Dict("en_US")
  return d.check(string) and len(string) == 5

def compareWord(user_string: str, ans_string: str):
  answer = [0] * 5 
  # 0 if char not in ans 
  # 1 if in ans, but not in correct pos
  # 2 if in ans and in correct pos
  for i in range(0,5):
    if user_string[i:i+1] in ans_string:
      answer[i] = 1
  return answer


def main():
    answer = compareWord("evift", "fivel")
    print(answer)

if __name__ == "__main__":
    main()


