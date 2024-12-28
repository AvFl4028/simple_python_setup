import sys
import os

args = sys.argv[1]
file_path = args + "/src/main.py"

def main():
    print("Creating project...")
    os.system(f'python -m venv "{args}\\venv"')
    os.mkdir(args + "/src")
    with open(file_path, "w") as f:
        f.write("""
def main():
    print("Hello, World!")
if __name__ == "__main__":
    main()
""")
        f.close()
    print("Project created successfully!")

if __name__ == "__main__":
    main()