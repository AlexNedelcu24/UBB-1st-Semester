def get_val(obj, key):
    if key == 'id':
        return obj.getID()
    if key == 'book_title':
        return obj.getTitle()
    if key == 'book_author':
        return obj.getAuthor()
    if key == 'client_name':
        return obj.getName()
    if key == 'client_CNP':
        return obj.getCNP()


def quickSort(list, key, cmp):
    if len(list) <= 1:
        return list
    pivot = list.pop()
    lesser = quickSort([x for x in list if cmp(x, pivot)], key=None, cmp=compare_book)
    greater = quickSort([x for x in list if not cmp(x, pivot)], key=None, cmp=compare_book)
    return lesser + [pivot] + greater

def gnomeSort(list, key, cmp):
    pos = 0
    while pos < len(list):
        if pos == 0 or not cmp(list[pos], list[pos-1]):
            pos = pos + 1
        else:
            list[pos], list[pos-1] = list[pos-1], list[pos]
            pos = pos - 1
    return list

def gnomeSort2(list, key):
    pos = 0
    while pos < len(list):
        if pos == 0 or get_val(list[pos], key) >= get_val(list[pos-1], key):
            pos = pos + 1
        else:
            list[pos], list[pos-1] = list[pos-1], list[pos]
            pos = pos - 1
    return list

def compare_book(book1, book2):
    if book1.getAuthor() < book2.getAuthor():
        return True
    if book1.getAuthor() == book2.getAuthor() and book1.getTitle() < book2.getTitle():
        return True
    return False

def compare_client(client1, client2):
    if client1.getName() < client2.getName():
        return True
    if client1.getName() == client2.getName() and client1.getCNP() < client2.getCNP():
        return True
    return False

