class state(object):

    def __repr__(self):
        return getattr(self, 'name', '<unnamed state>')
