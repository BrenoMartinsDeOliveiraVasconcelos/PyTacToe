def compare(l: list):
    equality = False
    index = -1
    for i in l:
        index += 1
        if index < len(l) - 1:
            if i == l[index + 1]:
                equality = True
            else:
                equality = False

    return equality
