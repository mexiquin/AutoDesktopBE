from os.path import join, isfile, expanduser


class DesktopEntry:
    entry_type: str
    ico_path: str
    name: str
    exe_path: str
    terminal: bool
    description: str

    def __init__(self, exe_path: str, name: str, ico_path: str, entry_type: str,
                 terminal: bool, description: str):
        self.terminal = terminal
        self.entry_type = entry_type
        self.ico_path = ico_path
        self.name = name
        self.exe_path = exe_path
        self.description = description

    def to_str(self):
        return f'[Desktop Entry]\n' \
               f'Name={self.name}\n' \
               f'Type={self.entry_type}\n' \
               f'Terminal={str(self.terminal).lower()}\n' \
               f'Exec={self.exe_path}\n' \
               f'Icon={self.ico_path}\n' \
               f'Comment={self.description}'

    def gen_filename(self):
        return self.name.join(self.name.split()).lower() + ".desktop"

    # print desktop entry to file
    def flush(self, entry_dir=f"{expanduser('~')}/.local/share/applications/"):
        newfile = join(entry_dir, self.gen_filename())
        if not isfile(newfile):
            with open(newfile, 'w') as entry_file:
                entry_file.write(self.to_str())

    # validate object is not null-populated
    def is_empty(self) -> bool:
        return None in (self.terminal,
                        self.entry_type,
                        self.ico_path,
                        self.name,
                        self.exe_path,
                        self.description)
