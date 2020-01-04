

def directory(species_name):
    index = pydex['name'][species_name]['index']
    return index
#should index > index_string for clarity? index is NOT an int and is not supposed to be until ater
#pydex is not a global variable but should be

def national_dex(species_name):
    index = pydex['name'][species_name]['national_dex']
    return index

def hoenn_dex(species_name):
    national_dex = pydex['name'][species_name]['hoenn_dex']
    return hoenn_dex

def register_species(pydex, species_name, species_index):
    species_data = {'index':species_index, 'species_name':species_name}  #can also sort by dex later if I need
    pydex['name'] = {species_name: species_data}
    pydex['index'] = {species_index: species_data}
    assert pydex['index'][species_index] == species_data
    assert pydex['index'][species_index]['species_name'] == species_name
    assert pydex['name'][species_name]['species_index'] == species_index
    return pydex


def append_species_data(pydex, species_name, more_species_data):
    #pydex['index'][species_index]['national_dex'] = int
    #assert pydex['name'][species_name]['national_dex'] == int
    pass

def thebiglist_directory(thebiglist):   #expensive, only run once
    directory = {}   #should look over thebiglis and create something like {species, row}
    #stuff
    return directory


if __name__ == "__main__":
    pydex = {'name':{}, 'index':{}}  #init
    species_name = 'SPECIES_NONE'
    species_index = 0
    register_species(pydex, species_name, species_index)








