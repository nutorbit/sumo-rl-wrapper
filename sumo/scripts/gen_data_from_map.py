import subprocess


def main():
    subprocess.call([
        "python", "sumo/sumo_utils/tools/osmWebWizard.py",
        "-o", "test"
    ])


if __name__ == "__main__":
    main()
    