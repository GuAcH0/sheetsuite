import os, sys, glob

#from pycparser import parse_file, c_parser, c_generator

# pip install csv or #is this standard py3 module?
# pip install gspread, oauth2client  #depending on which they want to use
	#pip vs pip3?

dir_species_rel = 'include/constants/species.h'
dir_base_stats_rel = 'src/data/pokemon/base_stats.h'

def check_python_version():
    if sys.version_info[0] >= 3:
        pass
    else:
        print("\nThis script is currently only optimized for Python3.")
        print("Please check that you are using Python3 and not Python2 you silly willy!\n")
        quit()

def find_rom_directory():
    print("\nThis script is currently only optimized for pokeemerald.")
    print("Automatically testing if current directory is /pokeemerald...")
    test_dir = os.path.expanduser('./')
    if os.path.exists(test_dir + dir_species_rel):
        return test_dir
    print("Searching inside current directoy...")
    test_dir = os.path.expanduser('./pokeemerald/')
    if os.path.exists(test_dir + dir_species_rel):
        return test_dir
    print("Checking one directory up...")
    test_dir = os.path.expanduser('../')
    if os.path.exists(test_dir + dir_species_rel):
        return test_dir
    print("Checking neighboring directory...")
    test_dir = os.path.expanduser('../pokeemerald/')
    if os.path.exists(test_dir + dir_species_rel):
        return test_dir
    else:
        print("Rom not found in nearby locations.")
        print("Please provide the directory of your project as an argument.")  
        print("Example: 'python3 sheetsuite.py ../pokeemerald/")
        quit()

def confirm_rom_directory(rom_directory):
    dir_species = rom_directory + "/" + dir_species_rel
    if os.path.exists(dir_species):
        print("ROM directory " + str(rom_directory) + " confirmed.")
    else:
        print("ROM not found at " + str(rom_directory))
        print("or file " + str(dir_species) + " is missing. Please check and try again.")
        quit()
    
def warning():
    print("\nRemember to always make a backup of your project!")

def intro():
    print("\nHello! welcome to the world of... hacking scripts!")
    print("My name is the Sheet Suite. People also call me the Dex/BST Modifier.")
    print("This script will automatically search for a spreadsheet (at this time only single-sheet spreadsheets are supported..")

def init_spreadsheet():
    if len(glob.glob('*.json')) == 1:
        print("\nFile " + str(glob.glob('*.json')) + " found. No other .json files found in current directory.")
        glob_response = input("Would you like to use this file? (y/n): ").split(" ")    #assumes sheet1, needs to ask
        if True:                      #change to case structure of 'glob_response'
            #move this entire if statement to another function called' init_gspread
            spreadsheet_filename = str(glob.glob('*.json')
            spreadsheet_directory = glob.glob('*.json') 
            from gspreadreader import gspread_to_species_directory
            #spreadsheet = gspreadauthenticator()
            sheet_list_of_dictionaries = gspread_to_species_directory(spreadsheet_filename)
            return sheet_list_of_dictionaries
    else:
        print("no spreadsheet found")
    #check .ods .xlxs .csv
    #generate spreadsheet option


if __name__ == "__main__":
    warning()
    check_python_version()
    if len(sys.argv) > 1:
        rom_directory_relative = os.path.expanduser(sys.argv[1])
    else:
        rom_directory_relative = find_rom_directory()
        print("Decompiled ROM found at: " + str(rom_directory_relative))
    rom_directory = os.path.realpath(rom_directory_relative)
    confirm_rom_directory(rom_directory)
    intro()
    init_spreadsheet()










