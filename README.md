# jalex
Just Another Lexer is a jison-compatible lexical analyzer with streaming capability.

```JavaScript

var Jalex = require("jalex");
var fs = require("fs");
var stdout = require("process").stdout;
var Parser = require("jison").Parser;

var lexer = new Jalex();

// Jalex will emit an error if an unmatched token
// is found in the input
lexer.on("error", err => {
    console.error(err);
    lexer.pause();
});

// match ID tokens in the input and
// set yytext on the lexer
lexer.addRule(/[A-Za-z_]\w+/, (match) => {
    // Jalex doesn't set yytext itself
    lexer.yytext = match;
    return 'ID';
});

// matches STRINGs in the input
lexer.addRule(/['"](.*)['"]/, function(match, s1) {
    // s1 captures the the first subgroup
    this.yytext = s1; // this is set to the lexer instance
    return 'STRING';
});

fs.createReadStream("testfile").pipe(lexer).pipe(stdout);

```