import json


def print_sites():
    f = open('minerals/world.json', 'r')
    data = json.load(f)
    f.close()

    for site in data:
        if site["country"] == "United Kingdom":
            print(site["site_name"], ": " + site["commod1"] + ", " + site["commod2"])

def print_minerals():
    with open('minerals/minerals.json', 'r') as f:
        data = json.load(f)

    for m in data:
        if float(m["Mohs Hardness"]) >= 7.5:
            print(m["Name"], ": \t" + m["Mohs Hardness"])


# Script begins here
if __name__ == '__main__':
    print_minerals()
    print_sites()
