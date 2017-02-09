# Instructions in how to complete this assigments are in the follwiing link
# http://docs.python-requests.org/en/master/user/quickstart/
# I got this link from "Taic"  thanks Taic



            # Practice and explanations before Homework.

    # importing request method
import requests
    #  saving the request Object in a variable so we can get information
r = requests.get('https://api.github.com/events')

    #  extracting and printing one portion of the information.
print(r.url)    # https://api.github.com/events
print("")

    # Raw response Content.
print(r.raw)    # <requests.packages.urllib3.response.HTTPResponse object at 0x7f075b027290>
print("")

    # HTML text from website.
print(r.text)    # THis will provide the HTML text of the requested website
print("")

    # Json decoder for data.
print(r.json()) # this will give the whole object in Json
print("")
print("")



# ------------------------------
#   Now lest do the Homework
# ------------------------------
print("Homework")
print("")

w = requests.get("https://www.google.com/")
print(w)
print("")

# print(w.text)
print("")


# ------------------------------
#   Extra Credit
# ------------------------------

url = "https://lambdaschool.com/contact"
files = {"Edxael contacting lambdaschool"}
w = requests.post(url, files=files)
w.text
