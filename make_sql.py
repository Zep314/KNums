from util.settings import Settings
import csv
from tqdm import tqdm


if __name__ == '__main__':
    with open(Settings().result, 'r', encoding='UTF-8') as input_csv:
        reader = csv.reader(input_csv, delimiter=';', quotechar='"')

        file_count = 0
        file_open = False
        insert_row_count = 0
        values_count = 0

        for row in tqdm(reader, desc='Прогресс'):
            if (row[0] != 'TU_RLTY_KID') and (row[1] == '0'):  # пропускаем заголовок
                ss = "".join(['  into XXX_KNUM (tu_rlty_kid,cadastral_number) values ('
                              , row[0]
                              , ",'"
                              , row[3]
                              , "')"
                              , '\n'
                              ])

                if (not file_open):
                    output_sql = open("".join([Settings().output_sql,'\\',f'{file_count:04}','.sql'])
                                        , 'w', encoding='cp1251')
                    file_open = True
                    file_count += 1
                    output_sql.write('insert all\n')

                output_sql.write(ss)
                insert_row_count += 1
                values_count += 1

                if insert_row_count >= Settings().insert_row_limit:
                    output_sql.write('select * from dual;\n')
                    output_sql.write('insert all\n')
                    insert_row_count = 0

                if values_count >= Settings().values_limit:
                    output_sql.write('select * from dual;\n')
                    output_sql.write('commit work;\n')
                    output_sql.close()
                    file_open = False
                    insert_row_count = 0
                    values_count = 0

        output_sql.write('select * from dual;\n')
        output_sql.write('commit work;\n')
        output_sql.close()

