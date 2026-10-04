class man:
    def behavior(self):
        print ("this is king")

class weman:
    def behavior(self):
        print("this is quine")

def attetuid (habbit):
    habbit.behavior()

man = man()
weman = weman()

attetuid(man)
attetuid(weman)