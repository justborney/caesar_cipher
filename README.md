# Caesar cipher
This project is an implementation of the Caesar cipher to encrypt and decrypt 
text. It solves the problem of transforming an input string by shifting each character by 
a certain number of positions in the alphabet.
The algorithm is implemented for both Russian and English.

## Contents
- [Technology](#technology)
- [Usage](#usage)
- [Contributing](#contributing)
- [To do](#to-do)
- [Project team](#project-team)

## Technology
- [Python3](https://www.python.org/)
- [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Usage.

Import encryption and decryption functions from the `.ceaser_cipher.caesar`
```Python
from .ceaser_cipher.caesar import encryption_caesar, decryption_caesar
```

## Tests

For tests simply run `unit_testing.sh`
```shell
bash unit_testing.sh
```
or run the tests in the source code folder with the command `python -m unittest` in the terminal.

## Contributing
How can I help with project development? How to submit a suggestion or bug report. 
How to send modification (issue pull request, what kind of steelguides are used): [CONTRIBUTING.md](./CONTRIBUTING.md).

## To do
- [x] Add a cool README
- [x] Add unittests
- [x] Rewrite without `ord()` and `chr()`
- [x] Add comments and docstrings
- [x] Add Russian language support
- [x] Add CONTRIBUTING.md
- [x] Add CHANGELOG.md
- [ ] Automate CHANGELOG.md

## Project team

- [Ainur Taktamyshev](tg://resolve?domain=justborn) - Python Backend developer