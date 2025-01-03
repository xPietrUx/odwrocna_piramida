import random
import subprocess
import time
import urllib.parse
import webbrowser
from find_anagram.find_anagram import find_anagram
from read.read import read_file
import re

file_path_in = "in/slownik.txt"
file_path_out = "out/host.py"


# Funkcja wykonująca podczas działania serweru
def search_anagram():
    # Czytanie slownik.txt z folderu in
    file_content: list = read_file(file_path_in)

    print(
        "Szukanie anagramu dla każdego o jeden mniejszy od podanego słowa aż do pozycji: jedna litera"
    )

    word = input("Podaj słowo: ")
    pattern = re.compile(r"^\w+$", re.UNICODE)
    while not word.strip() or not pattern.match(word):
        print(
            "Słowo nie może być puste i musi zawierać tylko litery. Spróbuj ponownie."
        )
        word = input("Podaj słowo: ")

    print("Chwila...\n")

    # Szukanie możliwych anagramów z slownik.txt pasująca dla danego słowa-1
    anagram_list = find_anagram(word, file_content)

    report_list = []

    if anagram_list == []:
        print(
            "Dla danego słowa nie występuje możliwość stworzenia odwróconej piramidy dla"
        )
        report_list.append(f"Niemożność stworzenia piramidy dla - {word}")
    else:
        print("Dla danego słowa można utworzyć piramidę")
        print("Tworzenie piramidy...\n")

        # Tworzenie piramidy
        print(word.upper())
        report_list.append(word.upper())
        while True:
            anagram_list = find_anagram(word, file_content)
            if not anagram_list:
                break
            random_tuple = random.choice(anagram_list)
            index = random_tuple[0]
            word = file_content[index].strip()
            report_list.append(word.upper())
            print(word.upper())

    # Przesyłanie danych do serwera
    data = ",".join(report_list)
    url = f"http://localhost:8080/results?data={urllib.parse.quote(data)}"
    webbrowser.open(url)


# Uruchomienie serwera rapotującego
print("Uruchamianie serwera...")
server_process = subprocess.Popen(["python", file_path_out])
time.sleep(2)
print("Serwer uruchomiony. Wykonywanie dalszych operacji...")

try:
    while True:
        search_anagram()
        print("Raport http utworzono pomyślnie")
        repeat = (
            input("Czy chcesz powtórzyć szukanie anagramu? (tak/nie): ").strip().lower()
        )
        if repeat != "tak":
            break
except KeyboardInterrupt:
    pass
finally:
    print("Zatrzymywanie serwera...")
    server_process.terminate()
