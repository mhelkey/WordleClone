from english_words import english_words_lower_alpha_set


def main():
  five_letter = set()
  for i in english_words_lower_alpha_set:
    if(len(i) == 5 and i.isalpha()):
      five_letter.add(i)
  five_letter = list(five_letter)
  print(five_letter)
  print(len(five_letter))

if __name__ == '__main__':
  main()
