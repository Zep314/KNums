from util.knum import Knum
from util.settings import Settings
import csv
from tqdm import tqdm
from time import sleep


class Controller:
    def __init__(self):
        self.knum = Knum()

    def run(self):
        with open(Settings().result, 'w', encoding='UTF-8') as output_csv:
            writer = csv.writer(output_csv,delimiter=';', quotechar='"')
            writer.writerow(['TU_RLTY_KID',
                             'Error',
                             'Error_text',
                             'KNum'
                             ])
            with open(Settings().base, 'r', encoding='UTF-8') as input_csv:
                reader = csv.reader(input_csv, delimiter=';', quotechar='"')
                for row in tqdm(reader, desc='Прогресс'):
                    if row[0] != 'TU_RLTY_KID':  # пропускаем заголовок
                        ouput_row = self.knum.get(
                              street =      row[5]
                            , street_type = row[4]
                            , house =       row[6]
                            , building =    row[7]
                            , settlement =  row[2]
                            , type_town =   row[3]
                            , apartment =   row[8]
                            , fiasid =      row[9]
                        )
                        ouput_row.insert(0,row[0])
                        writer.writerow(ouput_row)

                        sleep(Settings().sleep_delay)





