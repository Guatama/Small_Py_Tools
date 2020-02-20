from pprint_table import pprint_table

# Mock data for visual testing
headers = ['Name', 'Path', 'Creation time', 'Total', 'Complete']
data = [
    {
        'name_of_item': 'folder_1',
        'fullpath': '//home/folder_2/new_folder/folder_1',
        'time_when_folder_created': '2020.02.15 15:44:02',
        'total_jobs': '10543',
        'completed_jobs': '154'
    },
    {
        'name_of_item': 'HIDDEN ITEM',
        'fullpath': '',
        'time_when_folder_created': '',
        'total_jobs': '',
        'completed_jobs': ''
    },
    {
        'name_of_item': 'folder_2',
        'fullpath': '//home/folder_2/new_folder/folder_1',
        'time_when_folder_created': '2022.01.18 19:42:52',
        'total_jobs': '1543',
        'completed_jobs': '10'
    },
    {
        'name_of_item': 'folder_3',
        'fullpath': '//home/folder_2/new_folder/folder_1',
        'time_when_folder_created': '2009.03.15 15:44:02',
        'total_jobs': '634',
        'completed_jobs': '45'
    },
    {
        'name_of_item': 'HIDDEN ITEM_2',
        'fullpath': '',
        'time_when_folder_created': '',
        'total_jobs': '',
        'completed_jobs': ''
    },
    {
        'name_of_item': 'folder_4',
        'fullpath': '//home/folder_2/new_folder/folder_1',
        'time_when_folder_created': '2010.01.25 13:44:02',
        'total_jobs': '332243',
        'completed_jobs': '1454'
    }
]


def test_main(data, header):
    """Prints some test tables

    Arguments:
        :data: List[Dict[str, str]] -- data for printing
        header List[str] -- new names for columns in order of keys in dict (working with Python 3.7+)
    """
    for i in range(0, 2):
        print(f'Test {i+1}')
        print('Without main_attributes')
        pprint_table(list_with_data=data, main_attr=None, limit=i, full=False)
        print('\nWith 2 main_attributes')
        pprint_table(list_with_data=data, main_attr=['name_of_item', 'fullpath'], limit=i, full=False)
        print('\nWith 2 main_attributes and full=True')
        pprint_table(list_with_data=data, main_attr=['name_of_item', 'fullpath'], limit=i, full=True)
        print()
        print('\nWithout main_attributes but with header')
        pprint_table(list_with_data=data, main_attr=None, limit=i, full=False, header=headers)
        print('\nWith 2 main_attributes and header')
        pprint_table(list_with_data=data, main_attr=['name_of_item', 'fullpath'], header=['COOL NAME', 'Way to go'], limit=i, full=False)
        print()


def test_stairs(data, header):
    """Prints stairs using tables

    Arguments:
        :data: List[Dict[str, str]] -- data for printing
        header List[str] -- new names for columns in order of keys in dict (working with Python 3.7+)
    """
    for i in range(len(data)):
        pprint_table(list_with_data=data, main_attr=list(data[0].keys())[:i], header=headers[:i], limit=len(data)-i)


if __name__ == "__main__":
    test_main(data, headers)
    test_stairs(data, headers)
