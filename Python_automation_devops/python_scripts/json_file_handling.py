import json

def test_json_file():
    # Writing to a JSON file
    data = {"name1": "Alice", "age1": 25, "city1": "New York"}
    with open("file/data.json", "w") as file:
        json.dump(data, file)

def test_json_read():
    # Reading from a JSON file
    with open("file/data.json", "r") as file:
        data = json.load(file)
        print(data)
