## Generate template for next meeting note

from pathlib import Path
import datetime
import argparse

parser = argparse.ArgumentParser(description='Generate note')

parser.add_argument('--title', '-t',
                    dest='title',
                    type=str,
                    required=False,
                    default=None,
                    help='Add a title')

parser.add_argument('--dir', '-d',
                    dest='directory',
                    action='store_true',
                    help='make a new directory to include the notes')


args = parser.parse_args()



if __name__ == '__main__':

    today = datetime.date.today()

    notes_dir = Path(f'{Path(__file__).absolute().parent}/posts')
    template_file = Path(__file__).absolute().parent.joinpath('template_note.md')
    assert notes_dir.exists()
    assert template_file.exists()

    with open(template_file) as f:
        template = f.read()

    if args.title:
        title = args.title
        filename = f'{today.strftime("%Y-%m-%d")}_{args.title.replace(" ", "_")}'
    else:
        title = f'{today.strftime("%Y-%m-%d")}'
        filename = f'{today.strftime("%Y-%m-%d")}'


    template = template.replace('$DATE', f'"{today}"')
    template = template.replace('$TITLE', f'"{title}"')

    if args.directory:
        notes_dir = notes_dir.joinpath(f'{filename}')
        notes_dir.mkdir(exist_ok=True)

    new_file = notes_dir.joinpath(f'{filename}.md')
    if new_file.exists():
        raise OSError(f'The file {new_file} for the next meeting already exists. Stopping.')

    else:
        with open(new_file, 'w') as f:
            f.write(template)
        print(f'File {new_file} created')
