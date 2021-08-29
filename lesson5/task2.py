with open('file.txt', 'r') as fp:
    text = fp.readlines()
    print(text.__len__())
    for i in text:
        print(len(i.split()))