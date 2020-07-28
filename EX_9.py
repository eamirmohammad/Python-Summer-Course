#EX_9

class Time:
    '''
    Hour = None
    Minutes = None
    Seconds = None
    '''
    def __init__(self, Hour_value, Minutes_value, Seconds_value):
        self.Hour = Hour_value
        self.Minutes = Minutes_value
        self.Seconds = Seconds_value
    def showlist(arg):
        return [ arg.Hour, arg.Minutes, arg.Seconds ]
    def show(arg):
        return str(arg.Hour)+':'+str(arg.Minutes)+':'+str(arg.Seconds)
    def __str__(self):
        return str(self.Hour)+ ':' + str(self.Minutes) + ':' + str(self.Seconds)
    def __repr__(self):
        return str(self.Hour)+ ':' + str(self.Minutes) + ':' + str(self.Seconds)
    def __add__(self, other) :
        s = self.Seconds + other.Seconds
        m = self.Minutes + other.Minutes
        h = self.Hour + other.Hour
        if s >= 60:
            addsec = s - 60
            m += 1
        else:
            addsec = s
        if m >= 60 :
            addmin = m - 60
            h += 1
        else:
            addmin = m
        if h >= 24:
            addhour = h - 24
        else:
            addhour = h
        
        return addhour, addmin, addsec
    def __sub__(self,other):
        s = self.Seconds - other.Seconds
        m = self.Minutes - other.Minutes
        h = self.Hour - other.Hour
        if s < 0:
            subsec = 60+ s 
            m -= 1
        else:
            subsec = s
        if m < 0:
            submin = m + 60
            h -= 1
        else:
            submin = m
        if h < 00 :
            subhour = h + 24
        else:
            subhour = h
        return subhour, submin, subsec
    def __gt__ (self, other):
        self_time = self.Hour + self.Minutes/60 + self.Seconds/3600
        other_time = other.Hour + other.Minutes/60 + other.Seconds/3600
        if self_time > other_time:
            return True
        else:
            return False
    def __eq__ (self, other) :
        self_time = self.Hour + self.Minutes/60 + self.Seconds/3600
        other_time = other.Hour + other.Minutes/60 + other.Seconds/3600
        if self_time == other_time:
            return True
        else:
            return False
    def __lt__ (self, other):
        self_time = self.Hour + self.Minutes/60 + self.Seconds/3600
        other_time = other.Hour + other.Minutes/60 + other.Seconds/3600
        if self_time < other_time:
            return True
        else:
            return False
        

        
    
    
    
