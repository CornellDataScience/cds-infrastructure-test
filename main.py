from src.utils.generateJoke import JokeGenerator

#print("Hahah I have torch")

j = JokeGenerator("Emily")

while(j.joke_list) :
  print(j.getJoke())
  userAns = input()
  # output
  print(j.generateResponse(userAns))