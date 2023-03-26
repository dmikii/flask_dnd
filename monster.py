class Monster():
    __table__ = 'monsters'
    columns = ['id', 'name', 'size', 'type', 'alignment', 'ac',
                'hp', 'str', 'dex', 'con', 'int', 'wis', 'cha']
    
    def __init__(self, values):
        self.__dict__ = dict(zip(self.columns, values))

