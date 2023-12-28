from collections.abc import Iterable


class FRangeIterator:
    def __init__(self, start, stop, step):
        self.current = start - step
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return FRangeIterator(self.start, self.stop, self.step)


fr = FRange(0, 2, 0.5)
if isinstance(FRange, Iterable):
    print("True")
else:
    print(False)
it1 = iter(fr)
it2 = iter(fr)
print(next(it1))  # 0.0
print(next(it1))  # 0.5
print(next(it2))  # 0.0
print(next(it2))  # 0.5
