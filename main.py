from src.utils.generateJoke import JokeGenerator
from utils.jokeHints import AdvancedJokeGenerator

#print("Hahah I have torch")

j = JokeGenerator("Emily")
j2 = AdvancedJokeGenerator("Evelyn")

while(j.joke_list) :
  print(j.getJoke())
  userAns = input()
  # output
  print(j.generateResponse(userAns))

while(j2.joke_list) :
  print(j2.getJoke())
  userAns = input()
  # output
  print(j2.generateResponse(userAns))