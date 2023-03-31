from datetime import datetime

log_file = f"log-file-{datetime.now().strftime('%Y-%m-%d')}.log"


def log(text, log_file=log_file):
    with open(log_file, "a") as file:
        timestamp = datetime.now().strftime('[%Y-%m-%d %H:%M:%S] ')
        file.write(timestamp + text + "\n")


def dump(log_file=log_file):
    with open(log_file, "r") as file:
        contents = file.read()
        print(contents)
