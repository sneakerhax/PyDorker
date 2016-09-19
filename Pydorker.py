from google import search
import time
import urllib2
import sys

usage = "Usage: Pydorker.py <site.com> <dorklist>"

def banner():
    print "#########################"
    print "#       Pydorker        #"
    print "#     By: sneakerhax    #"
    print "#########################"
    print ""

def run_dorker(site, dorklist):
    with open(dorklist) as dorklist:
        for line in dorklist:
            try:
                dork = str(site) + " " + str(line)
                print "[Running Google Dork] - " + str(dork)
                for url in search(dork, num=10, stop=1):
                    print "[+] " + str(url)
                print "\n"
            except urllib2.HTTPError, e:
                print "[+] " + str(e)

def main():
    if len(sys.argv) == 3:
        site = "site:" + sys.argv[1]
        dorklist = "dorkfiles/" + sys.argv[2] + ".txt"
        banner()
        run_dorker(site, dorklist)
    else:
		print usage

if __name__ == "__main__":
    main()
