import configparser

config = configparser.ConfigParser()

config["DATABASE"] = {
    "host": "localhost",
    "port": "3306"
}

with open("config.ini", "w") as file:
    config.write(file)

config.read("config.ini")

print("Host:", config["DATABASE"]["host"])
print("Port:", config["DATABASE"]["port"])