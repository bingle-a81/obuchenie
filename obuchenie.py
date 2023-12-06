from functools import total_ordering
from math import hypot
class TrackLine:
    def __init__(self,to_x,to_y,max_speed,):
        self.to_x = to_x
        self.to_y = to_y
        self.coords=(self.to_x,self.to_y)
        self.max_speed = max_speed


@total_ordering
class Track:
    def __init__(self,start_x=0,start_y=0,):
        self.tr=[TrackLine(start_x,start_y,0)]

    def add_track(self, tr:TrackLine):
        self.tr.append(tr)

    def get_tracks(self):
        print (self.tr)
        return tuple(self.tr)
    
    def __len__(self):     
        res=(sum(self.__sl(self.tr[i-1].coords[0],self.tr[i-1].coords[1],self.tr[i].coords[0],self.tr[i].coords[1]) for i in range(1,len(self.tr))))
        return int(res)
    
    def __sl(self,x1,y1,x2,y2):
        return ((x1-x2)**2+(y1-y2)**2)**0.5
    

    def __eq__(self, __value) -> bool:
        if not isinstance(__value,TrackLine):
            AssertionError('')
        return len(self)==len(__value)

    def __gt__ (self, __value) -> bool:
        if not isinstance(__value,TrackLine):
            AssertionError('')    
            print(len(self))    
        return len(self)>len(__value)

        
track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
print(len(track1))
print(len(track2))
res_eq = track1 < track2
print(res_eq)
