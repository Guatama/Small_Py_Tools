import csv
from xlsxwriter.workbook import Workbook

def csv2xlsx(flist, result_name='result', sep='\t'):
    options = {
        'constant_memory': True,
        'strings_to_formulas': False,
        'strings_to_urls': False
    }

    if sep == '\t':
        file_type = '.tsv'
    else:
        file_type = '.csv'

    # flist = glob.glob(f'*.{file_type}')
    workbook = Workbook(f'{result_name}.xlsx', options=options)

    for sh in flist:
        name = sh.replace(f'{file_type}', '')
        worksheet = workbook.add_worksheet(name)
        print('Start: ' + sh)
        with open(sh, 'rt', encoding='utf8') as f:
            
            reader = csv.reader(f, delimiter=sep)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write(r, c, col)
        print('Done: ' + sh)
        print('-' * 10)

    workbook.close()