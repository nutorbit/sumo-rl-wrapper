import subprocess


def main():
    subprocess.call([
        "sumo-gui", "-c", "test/osm.sumocfg",
    ])


if __name__ == "__main__":
    main()
    