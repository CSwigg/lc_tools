# lcTools

Light Curve tools is a simple script that is meant to take in query outputs from SDSS SkyServer (and eventually PANSTARRS) in the form of CSV files and perform tasks to make a table of detections more useable. Also capable of retrieving a direct SQL query from the SDSS Stripe 82 and DR14 databases following an example string such as:

'''
query_txt = 'SELECT TOP 10                         \
    objID, ra, dec, modelMag_u, modelMag_g \
FROM                                       \
    PhotoPrimary                           \
WHERE                                      \
    ra BETWEEN 140 and 141                 \
AND dec BETWEEN 20 and 21                  \
AND type = 6                               \
AND clean = 1                              \
AND modelMag_u - modelMag_g < 0.5'


import lcTools as lc
# Call photoTable classmethod for di
grouped_sources = lc.photoTable.sql_retrieve('DR14', query_txt, s = True)

'''

# Future
- Single statistic variability (Swinbank el al. 2015)
- Actual documentation. 
        
