from SpamFilter import SpamFilter

if __name__ == "__main__":
    joe = SpamFilter()
    joe.presentationRun()
    print('----------------------------\n')
    joe.presentationRun()
    print(len(joe.hashes), "hashes in list")
    print(len(joe.links), "links in list")
