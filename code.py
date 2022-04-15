def main():
  import json
  print("hello world!")
  print("this is an update!")
  print("this is another update!")
  dict = {"obj" : "apple"}
  open("output.json", "w").write(json.dumps(dict))
