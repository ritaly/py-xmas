# coding=utf-8

def make_dict(seq):
    words_list = ' '.join(seq).lower().split()

    words_dict = {}
    for word in words_list:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1

    return words_dict

def get_most_common(words_dict):
    values = list(words_dict.values())
    values.sort(reverse = True)
    top3 = values[0:3]
    for word, count in words_dict.items():
        if count in top3:
            print(word, "-", count) 


def main():
    sentences = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
    ]

    dictionary = make_dict(sentences)
    get_most_common(dictionary)

if __name__ == '__main__':
    main()

