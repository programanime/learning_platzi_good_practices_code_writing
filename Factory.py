class MobileFactory:
    def __init__(self, model, name):
        self.model=model
        self.name=name
    
    model=2021
    @classmethod
    def create(cls, name):
        return MobileFactory(cls.model,name)

print(MobileFactory.create("toyota").model)