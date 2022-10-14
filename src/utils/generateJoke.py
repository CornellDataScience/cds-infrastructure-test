from collections import deque


class JokeGenerator:
  def __init__(self, name):
    self.name = name
    self.joke_list = deque()
    # Adding elements to a queue
    self.joke_list.append("What's 25*2?")
  
  def getJoke(self):
    return self.joke_list.popleft()