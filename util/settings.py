class Settings:
    base: str

    def __init__(self):
#        self.base = 'C:\\Work\\python\\KNums\\SQL\\base1.csv '
#        self.result = 'C:\\Work\\python\\KNums\\SQL\\result.csv '
        self.base = '/opt/KNums/SQL/base2.csv'
        self.result = '/opt/KNums/SQL/result.csv'
        self.sleep_delay = 0.2
