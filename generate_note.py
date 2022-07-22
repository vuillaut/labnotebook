## Generate template for next meeting note

from pathlib import Path
import datetime
import argparse

parser = argparse.ArgumentParser(description='Generate note')
parser.add_argument('--dir', '-d',
                    dest='directory',
                    default=False,
                    type=bool,
                    help='If True, make a new directory to include the notes')

args = parser.parse_args()



if __name__ == '__main__':

    today = datetime.date.today()

    notes_dir = Path(f'{Path(__file__).absolute().parent}/posts')
    template_file = Path(__file__).absolute().parent.joinpath('template_note.md')
    assert notes_dir.exists()
    assert template_file.exists()

    with open(template_file) as f:
        template = f.read()


    template = template.replace('$DATE', f'"{today}"')

    if args.directory:
        notes_dir = notes_dir.joinpath(f'{today}')
        notes_dir.mkdir(exist_ok=True)

    new_file = notes_dir.joinpath(f'{today}.md')
    if new_file.exists():
        raise OSError(f'The file {new_file} for the next meeting already exists. Stopping.')

    else:
        with open(new_file, 'w') as f:
            f.write(template)
        print(f'File {new_file} created')
