class BaseEntity:
    def toJSON(self):
        return self.__dict__
