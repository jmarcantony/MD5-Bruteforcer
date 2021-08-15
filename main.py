import hashlib
import time
import sys
import os

def print_error(code=0, path=None):
    cmd = "python" if os.name == "nt" else "python3"
    filename = sys.argv[0]
    if code == 0:
        print(f"[-] Invalid Arguments. Try {cmd} {filename} --help")
    else:
        print(f"[-] Invalid Wordlist Path '{path}'")
    quit(-1)

def print_help():
    cmd = "python" if os.name == "nt" else "python3"
    filename = sys.argv[0]
    docs = f"""
Optional Flags:
    -v: Bruteforces using verbose mode

Base Usage: {cmd} {filename} -h [MD5 Hash] -w [Wordlist Path] [Optional Flags]
    """
    print(docs)
    quit(-1)

def bruteforce(hash, path, verbose):
    with open(path) as f:
        wordlist = f.readlines()
        not_found = True
        start = time.time()
        for word in wordlist:
            word_hash = hashlib.md5(word.strip().encode()).hexdigest()
            if word_hash == hash:
                print(f"[+] Word Found: {word.strip()}")
                not_found = False
                break
            elif verbose:
                print(f"[-] Incorrect Word: {word.strip()}")
        end = time.time()
        if not_found:
            print("[-] Word was not in the wordlist")
        print(f"[*] Bruteforce finished in {round(end - start, 2)}s")

def main():
    if len(sys.argv) > 4 and "-h" in sys.argv and "-w" in sys.argv:
        HASH = sys.argv[sys.argv.index("-h") + 1]
        WORDLIST_PATH = sys.argv[sys.argv.index("-w") + 1]
        if not os.path.isfile(WORDLIST_PATH):
            print_error(1, WORDLIST_PATH) 
        bruteforce(HASH, WORDLIST_PATH, "-v" in sys.argv)
    else:
        if "--help" in sys.argv:
            print_help()
        print_error()

if __name__ == "__main__":
    main()
