# lc_tools

Light Curve tools is a simple script that is meant to take in query outputs from SDSS SkyServer (and eventually PANSTARRS) in the form of CSV files and perform tasks to make a table of detections more useable. 

# Grouping: 
Currently, lcTools most useful function is its grouping function. SDSS databases with DR >= 14 allow for grouping by 'thingID' from the 'DetectionIndex' table, however, the Stripe 82 database lacks a 'thingID'. Individual Stripe 82 detections are grouped into their respective star/galaxy by finding similar coordinate positions. Both grouping methods use pandas.DataFrame.group_by() which allows for quick grouping compared to other naive methods

# Goals: 

- Make object that actually does the plotting after all objects are grouped. Right now, lcTools is meant to be treated as a simple helper instance to go along with a user's personalized plotting script. It would be nice to expand this to make quick, simple light curves. 

- Some sort of way to interface directly with the SkyServer CasJobs query tool and have a script access it directly. This could replace having to open a browser, go to CasJobs, make a query, dowload a .csv into the correct folder, and then do the plotting. Astroquery might help with this (?). 
        
