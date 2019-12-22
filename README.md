# lcTools

Light Curve tools is a simple script that is meant to take in query outputs from SDSS SkyServer (and eventually PANSTARRS) in the form of CSV files and perform tasks to make a table of detections more useable. Also capable of retrieving a direct SQL query from the SDSS Stripe 82 and DR14 databases following an example string such as:

```
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
```
# Direct query to SDSS databases and group the rows by corresponding sources
```
import lcTools as lc
sdss_version = 'DR14'
grouped_sources = lc.photoTable.sql_retrieve(sdss_version, query_txt, s = True) # Returns dictionary
```

# Read in csv file and group the rows by corresponding sources\
```
grouped_sources = lc.photoTable('path_to_file', sdss_version, sort = True) # Returns dictionary
```


# Future
- Single statistic variability check (Swinbank el al. 2015)
- Actual documentation. 
        
