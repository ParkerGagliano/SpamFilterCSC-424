import hashlib


class SpamFilter():
    def __init__(self):
        self.fileNames = ["glassdoor.txt", "spamexample.txt", "test.txt"]
        self.hashes = []

    def createEmailBody(self, f):
        finalBody = ""
        entireBody = ''
        counter = 0
        emptyCounter = 0
        for i in f:
            entireBody += i
            if emptyCounter > 3:
                return finalBody
            if counter < 2:
                pass
            else:
                if i.strip():
                    finalBody += i
                    emptyCounter = 0
                else:
                    emptyCounter += 1
            counter += 1
        return [finalBody, entireBody]

    def checkForUnsubscribe(self, txt):
        substring = "Unsubscribe"
        final = str(txt)
        if final.find(substring) != -1 or final.find(substring.lower()) != -1 or final.find(substring.upper()) != -1:
            return True
        else:
            return False

    def presentationRun(self):
        for i in self.fileNames:
            f = open(i, "r")
            txt = self.createEmailBody(f)
            finalBody = txt[0]
            entireBody = txt[1]
            if self.checkAgainstHashes(finalBody):
                print("This email is spam and within hash list")
            else:
                if self.checkForUnsubscribe(entireBody):
                    print(f"File: {i} is not spam")
                else:
                    print("Unsubscribe not found in " + i)
                    result = hashlib.md5(finalBody.encode())
                    self.hashes.append(result.hexdigest())

    def customInput(self):
        fileName = input(
            "Enter the name of the file you want to check for spam: ")
        self.fileNames = [fileName, fileName2]

    def checkAgainstHashes(self, txt):
        result = hashlib.md5(txt.encode()).hexdigest()
        for i in self.hashes:
            if i == result:
                return True
        return False
