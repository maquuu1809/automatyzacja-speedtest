# Automatyzacja Speedtest
W tym repozytorium znajduje się program, który automatyzuje proces pomiarów prędkości Internetu przy użyciu strony [speedtest.pl](https://www.speedtest.pl). Program korzysta z biblioteki Selenium, zapisuje wyniki do pliku `.csv` i może działać w trybie niewidocznym (headless).


## 🛠️ Wymagania

- Python w wersji **co najmniej 3.10** - można pobrać ze strony [python.org](https://www.python.org/downloads/release/python-3100/)
- Przeglądarka **Google Chrome**
- Zainstalowana biblioteka **Selenium**:

```bash
pip install selenium
```

## ⚙️ Argumenty wejściowe
| Argument | Typ     | Wartość defaultowa | Opis                                                       |
|----------|---------|--------------------|------------------------------------------------------------|
| name     | String  | "wyniki"           | Nazwa pliku .csv do którego zapisywane są wyniki pomiarów. |
| repeats  | int     | 10                 | Liczba wykonywanych pomiarów.                              |
| interval | int     | 60                 | Odstęp (w sekundach) między kolejnymi pomiarami.           |
| headless | Boolean | False              | Czy uruchamiać przeglądarkę w tle (bez widocznego okna).   |


## ▶️ Przykład użycia

     if __name__ == "__main__":
         measure_network_speed(name="log_sieci", repeats=5, interval=30, headless=True)


## 🚀 Uruchomienie
Program można uruchomić w terminalu komendą: 

```bash
python main.py
```

lub za pomocą środowiska IDE (np. PyCharm, VS Code).


## 📄 Format pliku wynikowego
Tworzony podczas działania programu plik `.csv` zawiera dane w następującym formacie:
| Data                | Opóźnienie [ms] | Pobieranie [Mb/s] | Wysyłanie [Mb/s] |
|---------------------|-----------------|-------------------|------------------|
| 2025-07-30 12:54:31 | 6               | 90.06             | 91.46            |
| 2025-07-30 12:56:02 | 6               | 90.31             | 90.08            |
| 2025-07-30 12:57:34 | 6               | 88.13             | 88.08            |
| 2025-07-30 12:59:07 | 7               | 89.68             | 90.14            |
