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
        if self.arcsec_switch == True
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
            for x in gf.groups:
                source = gf.get_group(x)
                sourceDict[('{:.4f}'.format(round(np.mean(source.ra))), '{:.4f}'.format(round(np.mean(source.dec))))] = source
            return source
   
    @staticmethod
    def map_table(grouped_table, reference = None):
        plt.figure()
        plt.title('Mapping of Photometric Sources')
        plt.xlabel('RA')
        plt.ylabel('Dec')
        color = ['blue', 'orange']
        for g in grouped_table:
            if g.has
            plt.scatter(g.ra, g.dec, label = g.thingID.iloc[0], s=7, c=color)
            try:
                plt.annotate(g.thingID.iloc[0], (g.ra.iloc[0], g.ra.iloc[0]), horizontalalignment = 'center', verticalalignment='center', size=20, weight='bold')
                print('annotating')
            except:
                plt.annotate((g.ra.iloc[0], g.dec.iloc[0]), (g.ra.iloc[0], g.dec.iloc[0]), horizontalalignment = 'center', verticalalignment='center', size=520, weight='bold')
        plt.show()
    # TODO: Fix formating so that columns are aligned: Use format strings, or pandas(?)
    @staticmethod
    def show_things(self):
   
        '''
        Run sort_things(table) first!!!
        '''
        
        print('Total things: ', len(things))
        count=0
        for i in things:
            count += len(i)
        print('Total detections: ', count,'\n')
       
        for index, i in enumerate(things):
            print('THING ' + str(index))
            print('---------------------------------')
            for j in i:
                print('RA:'.rjust(10) + str(round(j[0],4)) + ' DEC:'.rjust(10) + str(round(j[1],4)) + ' MJD:'.rjust(10) + str(round(j[2],2)) + ' u:'.rjust(10) + str(round(j[3],2)) + ' g:'.rjust(10) + str(round(j[4],2)) + ' r:'.rjust(10) + str(round(j[5],2)) +' i:'.rjust(10) + str(round(j[6],2)) + ' z:'.rjust(10) + str(round(j[7],2)))
            print('\n')
    
    def unpack_thing(self,index):
        stacked_thing=np.stack(self.l_grouped[index],axis=0)
        return stacked_thing
        # Creates a dictionary of things 
   
    def dict_things(self, things):
        d = {}
        d['thing' + str(i)] = [self.unpack_thing(thing) for i, thing in enumerate(things)]
        return d
    
   

# class panstarrsTool(lcTool):

#     def __init__(self, file_path, indices):
#         super().__init__(file_path)
        
    
#     def group_things(self) -> np.ndarray:
        
#         '''
#         Groups detections by objID or by astrometry variations 
#         '''
       
#         # For PS files with output objID
#         try:
#             df = pd.read_csv(self.file_name)
#             gf = df.groupby('objID')
#             grouped = [gf.get_group(x) for x in gf.groups]
#             [self.l_grouped.append(x.values) for x in grouped]
#             return self.l_grouped
#         # Without objID
#         except KeyError:
#             print('\nSorting by astrometry variations:\n')
#             df = pd.read_csv(self.file_name)
#             gf = df.groupby([np.round(df['ra'],3), np.round(df['dec'],3)])
#             grouped = [gf.get_group(x) for x in gf.groups]
#             self.l_grouped = []
#             [self.l_grouped.append(x.values) for x in grouped]
#             return self.l_grouped
    

# class photoSource():
#     '''
#     Grouped detections of a single galaxy/star. 
#     '''
    
#     def __init__(self, thing, header):
#         '''
#         Initilize with a numpy.ndarray of detections (thing), and a corresponding list of strings
#         representing the detections' respective value types (header). Header is an attribute
#         of lcTools; access the header from a lcTools instance. 
#         '''
#         # Turns list of numpy arrays into a single numpy array of all detections
#         self.thing = np.stack(thing, axis = 0)
#         self.detection_count = len(self.thing)
#         self.header = np.asarray(header)

#     def dict_data(self):
#         d = {}
#         for i in range(len(self.thing[0])):
#             d[self.header[i]] = self.thing[:,i]
#         return d

#     # Sorts an array of dates and an array of magnitudes by the numerical order of the date array
#     def sort_by_date(date,mag,err_mag):
#         date, mag, err_mag= zip(*sorted(zip(date,mag,err_mag)))
#         return np.asarray(date), np.asarray(mag), np.asarray(err_mag)
    
#     @staticmethod
#     def to_fits(name:str):
#         '''
#         Takes in a dictionary of data and outputs to fits file based on key names
#         '''
#         t = Table(dict_data())
#         t.write('/Users/admin/Desktop/astro_research/{}.fits'.format(name))

#     def to_fits2(self,date_index:int, mag_index:int, err_mag_index:int, filter_name:str, name:str):
#         '''
#         Takes the date and photometry of one band of a source and writes it to a fits file
#         '''
        
#         date = self.thing[:,date_index]
#         mag = self.thing[:,mag_index]
#         err_mag = self.thing[:,err_mag_index]

#         t = Table()
#         t['Date'] = Column(date)
#         t[filter_name + '-band'] = Column(mag)
#         t[filter_name + '-band Error'] = Column(err_mag)

#         t.write('/Users/admin/Desktop/astro_research/' + name + '.fits')





