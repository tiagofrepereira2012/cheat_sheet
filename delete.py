import click
import os
import shutil


@click.command()
@click.argument("path")
@click.option("--relative-paths", "-r", multiple=True)
@click.option("--directories", "-d", multiple=True)
@click.option("--execute", "-x", is_flag=True, required=False)
def delete_files(path, relative_paths, directories, execute):

    if not execute:
        print("################")
        print("Dry run !!!!!!!!")
        print("################")

    for r in relative_paths:
        for d in directories:
            dirname = os.path.join(path, r, d)
            if os.path.exists(dirname):
                print(f"Deleting {dirname}")
                if execute:
                    shutil.rmtree(dirname)
            else:
                print(f"Directory {dirname} doesn't exist")

    pass


if __name__ == "__main__":
    delete_files()
