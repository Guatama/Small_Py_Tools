import typing as tp

def pprint_table(list_with_data: tp.List[tp.Dict[str, str]],
                 main_attr: tp.List[str]=None,
                 limit: int=None, 
                 full: bool=False) -> None:
    """[summary]
    
    Arguments:
        list_with_data {[List[Dict[str, str]], ...]} -- [description]
    
    Keyword Arguments:
        main_attr {[List[str]]} -- [description] (default: {None})
        limit {int} -- [description] (default: {None})
        full {bool} -- [description] (default: {False})
    """
    attr_list = list(list_with_data[0].keys())

    attr_config = dict.fromkeys(attr_list, False)
    if main_attr is None:
        full = True
    else:
        for item in main_attr:
            attr_config[item] = True

    len_dict = {}
    for item in attr_list:
        len_dict[item] = len(item)

    # Enter the maximum width for each column in the counter
    for line in list_with_data:
        for item in attr_list:
            # BUG! all_attr-type of task have separate sets of attributes
            try:
                if len_dict[item] < len(str(line[item])):
                    len_dict[item] = len(str(line[item]))
            except Exception:
                continue

    # Print header table with delimiter =
    for item in attr_config:
        if attr_config[item] or full:
            print(f'{item:{len_dict[item]}} : ', end='')
    print()
    for item in attr_config:
        if attr_config[item] or full:
            print(f'{"=":=<{len_dict[item]}} : ', end='')
    print()

    line_counter = 0
    for line in list_with_data:
        # Check limit of output
        if limit is not None and line_counter >= limit:
            break
        else:
            line_counter += 1

        # Print table row
        for item in attr_config:
            if attr_config[item] or full:
                print(f'{line[item]:{len_dict[item]}} : ', end='')
        print()

if __name__ == "__main__":
    mock_data = [
        {
            'name_of_item': 'folder_1',
            'fullpath': '//home/folder_2/new_folder/folder_1',
            'time_when_folder_created': '2020.02.15 15:44:02',
            'lock_state': ' ',
            'total_jobs': '10543',
            'completed_jobs': '154'
        },
        {
            'name_of_item': 'folder_2',
            'fullpath': '//home/folder_2/new_folder/folder_1',
            'time_when_folder_created': '2022.01.18 19:42:52',
            'lock_state': '🔒',
            'total_jobs': '1543',
            'completed_jobs': '10'
        },
        {
            'name_of_item': 'folder_3',
            'fullpath': '//home/folder_2/new_folder/folder_1',
            'time_when_folder_created': '2009.03.15 15:44:02',
            'lock_state': '🔒',
            'total_jobs': '634',
            'completed_jobs': '45'
        },
        {
            'name_of_item': 'folder_4',
            'fullpath': '//home/folder_2/new_folder/folder_1',
            'time_when_folder_created': '2010.01.25 13:44:02',
            'lock_state': ' ',
            'total_jobs': '332243',
            'completed_jobs': '1454'
        }
    ]

    pprint_table(mock_data) 