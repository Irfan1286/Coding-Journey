
class Maths:
    subjects = 'Maths'
    @classmethod    # This is a decorator assigned by @
    def change_subject(cls, subject):
        cls.subjects = subject
        return cls.subjects

Tawsif = Maths()

print(Tawsif.change_subject('Bangla'))

# class methods can be used as alternative form of constructors
class brands:
    def __init__(self, name, sale, complains):
        self.name = name
        self.sale = sale
        self.complains = complains
    @classmethod
    def from_slash(cls, string):
        # newlist = string.split('/')     # splits the string
        # return(newlist)
        return cls(*string.split('/'))

# xiaomi = brands('Mi', '7.2M', '50')       # previously this now full string
xiaomi = brands.from_slash('Mi-Ui/98M/40')
print(xiaomi.sale)