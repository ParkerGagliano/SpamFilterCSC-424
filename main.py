from SpamFilter import SpamFilter

if __name__ == "__main__":
    spam = SpamFilter()
    spam.presentationRun()
    print('----------------------------\n')
    spam.presentationRun()
    print(len(spam.hashes), "hashes in list")
    print(len(spam.links), "links in list")
