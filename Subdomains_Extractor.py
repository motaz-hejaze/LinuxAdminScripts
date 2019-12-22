import sys , json , os

from time import sleep

try:
  from os import scandir
except:
    print("Import Error")
    print("Required Modules Not Found!")
    exit()

if len(sys.argv) == 2:
    dirname = sys.argv[1]
    dir_path = os.path.abspath(dirname)

    try:
        with scandir(dir_path) as main_dir:
            print("Looping through main directory")
            sleep(1)
            print("...")
            sleep(1)
            print("..")
            sleep(1)
            print(".")
            for child_dir in main_dir:
                if child_dir.is_dir():
                    with scandir(child_dir) as folder:
                        for child_file in folder:
                            if child_file.is_file() and child_file.name == "hosts.json":
                                file_path = os.path.dirname(child_file)
                                dir = file_path.split("/")[-1]
                                print("----------------------------------")
                                print("Extracting host.json of : " + dir)
                                with open(child_file) as f:
                                    data = f.read()
                                    deserialized = json.loads(data)
                                    with open("Extracted_Subdomains.txt","a+") as fw:
                                        for key,value in deserialized.items():
                                            fw.write(key)
                                            fw.write("\n")
            print("----------------------------------")
            print("\n\n")
            print("Done Extracting all host.json files")
            sleep(1)
            print("===========================================================================")
            sleep(1)
            print("Please Check file Extracted_Subdomains.txt located in same script directory")
            sleep(1)
            print("===========================================================================")
            sleep(1)
            print("For Bugs / Improvements Please contact Author trapperx.1@gmail.com")
            print("Thanks for using Subdomains_Extractor!")

    except:
        print("Error in Directory Path or Name!")
        print("Make sure you typed the correct path of the main Directory")
        print("Example :")
        print("python3 Subdomains_Extractor.py /home/username/main_directory")
        print("Also Make Sure to use Python >= 3")


else:
    print("No Directory Name Provided")
    print("Make sure you typed the correct path of the main Directory")
    print("Example :")
    print("python3 Subdomains_Extractor.py /home/username/main_directory")
    print("Also Make Sure to use Python >= 3")
    exit()
