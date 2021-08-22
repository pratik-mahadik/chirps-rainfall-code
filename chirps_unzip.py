import gzip, shutil

for year in range(2003,2020):
    for mon in range(1,13):
        mon ="{0:02}".format(mon)
        for day in range(1,31):
            day = "{0.02}".format(day)
            filepath="c:/chirps/%s/"%(year)
            filenm="chirps-v2.0.%s.%s.%s.tif.gz"%(year,month,day)
            outpath="c:/chirps/unzipped/%s/"%(year)
            if(os.path.isfile('%s%s'%(filepath,filenm))):
                with gzip.open('%s%s'%(filepath,filenm), 'r') as f_in, open('%s%s'%(outpath,filenm), 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
