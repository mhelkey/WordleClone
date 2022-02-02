from english_words import english_words_lower_alpha_set
import numpy

def main():
  five_letter = set()
  for i in english_words_lower_alpha_set:
    if(len(i) == 5 and i.isalpha()):
      five_letter.add(i)
  five_letter = numpy.asarray(list(five_letter))
  print((five_letter))
  numpy.savetxt('answer.csv', five_letter, delimiter=',', fmt='%s')
  

if __name__ == '__main__':
  main()
