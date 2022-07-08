class Singleton:
    instance=None
    @classmethod
    def getInstance(cls):
        if not cls.instance:cls.instance="bien"
        return cls.instance

print(Singleton.getInstance())