def copy_photo(from,to):
    with open(from,'rb') as f1,
    open (to,'wb') as f2:
        for i in f1:
            f2.write(i)
    return none