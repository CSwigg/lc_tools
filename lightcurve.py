import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.time import Time
from lcTools import lcTool, groupedThing
import os 
import traceback
stripe82_data=np.genfromtxt('/Users/admin/Desktop/astro_research/our_object.csv',delimiter=',',skip_header=1)
csv_data_path = '/Users/admin/Desktop/lc_tools/data_files/'
def flux_to_mag(flux):
    return -2.5*np.log10(flux/3631)

#################### Old Photometry file ##########################
# hdu2=fits.open('/Users/admin/Desktop/astro_research/nev_stripe82_2.fits')
# w3=14.865
# mjd2=np.genfromtxt('/Users/admin/Downloads/nevpsb_photo.txt',usecols=0,delimiter='',dtype=float)
#################### Old Photometry file ##########################
'''
Here I change the photometry file that I'm comparing to because of a
few (~6) points that I couldn't locate in the old file (nev_stripe82.fits)
with a CasJobs query. I use the points I found for our source in a CasJobs query 
and wrote that out to a fits file using lc_tools.to_fits(). Wrote as 'thing0.fits'.
It only contains the i-band photometry. 
'''
hdu2 = fits.open('/Users/admin/Desktop/astro_research/our_objectDR14_clean.fits')


mjd=hdu2[1].data['Date']
t=Time(mjd,format='mjd')
date_spec = t.decimalyear

i_mag = hdu2[1].data['i-band'] 
i_err = hdu2[1].data['i-band Error']


############# These lines correspond to reading in data from nev_stripe82_2.fits ###############

# date_spec=np.array([1998.7329,1998.8836,2000.7527,2002.6781,2002.7603,2002.7603,2002.7603,2002.7603,2002.8288,2002.8288,2002.8534,2003.7411,2003.7411,2003.7986,2003.7986,2003.8096,2003.8753,2003.8753,2003.8863,2003.8863,2004.9495,2007.889,2010.0123])
# date_spec=[1998.7329,1998.8836,2000.7527,2002.6781,2002.7603,2002.7603,2002.7603,2002.7603,2002.8288,2002.8288,2002.8534,2003.7411,2003.7411,2003.7986,2003.7986,2003.8096,2003.8753,2003.8753,2003.8863,2003.8863,2004.9495,2007.889]
# date_spec=t.decimalyear

# u_mag=hdu2[1].data['modelmag_u']
# g_mag=hdu2[1].data['modelmag_g']
# r_mag=hdu2[1].data['modelmag_r']
# i_mag=hdu2[1].data['modelmag_r']
# z_mag=hdu2[1].data['modelmag_z']

# gspec_mag=22.7173
# rspec_mag=21.6198
# ispec_mag=20.8538

# g_mag=np.append(g_mag,gspec_mag)
# r_mag=np.append(r_mag,rspec_mag)
# i_mag=np.append(i_mag,ispec_mag)

# u_err=hdu2[1].data['modelmagerr_u']
# g_err=hdu2[1].data['modelmagerr_g']
# r_err=hdu2[1].data['modelmagerr_r']
# i_err=hdu2[1].data['modelmagerr_i']
# z_err=hdu2[1].data['modelmagerr_z']

############# These lines correspond to reading in data from nev_stripe82_2.fits ###############


# gspec_mag_err=0.672822
# rspec_mag_err=0.369691
# ispec_mag_err=0.177411

# g_err=np.append(g_err,gspec_mag_err)
# r_err=np.append(r_err,rspec_mag_err)
# i_err=np.append(i_err,ispec_mag_err)


###########################################
# date=stripe82_data[:,2]
# i_mag=stripe82_data[:,6]
# i_err=stripe82_data[:,9]
# time=Time(date,format='mjd')
# print(time)
# date_spec=time.decimalyear


# date_spec,i_mag,i_err=zip(*sorted(zip(date_spec,i_mag,i_err)))

###########################################

# plt.title('Light Curve')
# plt.xlabel('Date')
# plt.ylabel('Magnitude')



# plt.plot(date_spec,g_mag,linewidth=0.5,linestyle='--',label='g',c='green')
# plt.scatter(date_spec,g_mag,s=10,c='green')
# plt.errorbar(date_spec,g_mag,g_err,fmt='none',c='green',linewidth=0.5)

# plt.plot(date_spec,r_mag,linewidth=0.5,linestyle='--',label='r',c='red')
# plt.scatter(date_spec,r_mag,s=10,c='red')
# plt.errorbar(date_spec,r_mag,r_err,fmt='none',c='red',linewidth=0.5)

# plt.plot(date_spec,i_mag,linewidth=0.5,linestyle='--',label='i-band: our source',c='orange')
# plt.scatter(date_spec,i_mag,s=10,c='orange')
# plt.errorbar(date_spec,i_mag,i_err,fmt='none',c='orange',linewidth=0.5,capsize=1)

# plt.plot(date_manual,z_mag,linewidth=0.5,linestyle='--',label='z',c='purple')
# plt.scatter(date_manual,z_mag,s=10,c='purple')
# plt.errorbar(date_manual,z_mag,z_err,fmt='none',c='purple',linewidth=0.5)


def plot_check(thing_index, things, header):
    plt.figure()
    plt.title('Light Curve: SDSS i-band')
    plt.xlabel('Date')
    plt.ylabel('Magnitude')
    
    gt = groupedThing(things[int(thing_index)], header)
    
    # gt.to_fits(dict_data, 'our_objectDR14_clean.fits')
    thing = gt.thing
    ###### SDSS ######
    plt.plot(date_spec,i_mag,linewidth=0.5,linestyle='--',c='orange')
    plt.scatter(date_spec,i_mag,s=10,c='orange',label='Our Object: DR14')
    plt.errorbar(date_spec,i_mag,i_err,fmt='none',c='orange',linewidth=0.5,capsize=1,ecolor='orange')

    ra_t = thing[:,0]
    dec_t = thing[:,1]
    mjd_t=thing[:,2]
    u_t=thing[:,3]
    g_t=thing[:,4]
    r_t=thing[:,5]
    i_t=thing[:,6]
    z_t=thing[:,7]
    err_i_t=thing[:,9]
   
    t2=Time(mjd_t,format='mjd')
    d_t=t2.decimalyear
    d_t,i_t,err_i_t=zip(*sorted(zip(d_t,i_t,err_i_t)))
    plt.scatter(d_t,i_t,s=10,label='Our Object Stripe 82 at ra={}, dec={}'.format(np.round(ra_t[0],3),np.round(dec_t[0],3)))
    # plt.plot(d_t,i_t1,linewidth=0.5,linestyle='--')
    plt.errorbar(d_t,i_t,err_i_t,fmt='none',linewidth=0.5,capsize=2,c='b')
    ###### SDSS ######
   
    plt.legend()
    plt.gca().invert_yaxis()
    plt.show()

# Pass in instance of lcTools 
def diff_phot(table:lcTool):
    things = table.group_things()
    table.show_things(things)
    header = table.header
    # List of dictionaries
    d_things = []
    
    [d_things.append(groupedThing(thing,header).dict_data()) for thing in things]

    for x in d_things:
        if x['thingID'][0] == 77759292:
            our_object = x


    i_mags = {}
    errs_i = {}
    dates = {}
    
    for index, x in enumerate(d_things):
        if len(x['mjd_i']) == len(our_object['mjd_i']) and np.mean(x['modelMag_i']) <= 20.5 and np.mean(x['modelMag_i']) >= 19.5:
            i_mags[index] = x['modelMag_i']
            errs_i[index] = x['modelMagErr_i']
            dates[index] = x['mjd_i']
    
    print(i_mags.keys())
    median = np.median((i_mags[28],i_mags[42],i_mags[52],i_mags[55],i_mags[67],i_mags[68],i_mags[81],i_mags[110],i_mags[115],i_mags[134],i_mags[139],i_mags[140],i_mags[147],i_mags[150],i_mags[163],i_mags[168],i_mags[170],i_mags[195],i_mags[197],i_mags[207],i_mags[208],i_mags[222],i_mags[226],i_mags[228],i_mags[242],i_mags[265],i_mags[267],i_mags[272],i_mags[281],i_mags[286]),axis = 0)
    plt.figure()
    # plt.title('Median i-band of 30 sources overplotted on our object\'s light curve')
    plt.title('NeV i-band - median(30 other souces i-band)')
    plt.xlabel('MJD')
    plt.ylabel('Magnitude')
    plt.scatter(our_object['mjd_i'], our_object['modelMag_i'] - median)
    plt.plot(our_object['mjd_i'], our_object['modelMag_i'] - median)
    # plt.scatter(our_object['mjd_i'], our_object['modelMag_i'], label='Our Object')
    # plt.scatter(our_object['mjd_i'], median, label='Median 30 sources')
    plt.gca().invert_yaxis()
    # plt.legend()
    plt.show()

# Compares changes in photometry
def diff_photometry_dr14(things):
    '''
    Plotting below corresponds to the 'DR14.csv' file. 
    '''

    dict_things = check.dict_things(things)
    
    thing0 = dict_things['thing0']
    d0 = thing0[:,2]
    i0 = thing0[:,6]
    err_i0 = thing0[:,9]
    d0, i0, err_i0 = check.sort_by_date(d0, i0, err_i0)
    print(i0)
    thing1 = dict_things['thing1']
    d1 = thing1[:,2]
    i1 = thing1[:,6]
    err_i1= thing1[:,9]
    d1, i1, err_i1 = check.sort_by_date(d1, i1, err_i1)

    thing4 = dict_things['thing4']
    d4 = thing4[:,2]
    i4 = thing4[:,6]
    err_i4= thing4[:,9]
    d4, i4, err_i4 = check.sort_by_date(d4, i4, err_i4)

    thing6 = dict_things['thing6']
    d6 = thing6[:,2]
    i6 = thing6[:,6]
    err_i6 = thing6[:,9]
    d6, i6, err_i6 = check.sort_by_date(d6, i6, err_i6)

    thing7 = dict_things['thing7']
    d7 = thing7[:,2]
    i7 = thing7[:,6]
    err_i7 = thing7[:,9]
    d7, i7, err_i7 = check.sort_by_date(d7, i7, err_i7)

    thing10 = dict_things['thing10']
    d10 = thing10[:,2]
    i10 = thing10[:,6]
    err_i10 = thing10[:,9]
    d10, i10, err_i10 = check.sort_by_date(d10, i10, err_i10)

    # median = np.median((i1,i6,i7,i10),axis=0)
    plt.figure()
    #########################
    # print(i0)
    # print(median)
    # print(i0 - median)
    # plt.scatter(d0,i0 - median)
    # plt.plot(d0, i0 - median)
    #########################
    
    plt.scatter(d4, i4 - i4,color = 'blue')
    plt.plot(d4, i4 - i4,label='Star (ra=' + str(round(things[4][0][0]/3600,4)) +', dec=' + str(round(things[4][0][1]/3600,4)) + ')',color='blue')
    
    plt.scatter(d4, i0 - i4,color='orange')
    errorsA = np.sqrt((err_i0)**2 + (err_i4)**2)
    plt.errorbar(d4, i0 -i4, errorsA,fmt='none',linewidth=0.5,capsize=2, ecolor='orange')
    plt.plot(d4,i0 - i4,color = 'orange', label='Our source - Star')
    
    print(d4 - d0)
    
    plt.scatter(d4, i7 - i4,color= 'green')
    plt.plot(d4, i7 - i4,label = 'Other Galaxy (ra='+str(round(things[7][0][0]/3600,4)) + ', dec='+str(round(things[7][0][1]/3600,4)) + ') - Star', color='green')
    errorsB = np.sqrt((err_i7)**2 + (err_i4)**2)
    plt.errorbar(d4, i7 -i4, errorsB,fmt='none',linewidth=0.5,capsize=2,ecolor='green')
    print(d7 - d4)
    
    plt.legend()
    plt.show()

    


    
def return_things(self,things):
    self.things = things
    return self.things


def plot_show():
    user_input='y'
    while user_input=='y':
        table = lcTool(csv_data_path)
        try:
            table.deg_to_arcsec()
            things = table.group_things()
            table.show_things(things)
            choice=input('Which thing?: ')
            while choice != '':
                plot_check(choice, things, table.header)
                choice=input('Which thing?: ')
            user_input=input('Continue? (y/n): ')
        except Exception as e:
            if type(e) is TypeError and table is None:
                print('\nERROR: lc_tools never got a valid .csv file; table was set to None \n')
            else:
                print('\n' + traceback.format_exc() + '\n')
                print(type(e))
                  
            user_input = input('Continue? (y/n): ')
        

def table_data():
    user_input = 'y'
    while user_input == 'y':
        table = lcTool(csv_data_path)
       
        try:
            table.deg_to_arcsec()
            
            diff_phot(table)
            # diff_photometry_dr14(things)
         
        except Exception as e:
            print(e)
            if type(e) is TypeError:
                print('\nERROR: lc_tools never got a valid .csv file; table was set to None \n')
            else:
                print('\n' + traceback.format_exc() + '\n')
                print(type(e))
            
            user_input = input('Continue? (y/n): ')

plot_show()
# things,table = table_data()
