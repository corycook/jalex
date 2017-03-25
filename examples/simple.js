
var Jalex = require("../jalex");
var lex = new Jalex();

lex.addRule(/\s+/, () => { });
lex.addRule(/\w+/, function(id) {
    this.yytext = id;
    return 'ID';
});
lex.addRule(/simple example/, () => {
    console.log("\n\'simple example\' found.");
    return 'REJECT';
});

lex.pipe(process.stdout);
lex.write("a simple example word capture");
