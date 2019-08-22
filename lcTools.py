import numpy as np
import os
from astropy.table import Table, Column
import matplotlib.pyplot as plt
import csv
import pandas as pd

'''
Light curve tools are meant to take in a csv output file from a CasJobs query
and assist with quick light curve plots.
'''


class photoTable:
    
    def __init__(self, file_path, arcsec_switch = False):
        self.file_name = file_path
        self.table=[]
        self.l_grouped = []
        self.arcsec_switch = arcsec_switch
        # Attribute file_name to use throughtout the instance since file_name has to be set to null at end of __init__

        while (not os.path.exists(self.file_name)):
            print('\nWARNING: Table was not initialized.\n')
            self.file_name = None
            return 
           

        with open(self.file_name) as f: 
            self.table = pd.read_csv(self.file_name)
        
    def deg_to_arcsec(self):
        if self.arcsec_switch == False:
            self.table[['ra','dec']] = self.table[['ra','dec']] * 3600
            self.arcsec_switch = True

    def arcsec_to_deg(self):
        if self.arcsec_switch == True:
            self.table[['ra','dec']] = self.table[['ra','dec']] / 3600
            self.arcsec_switch = False
    
    def group_things(self, make_map = False):
        
        '''
        Groups detections by thingID or by astrometry variations (if .csv file is from 
        database < DR14)
        '''
       
        # For databases >= DR14
        sourceDict = {}
        try:
            gf = self.table.groupby('thingID')
            for x in gf.groups:
                source = gf.get_group(x)
                sourceDict[str(source.thingID.iloc[0])] = source
            return sourceDict
        # Sorting for stripe82 and databases < DR14
        except KeyError:
            print('\nSorting by astrometry variations:\n')
            self.table.deg_to_arcsec()
            gf = self.table.groupby([np.round(self.table['ra'],3), np.round(self.table['dec'],3)])
            self.table.arcsec_to_deg()
            for x in gf.groups:
                source = gf.get_group(x)
                sourceDict[('{:.4f}'.format(round(np.mean(source.ra))), '{:.4f}'.format(round(np.mean(source.dec))))] = source
            return source
   
    def make_source(self, source_key):
        gf = self.group_things()
        return photoSource(gf[source_key])


    @staticmethod
    def map_table(grouped_table, reference = None):
        plt.figure()
        plt.title('Mapping of Photometric Sources')
        plt.xlabel('RA')
        plt.ylabel('Dec')
        # color = [3 : 'blue', 6 : 'orange']
        for key, value in grouped_table.items():
            try:
                # SELECT p.type from photoObj <-- SDSS CAS
                plt.scatter(value.ra, value.dec, s=10, c=color[value.type.iloc[0]])
            except:
                plt.scatter(value.ra, value.dec, s=10, c='black')

            try:
                plt.annotate(key, (value.ra.iloc[0], value.ra.iloc[0]), horizontalalignment = 'center', verticalalignment='center', size=20, weight='bold')
                print('annotating')
            except:
                plt.annotate(key, (value.ra.iloc[0], value.dec.iloc[0]), horizontalalignment = 'center', verticalalignment='center', size=20, weight='bold')
        plt.show()

    




    

class photoSource():
    '''
    Grouped detections of a single galaxy/star. 
    '''
    
    def __init__(self, source):
        '''
        Initilize with a dictionary of detections (source); key being some sort of ID string or 
        a tuple of coordiantes (strings)
        '''
        self.source = source
        self.detection_count = len(self.source.values)
    
    # Sorts an array of dates and an array of magnitudes by the numerical order of the date array
    def sortDetection_by_date(date,mag,err_mag):
        date, mag, err_mag= zip(*sorted(zip(date,mag,err_mag)))
        return np.asarray(date), np.asarray(mag), np.asarray(err_mag)
    
    @staticmethod
    def to_fits(name:str):
        '''
        Takes in a dictionary of data and outputs to fits file based on key names
        '''
        t = Table(dict_data())
        t.write('/Users/admin/Desktop/astro_research/{}.fits'.format(name))

    def to_fits2(self,date_index:int, mag_index:int, err_mag_index:int, filter_name:str, name:str):
        '''
        Takes the date and photometry of one band of a source and writes it to a fits file
        '''
        
        date = self.thing[:,date_index]
        mag = self.thing[:,mag_index]
        err_mag = self.thing[:,err_mag_index]

        t = Table()
        t['Date'] = Column(date)
        t[filter_name + '-band'] = Column(mag)
        t[filter_name + '-band Error'] = Column(err_mag)

        t.write('/Users/admin/Desktop/astro_research/' + name + '.fits')



tbl = photoTable('data_files/DR14_clean.csv')
gf = tbl.group_things()
print(gf)

