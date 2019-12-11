# Dzień 4

Otwórz plik `log.csv` i przyjrzyj mu się uważnie.

Odczytaj zawartość pliku do słownika

Twój słownik po odczytaniu pliku będzie zawierał strukturę:

```python
some_logs = {
    20: 'ERROR',
    33: 'WARNING',
    59: 'WARNING4',
    74: 'ERROR',
    99: 'ERROR',
    81: 'WARNING',
    62: 'INFO',
    84: 'ERROR',
    36: 'WARNING',
    46: 'WARNING2',
    85: 'ERROR',
    64: 'INFO',
    71: 'ERROR1',
    7: 'ERROR',
    37: 'INFO4',
    90: 'INFO',
    13: 'INFO',
    93: 'INFO',
    68: 'ERROR',
    47: 'WARNING'
}
```

O pliku:
> The first value is the timestamp, while the second value is the type of log that was registered in the system at a given time.

Napisz funkcję, która wyświetla wszystkie **rodzaje** zdarzeń / logów, które pojawiły się w danym przedziale czasowym /liczbowym.

Na potrzeby zadania timestampy zostały zamienione na zwykłe liczby całkowite.

```python
def get_logs(start_interv, end_interv, logs_dict):
    pass
```

Rozwiązanie z wytłumaczeniem: http://getitjob.pl/2019/07/04/akcja-rekrutacja-python-2/

Rozwiązanie w pliku