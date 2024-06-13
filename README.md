# Victoria 2 Analyzer

Includes a parser and a commandline tool. Still very much in development, but can be used to view losses in wars.

Warning for a slow parser and spaghetti code.

## Running

First compile the parser with
`gcc -shared -o analyzer/parser/parser.so -fPIC -O2 analyzer/parser/parser.c`

Then run with
`python analyzer [path/to/.v2|.json]`
