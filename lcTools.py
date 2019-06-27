import numpy as np
import matplotlib.pyplot as plt
import os
from astropy.table import Table, Column
import csv

'''
Light curve tools are meant to take in a csv output file from a CasJobs query
and assist with quick light curve plots.
'''




'''
Ideas for sort functions: 
    -Boring: Load into astropy.table and sort by group_by
    -Fun: Recreate 2-D image of field and use sci-kit learn clusters
'''

class lcTools:
    # set SDSS table
    # TODO make this __init__ method
    def __init__(self,file_path):
        self.file_path=file_path
        self.table=[]
        file_name = self.file_path + input("Please enter the file name of the table you'd like to use (or type 'stop'): ")
       
        while (not os.path.exists(file_name)):
            if file_name == 'stop':
                print('\nWARNING: Table was not initialized.\n')
                return 
            else:
                file_name = input('No such table, try again: ')

        with open(file_name) as f: 
            self.header = next(csv.reader(f, delimiter=','))
            print(self.header)
            self.table = np.genfromtxt(file_name,delimiter=',',dtype='float',skip_header=1)
        



    # set PANSTARRS table
    # TODO this could be a @classmethod that specializes a table for 
    def set_table_ps():
        table=[]
        file_name = input("Please enter the file name of the table you'd like to use (or type 'stop'): ")
        if file_name =='stop':
            print('tried to return')
            return
        while (not os.path.exists(file_name)):
            if file_name == 'stop':
                return
            file_name = input("No such table, try again: ")
        table=np.genfromtxt(file_name,delimiter=',',skip_header=1,dtype='float',usecols=(17,18,10,5,26,27))
        return table

    def deg_to_arcsec(self):
        self.table[:,0:2]=self.table[:,0:2]*3600
        

    # sort for stripe82
    # TERRIBLE FUNCTION
    def sort_things(self):
        things=[]
        used_ra=[]
        for x,y in zip(self.table[:,0],self.table[:,1]):
            if np.any(np.isin(x,used_ra)):
                continue   
            else:  
                thing=[] 
                for i, (x2,y2) in enumerate(zip(self.table[:,0],self.table[:,1])):
                    if np.any(np.isin(x2,used_ra)):
                        continue
                    # These parameters might need a bit of tweaking to sort correctly
                    elif ((np.sqrt((x2 - x)**2 + (y2 - y)**2) < 1)):
                        thing.append(self.table[i])
                        used_ra.append(x2)   
                things.append(thing)
        return(things)

    # Sorts things by thingID; works for DR >= 14
    # This could probably be rewritten using np.split
    def sort_things2(table):
        things=[]
        used_ra=[]
        for ra,thingID in zip(table[:,0],table[:,10]):
            if np.any(np.isin(ra, used_ra)): 
                continue
            else:
                thing=[]
                for i, (ra2,thingID2) in enumerate(zip(table[:,0],table[:,10])):
                    if np.any(np.isin(ra2, used_ra)):
                        continue
                    if thingID2 == thingID:
                        thing.append(table[i])
                        used_ra.append(ra2)
                things.append(thing)
        print(things)
        return(things)

    # Sorts PANSTARRS i-band only
    def sort_things_ps(table):
        things=[]
        used_ra=[]
        for x,y in zip(table[:][:,0],table[:][:,1]):
            if np.any(np.isin(x,used_ra)):
                continue  
            else:
                thing=[]
                for i, (x2,y2) in enumerate(zip(table[:][:,0],table[:][:,1])):
                    if np.any(np.isin(x2,used_ra)):
                        continue
                    elif (abs(x2-x)<1.5) & (abs(y2-y)<1.5):
                        thing.append(table[i])
                        used_ra.append(x2)
                things.append(thing)
        return(things)


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
                print('RA:'.rjust(10) + str(round(j[0]/3600,4)) + ' DEC:'.rjust(10) + str(round(j[1]/3600,4)) + ' MJD:'.rjust(10) + str(round(j[2],2)) + ' u:'.rjust(10) + str(round(j[3],2)) + ' g:'.rjust(10) + str(round(j[4],2)) + ' r:'.rjust(10) + str(round(j[5],2)) +' i:'.rjust(10) + str(round(j[6],2)) + ' z:'.rjust(10) + str(round(j[7],2)))
            print('\n')
   
    @staticmethod   
    def show_things2(things):
        print('Total things: ', len(things))
        count=0
        for i in things:
            count+=len(i)
        print('Total detections: ', count,'\n')
        for index, i in enumerate(things):
            print('THING ' + str(index))
            print('---------------------------------')
            for j in i:
                print('RA:'.rjust(10) + str(round(j[0]/3600,4)) + ' DEC:'.rjust(10) + str(round(j[1]/3600,4)) + ' MJD:'.rjust(10) + str(round(j[2],2)) + ' u:'.rjust(10) + str(round(j[3],2)) + ' g:'.rjust(10) + str(round(j[4],2)) + ' r:'.rjust(10) + str(round(j[5],2)) +' i:'.rjust(10) + str(round(j[6],2)) + ' z:'.rjust(10) + str(round(j[7],2)) + 'thingID:'.rjust(10) + str(j[10]))
            print('\n')
   
    @staticmethod
    def show_things_ps(things):
        print('Total things: ', len(things))
        count=0
        for i in things:
            count+=len(i)
        print('Total detections: ', count,'\n')
        for index, i in enumerate(things):
            print('THING ' + str(index))
            print('---------------------------------')
            for j in i:
                print('RA:'.rjust(10) + str(round(j[0]/3600,4)) + ' DEC:'.rjust(10) + str(round(j[1]/3600,4)) + ' MJD:'.rjust(10) + str(round(j[2],2)) + ' i:'.rjust(10) + str(round(j[3],2)) + ' i_err:'.rjust(10) + str(round(j[4],2)))
            print('\n')
    '''
        Run sort_things(table) first!!!
    '''
    # Separates types of data from a thing into dictionary of arrays 
    # TODO







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
    for i, thing in enumerate(things):
        d['thing' + str(i)] = unpack_thing(thing)
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

