while True:
    try:
        linha_new = ""
        linha = input()

        maiuscula = True

        for l in linha:
            if l == ' ':
                linha_new += ' '
                continue
            if maiuscula:
                linha_new += l.upper()
                maiuscula = False
            else:
                linha_new += l.lower()
                maiuscula = True
        print(linha_new)
    except EOFError:
        break
