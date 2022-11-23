# Spam filter documentation

This spam filter is using python and reading from emails I copied and pasted into txt files.

- The main running logic is in the following photo. It uses smaller methods within the SpamFilter class, this shows the protocol it follows to filter these emails
  ![](images/Screenshot%202022-11-23%20at%201.57.25%20PM.png) <br /><br />

- The first thing that happens is the email is put through the createEmailBody method which just converts the text file into a string, but also creates a finalBody string that cuts out the first 3 lines of the email as well as, if applicable, the ending of an email, which would be if theres more than 2 lines of blank space. This allows for a more reliable hash since it wont include the persons name or potential different footers. This is returned along with the entireBody variable, which is the entire email in string format, which is used to check for blacklisted links and an unsubscribe link.
  ![](images/Screenshot%202022-11-23%20at%201.59.35%20PM.png) <br /><br />
- After creating these 2 separate strings for the given file, it then checks for the presence of blacklisted links, that are specified beforehand. They are a mix of very specific links and general links, both work well with filtering.

```
                            The default ones are set as:
talent.com
https://www.google.com/url?q=https://delighted.com/e/en-x-insta-cart/c/juInXzZ6hPRL34oM9tRwgmTI/0/00vXlNt7&amp;source=gmail&amp;ust=1668893715674000&amp;usg=AOvVaw2OHXQcgLnWtNinkbpk8ssl
paypal.com
https://links.joinhoney.com/u/click?_t=70657193eb7a404887947be80fb10777
affirm.com
```

![](images/Screenshot%202022-11-23%20at%202.03.20%20PM.png)<br /><br />

- If it contains a link, the current email is passed, and the email is marked as spam, not adding it to the hashlist, since the first thing checked is links
- If the email does not contain a specified link, it will then check the emails hash against the hashlist.
- If the email is in the hashlist, it is marked as spam.
  ![](images/Screenshot%202022-11-23%20at%202.05.24%20PM.png)<br /><br />

- If the email is not in the hashlist, it then checks for an unsubscribe link
  ![](images/Screenshot%202022-11-23%20at%202.07.21%20PM.png)<br /><br />

- If it lacks an unsubscribe link, the finalBody version of the email is then hashed and the hash is stored into the hashes array.
  ![](images/Screenshot%202022-11-23%20at%202.41.03%20PM.png)<br /><br />

## Demonstrating it in action

- This is how it will be ran to demonstrate it, firstly the main logic from the top is ran once, filtering out and identifying spam, adding it to a hashlist if necessary, the exact same files will be ran through it again, but this time it would be faster since theres a hashlist that its being checked against first.
  ![](images/Screenshot%202022-11-23%20at%202.12.27%20PM.png)<br /><br />

* This is the result
  ![](images/Screenshot%202022-11-23%20at%202.39.40%20PM.png)<br /><br />
* As you can see, the first run of this added 11 hashes to the list as well as blocking 5 files due to blacklisted links, and allowing the rest.
* Noteably, Intern1.txt and Intern2.txt had a different beginning and the second one was detected in the hashlist inside the first run of the method, even though they were addressed to different people

```
                            INTERN1.TXT
Hello,

You have been shortlisted for a student internship which will give you the opportunity to earn
350.00 per week. Kindly Submit your full name in a text message to the number below for more information
Tel: (360) 203-7255


Dr Michele Parker

                            INTERN2 .TXT
Hello Parker Gagliano,

You have been shortlisted for a student internship which will give you the opportunity to earn
350.00 per week. Kindly Submit your full name in a text message to the number below for more information
Tel: (360) 203-7255


Dr Michele Parker
```

## Conclude + Summary

To conclude, this spam filter will first, check for blacklisted links, then check if the email is already in a hashlist, if these arent true, then it will check for an unsubscribe link, if that is true, its allowed through, if not it is added to the hashlist and marked as spam.
