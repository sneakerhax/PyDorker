from googlesearch import search
import time
import sys

usage = "Usage: PyDorker.py <site.com> <dorklist>"


def banner():
    print("    ____        ____             __")
    print("   / __ \__  __/ __ \____  _____/ /_____  _____")
    print("  / /_/ / / / / / / / __ \/ ___/ //_/ _ \/ ___/")
    print(" / ____/ /_/ / /_/ / /_/ / /  / ,< /  __/ /")
    print("/_/    \__, /_____/\____/_/  /_/|_|\___/_/")
    print("      /____/")


def run_dorker(site, dorklist):
    with open(dorklist) as dorklist:
        for line in dorklist:
            try:
                dork = str(site) + " " + str(line)
                print("[Running Google Dork] - " + str(dork))
                for url in search(dork, num=10, stop=1):
                    print("[+] " + str(url))
                    print("\n")
            except:
                print("[-] error searching or no results \n")


def main():
    if len(sys.argv) == 3:
        site = "site:" + sys.argv[1]
        dorklist = "dorkfiles/" + sys.argv[2] + ".txt"
        banner()
        run_dorker(site, dorklist)
    else:
        print(usage)

if __name__ == "__main__":
    main()
