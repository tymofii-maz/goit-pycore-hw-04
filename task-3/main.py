import sys
from pathlib import Path
from colorama import Fore, Style, Back, init

def list_dir(path: Path, prefix: str = "") -> None:
    """Виводить вміст папки, а потім (рекурсивно) вміст кожної підпапки."""
    for item in path.iterdir():
        if item.is_file():
            print(f"{prefix}{Fore.GREEN}{item.name}")
        elif item.is_dir():
            print(f"{prefix}{Fore.BLUE}{item.name}/"); list_dir(item, prefix + "    ")

def main() -> None:
    init(autoreset=True)
    if len(sys.argv) < 2:
        folder = Path(sys.argv[1])
        if not folder.is_dir():
            print(f"{Fore.RED}Шлях не існує чи не є папкою!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.BLUE}{folder.resolve().name}/")
            list_dir(folder)
    else:
        print("Використання: 'python3 main.py /шлях/до/папки'")
        break

if __name__ == "__main__":
    main()
