import hashlib
from time import sleep
import re


class SpamFilter():
    def __init__(self):
        self.fileNames = ["ups.txt", "staples.txt", "glassdoor.txt",
                          "spamexample.txt", "job.txt",  "apt.txt", "test.txt", "indeed.txt", "affirm.txt", "google.txt", "bestbuy.txt",  "lucid.txt", "instacart.txt", "intern.txt", "intern2.txt", "zillow.txt", "ups2.txt", "paypal.txt", "honey.txt", "tabajo.txt"]
        self.hashes = []
        self.links = ["http://links4.upsemail.com",
                      "https://www.google.com/url?q=https://delighted.com/e/en-x-insta-cart/c/juInXzZ6hPRL34oM9tRwgmTI/0/00vXlNt7&amp;source=gmail&amp;ust=1668893715674000&amp;usg=AOvVaw2OHXQcgLnWtNinkbpk8ssl", "paypal.com", "https://links.joinhoney.com/u/click?_t=70657193eb7a404887947be80fb10777", "affirm.com"]

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
            f = open(f"emails/{i}", "r")
            txt = self.createEmailBody(f)
            finalBody = txt[0]
            entireBody = txt[1]
            if self.checkAgainstLinks(entireBody):
                print(f"{i} contains a blacklisted link, and is spam")
            else:
                if self.checkAgainstHashes(finalBody):
                    print(f"{i}This email was found in the spam hash list")
                    sleep(.25)
                else:
                    if self.checkForUnsubscribe(entireBody):
                        print(f"{i} is not spam")
                        sleep(.25)
                    else:
                        print(f"{i} has no unsubscribe link, adding to hashlist")
                        sleep(.25)
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

    def checkAgainstLinks(self, txt):
        for i in self.links:
            if i in txt:
                return True

        return False
