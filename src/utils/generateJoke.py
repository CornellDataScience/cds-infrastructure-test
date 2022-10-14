from collections import deque


class JokeGenerator:
  def __init__(self, name):
    self.name = name
    self.joke_list = deque()
    # Adding elements to a queue
    self.joke_list.append("What's 25*2?")
    self.joke_list.append("What is 'an imitation of a song or artist, with deliberate exaggeration for comic effect' - but plural?")
  
  def getJoke(self):
    return self.joke_list.popleft()

  def generateResponse(self, userAns):
    return userAns + " nuts in your mouth! :P"