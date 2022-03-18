from os.path import join
from os.path import isfile


class DesktopEntry:
    entry_type: str
    ico_path: str
    name: str
    exe_path: str
    version: int
    encoding: str
    terminal: bool

    def __init__(self, encoding: str, version: int, exe_path: str, name: str, ico_path: str, entry_type="Application",
                 terminal=False):
        self.terminal = terminal
        self.entry_type = entry_type
        self.ico_path = ico_path
        self.name = name
        self.exe_path = exe_path
        self.version = version
        self.encoding = encoding

    def to_str(self):
        formatted_string = f"[Desktop Entry]\n\
                            Encoding={self.encoding}\n\
                            Version={self.version}\n\
                            Type={self.entry_type}\n\
                            Terminal={self.terminal}\n\
                            Exec={self.exe_path}\n\
                            Name={self.name}\n\
                            Icon={self.ico_path}\n"

    def gen_filename(self):
        return self.name.join(self.name.split()).lower() + ".desktop"

    # print desktop entry to file
    def flush(self, entry_dir="~/.local/share/applications/"):
        newfile = join(entry_dir, self.gen_filename())
        if not isfile(newfile):
            with open(newfile, 'w') as entry_file:
                entry_file.write(self.to_str())
