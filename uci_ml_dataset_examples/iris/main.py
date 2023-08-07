from pathlib import Path

import click


@click.command()
@click.option(
    "downloadDataset",
    "-d",
    "--download",
    is_flag=True,
    help="Flag to download the Iris dataset",
)
@click.option(
    "datasetFilepath",
    "-i",
    "--input",
    type=Path,
    required=True,
    nargs=1,
    help="Path to the Iris dataset",
)
def main(downloadDataset: bool, datasetFilepath: Path) -> None:
    pass


if __name__ == "__main__":
    main()
