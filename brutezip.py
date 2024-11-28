import argparse
import os
import zipfile

def main():
    passwords, zipfile_path = load_words()
    bruteforce_zip(zipfile_path, passwords)

def load_words():
    parser = argparse.ArgumentParser(description='Bruteforce ZIP script.')
    parser.add_argument('-w', '--wfile', required=True, help='Path to the wordlist file')
    parser.add_argument('-z', '--zfile', required=True, help='Path to the zip file')

    args = parser.parse_args()
    wordlist = args.wfile
    zipfile_path = args.zfile  

    print(f"Wordlist file: {os.path.basename(wordlist)}")
    print(f"Zip file: {os.path.basename(zipfile_path)}")


    with open(wordlist, 'r') as file:
        passwords = [word.strip() for line in file for word in line.split()]

    return passwords, zipfile_path

def bruteforce_zip(zipfile_path, passwords):
    found = False
    try:
        with zipfile.ZipFile(zipfile_path, 'r') as zip_file:
            for password in passwords:
                try:
                    zip_file.extractall(pwd=password.encode('utf-8'))
                    print(f"Password found: {password}")
                    found = True
                    break
                except:
                    pass
    except FileNotFoundError:
        print(f"ZIP file not found: {zipfile_path}")
    except zipfile.BadZipFile:
        print(f"Invalid ZIP file: {zipfile_path}")

if __name__ == "__main__":
    main()
