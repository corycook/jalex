
var Jalex = require('../jalex');
var stdout = require("process").stdout;
var Transform = require("stream").Transform;
var fs = require("fs");

var reservedWords = {
    'from': 'FROM',
    'import': 'IMPORT',
    'as': 'AS',
    'if': 'IF',
    'else': 'ELSE',
    'not': 'NOT',
    'and': 'AND',
    'or': 'OR',
    'in': 'IN',
    'class': 'CLASS',
    'def': 'DEF',
    'for': 'FOR',
    'True': 'TRUE',
    'False': 'FALSE'
};

var lex = new Jalex();

var lastToken = null;
lex.on('token', function (token) {
    lastToken = token;
});
lex.on('error', err => {
    console.error(err.message);
    lex.pause();
});

var indent = 0;
var next = -1;
var braces = [];

lex.addRule(/#(.*)/, () => { });
lex.addRule(/['"]{3,}([\s\S]*?)['"]{3,}/m, () => { });
lex.addRule(/\r?\n/, () => (braces.length === 0 && lastToken !== 'NEWLINE') ? 'NEWLINE' : 'REJECT');
lex.addRule(/([ ]*)([A-Za-z_]\w*)/m, function (m, i, t) {
    if (lastToken === 'NEWLINE' || lastToken === 'DEDENT') {
        if (next == -1) {
            next = Math.floor(i.length / 4);
        }
        if (next != -1 && indent != next) {
            return 'REJECT';
        } else {
            next = -1;
        }
    }
    if (t in reservedWords)
        return reservedWords[t];
    this.yytext = t;
    return 'NAME';
});
lex.addRule(/[ ]*(?=[A-Za-z_]\w*)/, function (m) {
    if (lastToken === 'NEWLINE' || lastToken === 'DEDENT') {
        next = Math.floor(m.length / 4);
    }
});
lex.addRule(/[ ]/, () => {
    if (-1 === next) {
        return;
    } else if (indent < next) {
        indent++;
        return 'INDENT';
    } else if (indent > next) {
        indent--;
        return 'DEDENT'
    }
});
lex.addRule(/[;:\.,<>|=\-\+\*%/]/, m => m);
lex.addRule(/[<>\+\-\*%|=]=/, m => m);
lex.addRule(/[\(\[\{]/, m => {
    braces.push(m);
    return m;
});
lex.addRule(/[\)\]\}]/, m => {
    braces.pop();
    return m;
});
lex.addRule(/\d+\.?\d*/, function (m) {
    this.yytext = m;
    return 'NUMBER';
});
lex.addRule(/['"](.*?[^\\]?)['"]/, function (m, s) {
    this.yytext = s;
    return 'STRING';
});

var level = 0;
var fn = "examples/pokekombat.py";

var file = fs.readFileSync(fn);
var source = file.toString();

fs.createReadStream(fn)
    .pipe(lex)
    .pipe(new Transform({
        transform: (d, enc, c) => {
            var token = d.toString();
            var src = source.substring(lex.yyloc.first_index, lex.yyloc.last_index);
            c(null, `${token}: ${src} (at ${lex.yyloc})\n`);
        }
    }))
    .pipe(stdout);
