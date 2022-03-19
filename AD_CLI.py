import argparse
from DesktopEntryStruct import DesktopEntry


def main():
    # set up argument parser
    parser = argparse.ArgumentParser(prog='AD_CLI', description='Automatically create and install .desktop files for '
                                                                'your apps', )

    parser.add_argument('name', type=str, help='The name of the app')
    parser.add_argument('exe_path', type=str, help='Path to the app\'s executable')
    parser.add_argument('-d', '--description', type=str, default="", help="Application description")
    parser.add_argument('-i', '--icon_path', type=str, help='Path to an icon image for the app')
    parser.add_argument('-t', action='store_true', help='Execute with external terminal')
    parser.add_argument('--entry_type', type=str, default='Application', help='The type of entry (default: Application')

    # parse the args
    args = parser.parse_args()

    # create object with inputted data
    new_entry = DesktopEntry(args.exe_path,
                             args.name,
                             args.icon_path,
                             args.entry_type,
                             args.t,
                             args.description)

    # flush that data into a file in the proper location
    if not new_entry.is_empty():
        print(args)
        print(new_entry.to_str())
        new_entry.flush()


if __name__ == '__main__':
    main()
