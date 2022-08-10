import json

def read_json(src):
  f = open(src, "r", encoding="utf-8")
  lines = json.load(f)
  return lines

def read_train(src):
  lines = read_json(src)
  for i, line in enumerate(lines):
    question = line["question"]
    if question.find("_") != -1:
      print(question)

if __name__ == "__main__":
  src = "scripts/reclor_data/train.json"
  read_train(src)
  # print(res)