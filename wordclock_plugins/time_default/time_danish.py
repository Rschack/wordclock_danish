''' Provided by Schack'''


import datetime as dt

class time_danish():
    '''
    This class returns a given time as a range of LED-indices.
    Illuminating these LEDs represents the current time on a Danish WCA
    '''

    def __init__(self):
        self.prefix = range(0,7) +  range(8,10) # -> KLOKKEN ER
        self.minutes=[[], \
            # -> FEM MINUTTER OVER
            range(11,14) + range(36,44) + range(49,51), \
            # -> TI MINUTTER OVER
            range(33,35) + range(36,44) + range(49,51), \
            # -> KVART OVER
            range(25,30) + range(49,51), \
            # -> TYVE MINUTTER OVER
            range(14,18) + range(36,44) + range(49,51), \
            # -> FEM MINUTTER I HALV
            range(11,14) + range(36,44) + range(60,61) + range(62,66), \
            # -> HALV
            range(62,66), \
            # -> FEM MINUTTER OVER HALV
            range(11,14) + range(36,44) + range(47,51) + range(62,66), \
            # -> TYVE MINUTTER I
            range(14,18) + range(36,44) + range(60,61), \
            # -> KVART I
            range(25,30) + range(60,61), \
            # -> TI MINUTTER I
            range(33,35) + range(36,44) + range(60,61), \
            # -> FEM MINUTTER I
            range(11,14) + range(36,44) + range(60,61) ]
            # -> TOLV
        self.hours= [range(106,110), \
            # -> ET
            range(66,68), \
            # -> TO
            range(68,70), \
            # -> TRE
            range(70,73), \
            # -> FIRE
            range(73,77), \
            # -> FEM
            range(77,80), \
            # -> SEKS
            range(80,84), \
            # -> SYV
            range(85,88), \
            # -> OTTE
            range(88,92), \
            # -> NI
            range(93,95), \
            # -> TI
            range(97,99),\
            # -> ELLEVE
            range(99,105), \
            # -> TOLV
            range(106,110)]

    def get_time(self, time, withPrefix=True):
        hour=time.hour%12+(1 if time.minute/5 >= 7 else 0)
        minute=time.minute/5
        # Assemble indices
        return  \
            (self.prefix if withPrefix else []) + \
            self.minutes[minute] + \
            self.hours[hour] + \
            (self.full_hour if (minute == 0) else [])
