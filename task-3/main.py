import sys
from pathlib import Path
from colorama import Fore, Style, Back, init

def list_dir(path: Path, prefix=""):
    for item in path.iterdir():
        if item.is_file():
            print(f"{prefix}{Fore.GREEN}{item.name}")
        elif item.is_dir():
            print(f"{prefix}{Fore.BLUE}{item.name}/"); list_dir(item, prefix + "    ")

def main():
    init(autoreset=True)
    if len(sys.argv) > 1:
        folder = Path(sys.argv[1])
        if not folder.exists():
            print(f"{Fore.RED}Шлях не існує чи не є папкою!{Style.RESET_ALL}")
        else:
            print(f"{Fore.BLUE}{folder.resolve().name}/")
            list_dir(folder)
    else:
        print("Використання: 'python3 main.py /шлях/до/папки'")
        quit()

if __name__ == "__main__":
    main()
