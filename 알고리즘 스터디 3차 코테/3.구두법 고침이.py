def solution(document):
    doc = document
    while "??" in doc or "!!" in doc\
        or "!?" in doc or "?!" in doc:
        doc = doc.replace("??", "?")
        doc = doc.replace("!!", "!")
        doc = doc.replace("!?", "?")
        doc = doc.replace("?!", "?")

    return doc

print(solution("a??a ?!a a!?b b!?!C C?!!D D?!?EE ??? FF!!! !???!"))