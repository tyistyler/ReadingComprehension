import json

# 共17种问题类型名
def read_json(path="./reclor_data"):
  f = open(path, "r", encoding="utf-8")
  json_f = json.load(f)
  return json_f


if __name__ == "__main__":
  src = "./scripts/reclor_data/train.json"
  lines = read_json(src)
  label_set = set()
  for line in lines:
    context = line["context"]
    question = line["question"]
    answers = line["answers"]
    label = line["label"]
    id_string = line["id_string"]
    if label not in label_set:
      label_set.add(label)
  print(label_set)


  # for key, value in res.items():
  #   print(key)
  #   print(value)
  