import cx_Freeze

executables = [cx_Freeze.Executable('snake_game.py')]

cx_Freeze.setup(
    name="snake_game",
    options={'build_exe': {'packages':['pygame'],
                           'include_files':['imag']}},

    executables = executables
    
)