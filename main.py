# the frequency of occurrence of letters
original = {
    'а': 0.072,
    'б': 0.017,
    'в': 0.052,
    'г': 0.016,
    'д': 0.035,
    'е': 0.017,
    'є': 0.008,
    'ж': 0.009,
    'з': 0.023,
    'и': 0.061,
    'і': 0.057,
    'ї': 0.006,
    'й': 0.008,
    'к': 0.035,
    'л': 0.036,
    'м': 0.031,
    'н': 0.065,
    'о': 0.094,
    'п': 0.029,
    'р': 0.047,
    'с': 0.041,
    'т': 0.055,
    'у': 0.04,
    'ф': 0.001,
    'х': 0.012,
    'ц': 0.006,
    'ч': 0.018,
    'ш': 0.012,
    'щ': 0.001,
    'ю': 0.004,
    'я': 0.029,
    'ь': 0.029,
    ' ': 0.17
}

new = {
    'а': 0,
    'б': 0,
    'в': 0,
    'г': 0,
    'д': 0,
    'е': 0,
    'є': 0,
    'ж': 0,
    'з': 0,
    'и': 0,
    'і': 0,
    'ї': 0,
    'й': 0,
    'к': 0,
    'л': 0,
    'м': 0,
    'н': 0,
    'о': 0,
    'п': 0,
    'р': 0,
    'с': 0,
    'т': 0,
    'у': 0,
    'ф': 0,
    'х': 0,
    'ц': 0,
    'ч': 0,
    'ш': 0,
    'щ': 0,
    'ю': 0,
    'я': 0,
    'ь': 0,
    ' ': 0
}


text = input('Введіть текст: ')
print(len(text))


# magic
i = 0
for characters in text:
    print(text[i])
    if text[i] == " ":
        print("-")
    elif text[i] == "е":
        new['е'] += 1
    else:
        print("+")
    i += 1

print(new['е'])

# len(text) * к-сть_цієї_букви_в_тексті / 100
