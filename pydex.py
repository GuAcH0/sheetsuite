import config
import sys
from itertools import combinations

class pydex:
    def __init__(self):
        self.identifier = {}
        self.index = {}
        self.name = {}

    class species:
        def __init__(self, identifier, index, name, natl=None):
            self.identifier = identifier
            self.index = index
            self.name = name
            self.natl = natl

    def register(self, species_identifier, species_constant, species_name):
        species_data = self.species(species_identifier, species_constant, species_name)
        self.identifier[species_identifier] = species_data  
        self.index[species_constant] = species_data  
        self.name[species_name] = species_data

    def check_sheets_consistency(self, row_matched_biglist, column_key):
        incorrect_rows = []
        for rowindex in range(len(row_matched_biglist)):
            row = row_matched_biglist[rowindex]
            expected_shared_value = list(row.values())[0][column_key]
            if all(biglist[column_key] == expected_shared_value for biglist in row.values()):
                pass
            else:
                incorrect_rows.append(rowindex)
        return incorrect_rows

    def fuse_biglists(self, thebigdict):
        print('Consolidating sheets...')
        number_of_rows = self.compare_biglist_lengths(thebigdict)
        row_matched_biglist = self.match_biggerdict_rows(thebigdict, number_of_rows)
        sheet_inconsistencies = {}
        species_column_key = config.species_name_column
        #species_inconsistent_rows = self.check_sheets_consistency(row_matched_biglist, species_column_key)
        #sheet_inconsistencies[species_column_key] = species_inconsistent_rows
        for duplicate_column_key in self.find_duplicate_columns(thebigdict):
            duplicate_inconsistent_rows = self.check_sheets_consistency(row_matched_biglist, duplicate_column_key)
            sheet_inconsistencies[duplicate_column_key] = duplicate_inconsistent_rows
        assert species_column_key in sheet_inconsistencies.keys()
        if len(sheet_inconsistencies) == 0:
            thebiggerlist = []
            for oldrow in row_matched_biglist:
                newrow = {}
                for sheet in oldrow:
                    newrow.update(oldrow[sheet])
                thebiggerlist.append(newrow)
            return thebiggerlist
        else:
            for column_key in sheet_inconsistencies.keys():
                print("Listing inconsistencies found between spreadsheets for column '" + str(column_key) + "'.")
                list_of_inconsistent_rows = sheet_inconsistencies[column_key]
                for rowindex in list_of_inconsistent_rows:
                    for sheet, rowdata in row_matched_biglist[rowindex].items():
                        potentially_incorrect_value = rowdata[column_key]
                        print("Compare sheet '" + str(sheet) + "', row " + str(rowindex) + ", '" + str(potentially_incorrect_value) + "'.")
            sys.exit("Not all spreadsheets are consistent. Fix the errors listed above.")

    def find_duplicate_columns(self, thebigdict):
        biglists = thebigdict.values()
        duplicate_columns = []
        for biglist1, biglist2 in combinations(biglists,2):
            biglist1row0 = biglist1[0]
            biglist2row0 = biglist2[0]
            shared_columns = set(biglist1row0).intersection(biglist2row0)
            for shared_column in shared_columns:
                duplicate_columns.append(shared_column)
        return duplicate_columns

    def match_biggerdict_rows(self, thebigdict, number_of_rows):
        row_matched_biglist = []
        for current_row in range(number_of_rows):
            matched_row = {}
            for sheet, biglist in thebigdict.items():
                matched_row[sheet] = biglist[current_row]
            row_matched_biglist.append(matched_row)
        return row_matched_biglist

    def compare_biglist_lengths(self, thebigdict):
        biglists = list(thebigdict.values())
        expected_number_of_rows = len(biglists[0])
        if all(len(biglist) == expected_number_of_rows for biglist in biglists):
            print('All sheets confirmed same length.')
            return expected_number_of_rows
        else:
            for sheet_name, biglist in thebigdict:
                print("Sheet '" + sheet_name + "' contains " + str(len(biglist)) + " rows.")
            sys.exit("Not all sheets in spreadsheet have the same number of rows! See above output. Quitting.")

    def register_thebigdict(self, thebigdict):
        thebiggerlist = self.fuse_biglists(thebigdict)
        for row in thebiggerlist:
            species_column_key = config.species_name_column
            species_name = row[species_column_key]
            species_identifier = "SPECIES_" + str(species_name)
            natdex_identifier = "NATIONAL_DEX_" + str(species_name)
            hoenndex_identifier = "HOENN_DEX_" + str(species_name)
            natdex_constant = row[config.natdex_column]
            species_constant = natdex_constant          #need to change later, not true if unown included
            hoenndex_constant = 69          #need to change later for obvious reasons
            self.register(species_identifier, species_constant, species_name)
            #this point in code should check if existing index/natdex, various reasons this could go wrong not sure
            self.index[species_constant].natdexid = natdex_identifier
            self.index[species_constant].natdex = natdex_constant
            self.index[species_constant].hoenndexid = hoenndex_identifier
            self.index[species_constant].hoenndex = hoenndex_constant

"""
merge this entire thing with new method in pydex
confused because seems like cyclic thing, pydex creates pydex inside iteself? (above method)

compare_biglist_lengths should be called from this function not the function inside other function
all functions should be called here
def thebigdict_to_pydex(thebiggerlist):
    import config
    newdex = pydex()
    for biglist in thebiggerlist:  #this is actually wrong; expects natdex column in first biglist/sheet but not true
        for row in biglist:
            species_column_key = config.species_name_column
            species_name = row[species_column_key]
            species_identifier = "SPECIES_" + str(species_name)
            natdex_identifier = "NATIONAL_DEX_" + str(species_name)
            hoenndex_identifier = "HOENN_DEX_" + str(species_name)
            natdex_constant = row[config.natdex_column]
            species_constant = natdex_constant          #need to change later, not true if unown included
            hoenndex_constant = 69          #need to change later for obvious reasons
            newdex.register(species_identifier, species_constant, species_name)
            #this point in code should check if existing index/natdex, various reasons this could go wrong not sure
            newdex.index[species_constant].natdexid = natdex_identifier
            newdex.index[species_constant].natdex = natdex_constant
            newdex.index[species_constant].hoenndexid = hoenndex_identifier
            newdex.index[species_constant].hoenndex = hoenndex_constant
    return newdex
"""


"""
Some notes on names of objects used:

row = {'name':... 'index':...} 
biglist1 = [rowA1,rowA2,rowA3...] from sheet1
biglist2 = [rowB1,rowB2,rowB3...] from sheet2
thebigdict = {sheet1:biglist1, sheet2:biglist2, ....}
rowmatchedbiglist = [{sheet1:biglist1[0], sheet2:biglist2[0]...}
                     {sheet1:biglist1[1], sheet2:biglist2[1]...}
                  ...{sheet1:biglist1[N], sheet2:biglist2[N]...}]
"""



#TODO    
#fix thebiggerlist_to_basic_pydex(thebiggerlist) 
#assert species_column_key in sheet_inconsistencies.keys()
#change this line to check that each sheet has this column, during the fuse


"""
TODO low priority -
- are there any good reasons why # rows would be different? in compare biglist lenghs?
- feature - have an 'ignore row' or 'ignore column' marker, ex
  #blastoise             stuff....
    #blastoise USE=TRUE  diff stuff...
- what does the checkbox in gspread turn into? a boolean or other symbol? potentiall useful
- pretty indent using textwrape
    https://stackoverflow.com/questions/18756510/printing-with-indentation-in-python
- returns list of inconsistencies, but only first 10 in case the whole thing is messed up and asks if you want to display all and check manually later
"""







if __name__ == "__main__":
    import glob
    spreadsheet_filename = glob.glob('*.json')[0]

    from cleanerupper import print_lines

    from gspreadreader import gspread_opener
    filename = glob.glob('*.json')[0]   #only one json file, one service account
    gsheet_name = 'Test Data'
    thebigdict = gspread_opener(filename, gsheet_name)
    dex = pydex()
    dex.register_thebigdict(thebigdict)

"""
    species_filename = './testfiles/species.h'
    lines = openfile(species_filename)
    header, index_lines, wrapper1, natdex_lines, wrapper2, hoenndex_lines, footer = species_wrapper_parser(lines)
    lines = write_species(header, wrapper1, wrapper2, footer, newdex)
    #print_lines(lines)  #works, need to write out
"""













