# Jalex

Just Another Lexer is a jison-compatible lexical analyzer with streaming capability.

## Basic Usage

Create an instance of Jalex and add rules to watch for on the input.

```JavaScript
var Jalex = require('jalex');
var lex = new Jalex();

// match tokens
lex.addRule(/[A-Za-z_]\w+/, (match) => {
    return 'ID';
});

// ignore whitespace
lex.addRule(/\s+/, () => { });

// interact using Node Streaming interface
lex.pipe(process.stdout);
lex.write("  token");
```

Jalex will execute the handler for the longest matching rule.

### addRule

The addRule function accepts a regular expression and a handler function.
Both arguments are required. 

The regular expression matches are spread to the arguments of the handler. 
So the first argument is the entire match, the second argument is the 
first subgroup, and so forth.

```JavaScript
lex.addRule(/\s+(\w+)/, (match, name) => {
    console.log(name); // "word"
    return 'NAME';
});
lex.write("   word");
```

## As Jison Lexer

Jalex can be used as a custom lexer for Jison.

```JavaScript
var Jalex = require('jalex');
var lex = new Jalex();

lex.addRule(/[A-Za-z_]\w+/, (match) => {
    return 'ID';
});
lex.addRule(/\s+/, () => { });

var Parser = require('jison').Parser;
var parser = new Parser({
    bnf: {
        S: ["ID EOF", "return 'token';"]
    }
});

// set Jalex as the lexer for Jison
parser.lexer = lex;
var result = parser.parse("   token");
```

## Setting yytext

The **this** argument of the addRule callback
will be the current instance of the lexer.

The **yytext** property can be set on the lexer 
to forward a value to Jison.

```JavaScript
lex.addRule(/\w+/, function(match) {
    this.yytext = match;
    return 'ID';
});

var parser = new Parser({
    bnf: {
        S: ["ID EOF", "return yytext;"]
    }
});
```

Be sure to set **yytext** via the **this** argument as Jison
creates a cloned instance of Jalex during parsing.

## Source mapping with yyloc

As the lexer consumes input, the **yyloc** object on 
the Jalex instance will be updated to indicate the 
position of the token. It has the following
values to assist with source mapping:

- *first_index* the index in the input file where the current match starts
- *last_index* the index in the input file where the current match ends
- *first_line* the line on which the current match begins
- *last_line* the line on which the current match ends
- *first_column* the index on the first line where the current match begins
- *last_column* the index on the last line where the current match ends

The yyloc values should not be altered as the values are 
incremental rather than absolute.

## Special tokens

Jalex responds to and returns for some special tokens: [EOF](#eof) and [REJECT](#reject)

### EOF

Jalex returns the EOF token when it reaches the end of the input.

### REJECT

If the longest matching rule returns a REJECT 
token then Jalex will use the next longest matching 
rule and continue in that fashion until a non-REJECT token
is returned by a handler, nothing is returned (empty rule), or 
no more rules match the input.
In the last case lexing continues at the next input character.

```JavaScript
var Jalex = require("../jalex");
var lex = new Jalex();

lex.addRule(/\s+/, () => { });
lex.addRule(/\w+/, function(id) {
    return 'ID';
});

// look for 'simple example' but reject to allow 'simple' and 'example'
// to match as IDs
lex.addRule(/simple example/, () => {
    console.log("\n\'simple example\' found.");
    return 'REJECT';
});

lex.pipe(process.stdout);
lex.write("a simple example word capture");
```
