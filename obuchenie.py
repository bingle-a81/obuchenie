from functools import total_ordering
from math import hypot
class TrackLine:
    def __init__(self,to_x,to_y,max_speed,):
        self.to_x = to_x
        self.to_y = to_y
        self.coords=(self.to_x,self.to_y)
        self.max_speed = max_speed



class Track:
    def __init__(self,start_x=0,start_y=0,):
        self.tr=[(start_x,start_y)]

    def add_track(self, tr):
        self.tr.append(tr)

    def get_tracks(self):
        return tuple(self.tr)
    
    def __len__(self):
        return int(sum([hypot(x[0],x[1]) for x in self.tr]))
    
    @total_ordering
    def __eq__(self, __value: object) -> bool:
        return 
        
track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
print(len(track1))

