import numpy as np
from astropy.time import Time
from lcTools import panstarrsTool
import matplotlib.pyplot as plt
ps_data=np.genfromtxt('/Users/admin/Desktop/lc_tools/data_files/ps1.csv',delimiter=',',usecols=(5,26,27,10),names=True) 
header = list(ps_data.dtype.names)
def flux_to_mag(flux):
    return -2.5*np.log10(flux/3631)
def fluxErr_to_magErr(flux,flux_err):
    return -2.5*(0.434)*(flux_err/(flux))
def panstarrs_nearby(data):
    
    g=[]
    g_err=[]
    g_date=[]
    g_ra=[]
    g_dec=[]
    
    r=[]
    r_err=[]
    r_date=[]
    r_ra=[]
    r_dec=[]

    i=[]
    i_err=[]
    i_date=[]
    i_ra=[]
    i_dec=[]

    z=[]
    z_err=[]
    z_date=[]
    z_ra=[]
    z_dec=[]

    y=[]
    y_err=[]
    y_date=[]
    y_ra=[]
    y_dec=[]

    filter=data[:,3]
    fluxes=data[:,4]
    fluxes_err=data[:,5]
    ra=data[:,0]
    dec=data[:,1]
    dates=data[:,2]
    for k, j in enumerate(filter):
        if j==1:
            g.append(flux_to_mag(fluxes[k]))
            t=Time(dates[k],format='mjd')
            g_date.append(t.decimalyear)
            g_err.append(fluxErr_to_magErr(fluxes[k],fluxes_err[k]))
            g_ra.append(ra[k])
            g_dec.append(dec[k])
        elif j==2:
            r.append(flux_to_mag(fluxes[k]))
            t=Time(dates[k],format='mjd')
            r_date.append(t.decimalyear)
            r_err.append(fluxErr_to_magErr(fluxes[k],fluxes_err[k]))            
            r_ra.append(ra[k])
            r_dec.append(dec[k])          
        elif j==3:
            i.append(flux_to_mag(fluxes[k]))
            t=Time(dates[k],format='mjd')
            i_date.append(t.decimalyear)
            i_err.append(fluxErr_to_magErr(fluxes[k],fluxes_err[k]))
            i_ra.append(ra[k]*3600)
            i_dec.append(dec[k]*3600)
        elif j==4:
            z.append(flux_to_mag(fluxes[k]))
            t=Time(dates[k],format='mjd')
            z_date.append(t.decimalyear)  
            z_err.append(fluxErr_to_magErr(fluxes[k],fluxes_err[k]))
            z_ra.append(ra[k])
            z_dec.append(dec[k])
        elif j==5:
            y.append(flux_to_mag(fluxes[k]))
            t=Time(dates[k],format='mjd')
            y_date.append(t.decimalyear)
            y_err.append(fluxErr_to_magErr(fluxes[k],fluxes_err[k]))
            y_ra.append(ra[k])
            y_dec.append(dec[k])
        ps_thing=[]
        ps_thing=np.asarray(ps_thing)
    i=np.asarray(i)
    i_err=np.asarray(i_err)
    i_ra=np.asarray(i_ra)
    i_dec=np.asarray(i_dec)
    i_date=np.asarray(i_date)
    ps_thing=np.column_stack((i_ra,i_dec,i_date,i,i_err))
    
    
    print(ps_thing)
    return ps_thing

def panstarrs_our_object(data):

    g=[]
    g_err=[]
    g_date=[]
    r=[]
    r_err=[]
    r_date=[]
    i=[]
    i_err=[]
    i_date=[]
    z=[]
    z_err=[]
    z_date=[]
    y=[]
    y_err=[]
    y_date=[]
    filter=data[:,0]
    fluxes=data[:,1]
    dates=data[:,3]
    fluxes_err=data[:,2]
    for k, j in enumerate(filter):
        if j==1:
            g.append(flux_to_mag(fluxes[k]))
            t=Time(dates[k],format='mjd')
            g_date.append(t.decimalyear)
        elif j==2:
            r.append(flux_to_mag(fluxes[k]))
            t=Time(dates[k],format='mjd')
            r_date.append(t.decimalyear)
        elif j==3:
            i.append(flux_to_mag(fluxes[k]))
            i_err.append(fluxErr_to_magErr(fluxes[k],fluxes_err[k]))
            t=Time(dates[k],format='mjd')
            i_date.append(t.decimalyear)
        elif j==4:
            z.append(flux_to_mag(fluxes[k]))
            t=Time(dates[k],format='mjd')
            z_date.append(t.decimalyear)  
        elif j==5:
            y.append(flux_to_mag(fluxes[k]))
            t=Time(dates[k],format='mjd')
            y_date.append(t.decimalyear)
    return g,r,i,z,y,g_date,r_date,i_date,z_date,y_date,i_err

ps_g,ps_r,ps_i,ps_z,ps_y,g_d,r_d,i_d,z_d,y_d,err_i=panstarrs_our_object(ps_data)
g_d,ps_g=zip(*sorted(zip(g_d,ps_g)))
r_d,ps_r=zip(*sorted(zip(r_d,ps_r)))
i_d,ps_i,err_i=zip(*sorted(zip(i_d,ps_i,err_i)))
z_d,ps_z=zip(*sorted(zip(z_d,ps_z)))
y_d,ps_y=zip(*sorted(zip(y_d,ps_y)))
# plt.scatter(g_d,ps_g,s=10,c='purple')
# plt.plot(g_d,ps_g,linewidth=0.5,linestyle='--',c='purple')
# plt.scatter(r_d,ps_r,s=10,c='red')
# plt.plot(r_d,ps_r,linewidth=0.5,linestyle='--',c='red')
# plt.scatter(i_d,ps_i,s=10,c='green')
# plt.plot(i_d,ps_i,linewidth=0.5,linestyle='--',label='g',c='green')
# plt.scatter(z_d,ps_z,s=10,c='blue')
# plt.plot(z_d,ps_z,linewidth=0.5,linestyle='--',label='g',c='blue')
# plt.scatter(y_d,ps_y,s=10,c='black')
# plt.plot(y_d,ps_y,linewidth=0.5,linestyle='--',label='g',c='black')

def plot_check(thing_index):
    plt.figure()
    plt.title('Light Curve')
    plt.xlabel('Date')
    plt.ylabel('Magnitude')
    
    thing = groupedThing()
    
    ###### PANSTARRS ######
    p_date=thing[:,2]
    p_i=thing[:,3]
    p_err_i=thing[:,4]
    
    p_date,p_i,p_err_i=zip(*sorted(zip(p_date,p_i,p_err_i)))
    plt.scatter(p_date,p_i,s=10,label='Other object',c='blue')
    plt.plot(p_date,p_i,linewidth=0.5,linestyle='--',c='blue')
    plt.errorbar(p_date,p_i,p_err_i,fmt='none',linewidth=0.5,capsize=2,c='blue')

    plt.scatter(i_d,ps_i,s=10,c='orange')
    plt.plot(i_d,ps_i,linewidth=0.5,linestyle='--',c='orange')
    plt.errorbar(i_d,ps_i,err_i,fmt='none',linewidth=0.5,capsize=2,c='orange')
   
    
   
    plt.legend()
    plt.gca().invert_yaxis()
    plt.show()

user_input=''
while user_input=='':
    
    pan_tools = panstarrs_tool()
    mags=panstarrs_nearby(ps_data_nearby)
    things=check.sort_things_ps(mags)
    check.show_things_ps(things)
    choice=input('Which thing?: ')
    
    while choice != '':
        plot_check(choice)
        choice=input('Which thing?: ')
    user_input=input('Hit Enter to continue:')
