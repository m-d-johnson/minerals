import json


def print_sites():
    minerals_file = open('world.json', 'r')
    data = json.load(minerals_file)
    minerals_file.close()

    for site in data:
        if site["country"] == "United Kingdom":
            print(site["site_name"], ": " + site["commod1"] + ", " + site["commod2"])

def print_minerals():
    with open('minerals.json', 'r') as f:
        data = json.load(f)

    for m in data:
        if float(m["Mohs Hardness"]) >= 7.5:
            print(m["Name"], ": \t" + m["Mohs Hardness"])


# Script begins here
if __name__ == '__main__':
    print_minerals()
    print_sites()
