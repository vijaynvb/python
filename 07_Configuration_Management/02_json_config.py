import json

with open("01_config.json", "r") as file:
    config = json.load(file)

print("App Name:", config["app_name"])
print("Version:", config["version"])
print("Debug:", config["debug"])