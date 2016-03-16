import random, time

class TheGame:
  """Guess the number"""
  __i = 0;

  def __init__(self, UB):
    self.__i = random.randint(1, UB)

  def guess(self, i):
    print "Guess:", i, "...",
    time.sleep(0.5)

    if self.__i < i:
      print "too big"
      return -1
    elif self.__i > i:
      print "too small"
      return 1
    else:
      print "you won!"
      return 0