# Dzień 5

Otwórz plik `log.csv` i przyjrzyj mu się uważnie.

Odczytaj zawartość pliku do słownika

Twój słownik po odczytaniu pliku będzie zawierał strukturę:

```python
some_logs = {
    1564517408: 'ERROR',
    1562514432: 'WARNING',
    1564015907: 'WARNING4',
    1563822588: 'ERROR',
    1563125949: 'ERROR',
    1564225949: 'WARNING',
    1562491290: 'INFO',
    1563184020: 'ERROR',
    1562956120: 'WARNING',
    1564477808: 'WARNING2',
    1564421475: 'ERROR',
    1562764321: 'INFO',
    1562709301: 'ERROR1',
    1563900303: 'ERROR',
    1564125540: 'INFO4',
    1564010897: 'INFO',
    1564279899: 'INFO',
    1564456120: 'INFO',
    1564452850: 'ERROR',
    1564528675: 'WARNING'
}
```

O pliku:
> The first value is the timestamp, while the second value is the type of log that was registered in the system at a given time.

Napisz funkcję, która wyświetla wszystkie **rodzaje** zdarzeń / logów, które pojawiły się w danym przedziale czasowym.

**Rozszerzenie dnia 4**

Ponieważ są to timestampy - czyli punkty czasowe możemy założyć, że użytkownik będzie podawał zakres czasowy w bardziej ludzkim formacie, jakim to już wasza decyzja 😛 

Przy czym sama funkcja z wczoraj nie powinna się tak naprawdę zmienić 🙂 


**Gdy wyczerpią się inne środki:**

- Przykład "odpakowania" timestampu do formatu czasu: `hint01.py`
- Przykład "zapakowania" daty w timestamp: `hint02.py`

