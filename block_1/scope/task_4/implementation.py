def bad_open(file_path, mode):
    """Некорректная функция открытия файла"""
    raise Exception


def open_and_close_file(file_path):
    """Открывает и закрывает файл

    Args:
        file_path: путь до файла
    """
    open = bad_open
    ###
    # Добавьте свой код сюда
    ###

    # region свой код
    def default_open(path, mode):
        import builtins
        return builtins.open(path, mode)

    def correct_open():
        nonlocal open
        open = default_open

    correct_open()
    # endregion
    
    f = open(file_path, 'r')
    f.close()
