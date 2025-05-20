import json

def load_config():
    url = input("?url: ")
    cookie = input("?cookie: ")
    delay = input("?delay: ")
    visualize = input("?visualize (y): ")
    if visualize.lower() == "y":
        visualize = "true"
    else:
        visualize = "false"

    config = {
        "URL": url,
        "COOKIE": cookie,
        "DELAY_MIN": delay,
        "VISUALIZE": visualize
    }

    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)

