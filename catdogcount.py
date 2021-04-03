def cat_dog(str):
    cat_substring = "cat"
    dog_substring1 = "dog"

    count_cat = str.count(cat_substring)
    count_dog = str.count(dog_substring1)

    if count_cat == count_dog:
        return True
    else:
        return False

print(cat_dog('catdog'))