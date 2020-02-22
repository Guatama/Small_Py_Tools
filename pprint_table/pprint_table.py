import typing as tp
from warnings import warn
from platform import python_version_tuple


def pprint_table(list_with_data: tp.List[tp.Dict[str, str]],
                 main_attr: tp.List[str]=None,
                 header: tp.List[str]=None,
                 limit: int=None,
                 full: bool=False) -> None:
    """Printing tables in the terminal

    Arguments:
        list_with_data->List[Dict[str, str]], ...] -- input data in format:
        [ One elemnt in list - one line of table
            {
            'Column_name': 'Value_in_line',
            'Column_name': 'Value_in_line',
            ...
            },
            ...
        ]

    Keyword Arguments:
        main_attr->List[str] -- List of columns to display (default: None)
        limit->int -- Limit the number of rows in a table (default: None)
        full->bool -- Show all columns from data (default: bool->False)
    """
    # Check that user has Python 3.7+
    py_version = python_version_tuple()
    is_py3 = int(py_version[0]) >= 3
    is_py37 = is_py3 and int(py_version[1]) >= 7
    if not is_py3 or not is_py37:
        warn('Your version is, the order of columns in the table')

    # Creating basic configurations for displaying a table
    attr_list: tp.List[str] = list(list_with_data[0].keys())
    attr_config: tp.Dict[str, bool] = dict.fromkeys(attr_list, False)

    main_attr = attr_list if main_attr is None else main_attr
    header = attr_list if header is None else header
    header_config: tp.Dict[str, str] = {
        attr_key: header_name for (attr_key, header_name)
        in zip(attr_list, header)
    }

    # Determining how many columns should be displayed
    if main_attr is None:
        full = True
    else:
        for item in main_attr:
            attr_config[item] = True

    # Creating default dict of columns length
    len_dict: tp.Dict[str, int] = {}
    for item in attr_list:
        len_dict[item] = len(item)

    # Enter the maximum width for each column in the data
    for line in list_with_data:
        for item in attr_list:
            if len_dict[item] < len(line[item]):
                len_dict[item] = len(line[item])

    # Print header table with delimiter =
    for item in main_attr:
        if attr_config[item] or full:
            print(f'{header_config[item]:{len_dict[item]}} : ', end='')
    print()
    for item in main_attr:
        if attr_config[item] or full:
            print(f'{"=":=<{len_dict[item]}} : ', end='')
    print()

    # Print line of table
    line_counter = 0
    for line in list_with_data:
        # Check limit of output
        if limit is not None and line_counter >= limit:
            break
        else:
            line_counter += 1

        # Print table row
        for item in main_attr:
            if attr_config[item] or full:
                print(f'{line[item]:{len_dict[item]}} : ', end='')
        print()
