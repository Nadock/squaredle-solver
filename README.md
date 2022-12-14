# Squaredle Solver

Find all the valid and bonus words in a [Squaredle](https://squaredle.app) game.

## Usage

You'll need a working Python 3.8 or later, then run:

```bash
$> python -m squaredle ./words_alpha.txt ./games/2022-11-01.txt

Loaded Squaredle Game -- "LEN LIT SLY"

From L (0, 0) there are 20 words:
LILT, LENIS, LENITY, LILE, LITE, LILLY, LINTEL, LINTELS, LENTIL, LILY, LENT, LINET, LINT, LEIS, LIEN, LILL, LISLE, LINE, LINTY, LENTILS

From E (0, 1) there are 2 words:
ELLS, ELSIN

From N (0, 2) there are 9 words:
NELLY, NILS, NILL, NILLS, NELL, NEIL, NIELS, NETI, NILE

From I (1, 1) there are 9 words:
ILLY, ISLET, INTEL, ITLL, ILLS, ISLE, ITEL, ITEN, INTL

From T (1, 2) there are 13 words:
TILE, TELLS, TILL, TILLY, TELI, TELL, TEIL, TIEN, TELLIN, TILS, TINE, TELLY, TILLS

From S (2, 0) there are 16 words:
SLIT, SLITE, SLILY, SLENT, SILEN, SILLY, SINE, SILENT, SLINE, SILENTLY, SLINTE, SILE, SILTY, SILL, SITE, SILT

From Y (2, 2) there are 4 words:
YILLS, YITE, YILT, YILL

Found 73 words in total
```

The `./words_alpha.txt` argument is a text file containing a newline delimited list of
valid words to reference when searching for Squardle words.

The `./games/2022-11-01.txt` argument is a text file containing the Squardle board as
newline separated rows of characters.

## Loading Current Games

Okay so fair warning, this section does cross the line into cheating IMO.

The `:/load_current_games.py` script reads the Squaredle API and extracts the current
available games — usually today and yesterdays games. It then writes out the game board
to the `:/games` directory.

The script also writes a corresponding `_words.txt` file which is the part that is kinda
cheating. It contains a list of only the valid & bonus words for the corresponding game.
You can use this file instead of the `words_alpha.txt` file to ensure 100% accuracy of
the results.

This script uses the `requests` library to read the API, which if you don't have already
you can install yourself or run the script in the Pipenv environment via:

```console
pipenv install
pipenv run ./load_current_games.py
```
