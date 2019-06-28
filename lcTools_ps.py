from lcTools import lcTools

class lcTools_ps(lcTools):
            # set PANSTARRS table
    # TODO this could be a @classmethod that specializes a table for 
    def set_table():
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
    
        # Sorts PANSTARRS i-band only
    @staticmethod
    def sort_things(table):
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

    @staticmethod
    def show_things(things):
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