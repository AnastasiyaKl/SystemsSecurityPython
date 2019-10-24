from cx_Freeze import setup, Executable

executables = [Executable('sys_security.py',
                          targetName='sys_security.exe',
                          base='Win32GUI')]
include_files = ['data']

options = {
    'build_exe': {
        'include_msvcr': True,
        'include_files': include_files,
    }
}

setup(name='sys_security',
      version='0.0.1',
      description='Sys_security - lab 1,2',
      executables=executables,
      options=options)