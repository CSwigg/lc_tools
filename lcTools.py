import numpy as np
import matplotlib.pyplot as plt
import os
from astropy.table import Table, Column
import csv
import pandas as pd

'''
Light curve tools are meant to take in a csv output file from a CasJobs query
and assist with quick light curve plots.
'''

class lcTools:
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.table=[]
        self.file_name = self.file_path + input("Please enter the file name of the table you'd like to use (or type 'stop'): ")
        while (not os.path.exists(self.file_name)):
            if self.file_name == 'stop':
                print('\nWARNING: Table was not initialized.\n')
                return 
            else:
                file_name = input('No such table, try again: ')

        with open(self.file_name) as f: 
            self.header = next(csv.reader(f, delimiter=','))
            print(self.header)
            self.table = np.genfromtxt(f,delimiter=',',dtype='float',skip_header=1)
        
    def deg_to_arcsec(self):
        self.table[:,0:2]=self.table[:,0:2]*3600
    
    def group_things(self) -> np.ndarray:
        '''
        Groups detections by thingID or by astrometry variations (if .csv file is from 
        database < DR14)
        '''
        # For databases >= DR14
        try:
            df = pd.read_csv(self.file_name)
            gf = df.groupby('thingID')
            grouped = [gf.get_group(x) for x in gf.groups]
            l_grouped = []
            [l_grouped.append(x.values) for x in grouped]
            return l_grouped
        # Sorting for stripe82 and databases < DR14
        except KeyError:
            print('\nSorting by astrometry variations:\n')
            df = pd.read_csv(self.file_name)
            gf = df.groupby([np.round(df['ra'],3), np.round(df['dec'],3)])
            grouped = [gf.get_group(x) for x in gf.groups]
            l_grouped = []
            [l_grouped.append(x.values) for x in grouped]
            return l_grouped
    
    def group_things82(self) -> np.ndarray:
        '''
        Groups detections from a Stripe82 CasJobs file by grouping detections by accounting 
        for small variations in astrometry. 
        '''
        df = pd.read_csv(self.file_name)
        gf = df.groupby([np.round(df['ra'],3), np.round(df['dec'],3)])
        grouped = [gf.get_group(x) for x in gf.groups]
        l_grouped = []
        return [l_grouped.append(x.values) for x in grouped]


    # TODO: Fix formating so that columns are aligned: Use format strings, or pandas(?)
    @staticmethod
    def show_things(things):
        
        '''
        Run sort_things(table) first!!!
        '''
        
        print('Total things: ', len(things))
        count=0
        for i in things:
            count+=len(i)
        print('Total detections: ', count,'\n')
        for index, i in enumerate(things):
            print('THING ' + str(index))
            print('---------------------------------')
            for j in i:
                print('RA:'.rjust(10) + str(round(j[0],4)) + ' DEC:'.rjust(10) + str(round(j[1],4)) + ' MJD:'.rjust(10) + str(round(j[2],2)) + ' u:'.rjust(10) + str(round(j[3],2)) + ' g:'.rjust(10) + str(round(j[4],2)) + ' r:'.rjust(10) + str(round(j[5],2)) +' i:'.rjust(10) + str(round(j[6],2)) + ' z:'.rjust(10) + str(round(j[7],2)))
            print('\n')

   

def unpack_thing(thing):
    stacked_thing=np.stack(thing,axis=0)
    return stacked_thing

    # Sorts an array of dates and an array of magnitudes by the numerical order of the date array
def sort_by_date(date,mag,err_mag):
    date, mag, err_mag= zip(*sorted(zip(date,mag,err_mag)))
    return np.asarray(date), np.asarray(mag), np.asarray(err_mag)

    # Creates a dictionary of things 
def dict_things(things):
    d = {}
    d['thing' + str(i)] = [unpack_thing(thing) for i, thing in enumerate(things)]
    return d

def dict_data(thing, table):
    d = {}
    for i in range(len(thing[0])):
        d[table.header[i]] = thing[:,i]
    return d

def to_fits(thing, date_index:int, mag_index:int, err_mag_index:int, filter_name:str, name:str):
    '''
    Takes the date and photometry of one band of a source and writes it to a fits file
    '''
    thing = unpack_thing(thing)
    date = thing[:,date_index]
    mag = thing[:,mag_index]
    err_mag = thing[:,err_mag_index]

    t = Table()
    t['Date'] = Column(date)
    t[filter_name + '-band'] = Column(mag)
    t[filter_name + '-band Error'] = Column(err_mag)

    t.write('/Users/admin/Desktop/astro_research/' + name + '.fits')


def to_fits2(d:dict, name:str):
    '''
    Takes in a dictionary of data and outputs to fits file based on key names
    '''
    t = Table()
    t[key] = [Column(d[key]) for key, value in d.items()]
    t.write('/Users/admin/Desktop/astro_research/{}.fits'.format(name))






####### Unused functions ############

# sort for stripe82
# TERRIBLE FUNCTION ----> O(N^2)
# def sort_things(self):
#     things=[]
#     used_ra=[]
#     for x,y in zip(self.table[:,0],self.table[:,1]):
#         if np.any(np.isin(x,used_ra)):
#             continue   
#         else:  
#             thing=[] 
#             for i, (x2,y2) in enumerate(zip(self.table[:,0],self.table[:,1])):
#                 if np.any(np.isin(x2,used_ra)):
#                     continue
#                 # These parameters might need a bit of tweaking to sort correctly
#                 elif ((np.sqrt((x2 - x)**2 + (y2 - y)**2) < 1)):
#                     thing.append(self.table[i])
#                     used_ra.append(x2)   
#             things.append(thing)
#     return(things)
