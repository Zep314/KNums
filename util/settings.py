class Settings:
    base: str

    def __init__(self):
#        self.base = 'C:\\Work\\python\\KNums\\SQL\\base2.csv '
#        self.result = 'C:\\Work\\python\\KNums\\SQL\\result.csv '
        self.base = '/opt/KNums/SQL/base2.csv'
        self.result = '/opt/KNums/SQL/result.csv'
        self.sleep_delay_min = 0.2
        self.sleep_delay_max = 2
        self.sleep_delay_step = 0.2
        self.sleep_current = 2
        self.error_try = 3

    def reset_delay(self):
        self.sleep_current = self.sleep_delay_max

    def decrease_delay(self):
        if self.sleep_current > self.sleep_delay_min:
            self.sleep_current -= self.sleep_delay_step
        else:
            self.sleep_current = self.sleep_delay_min

    def get_delay(self):
        return self.sleep_current