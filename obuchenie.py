class A:
    def __init__(self,word) -> None:
        self.word=word
        self.__getattribute__(word)()

    def go(self):
        print('go')

    def stop(self):
        print('stop')

a=A('stop')