/**
 * MIT License
 * 
 * Copyright (c) 2017 Cory Cook
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

var Transform = require("stream").Transform;

class Location {
    /**
     * Should usually be constructed without a parameter; however,
     * can also be used as a copy constructor.
     * @param {Location|null} initial_values
     */
    constructor({ first_line = 1, last_line = 1, first_column = 0, last_column = 0, first_index = 0, last_index = 0 } = {}) {
        this.first_line = first_line;
        this.first_column = first_column;
        this.last_line = last_line;
        this.last_column = last_column;
        this.first_index = first_index;
        this.last_index = last_index;
    }
    /**
     * Updates the counts for the next substring of the input.
     * @param {string} text the string text to use to update counts
     */
    push(text) {
        var lines = text.split('\n');
        this.first_line = this.last_line;
        this.last_line = this.first_line + lines.length - 1;
        this.first_column = this.last_column;
        this.last_column = (lines.length > 1 ? 0 : this.first_column) + lines[lines.length - 1].length;
        this.first_index = this.last_index;
        this.last_index = this.first_index + text.length;
    }
}

module.exports = class Jalex extends Transform {
    /**
     * Just Another Lexer is a jison-compatible lexical analyzer with streaming capability.
     * @param {object} options the options forwarded to the Transform constructor
     */
    constructor(options) {
        super(options);
        this.rules = [];
        this.input = "";
        this.index = 0;
        this.yyloc = new Location();
    }
    _transform(buffer, encoding, callback) {
        this.input += buffer.toString();
        for (let token = this.lex(); token; token = this.lex()) {
            this.push(token);
            if (token === 'EOF') {
                break;
            }
        }
        this.input = this.input.substring(this.index);
        this.index = 0;
        callback();
    }
    /**
     * Add a lexical rule to watch for on the input.
     * @param {RegExp} regex The rule to match against the string input.
     * @param {function(...string)} handler The rule handler
     * will be called when 
     */
    addRule(regex, handler) {
        this.rules.push({
            regex: new RegExp(regex.source, regex.flags + "y"),
            handler: handler
        });
    }
    /**
     * Jison method to set the input.
     * @param {string|Buffer} input String or buffer input
     */
    setInput(input) {
        this.input = input.toString();
        this.index = 0;
        this.yyloc = new Location();
    }
    /**
     * Jison method to retrieve the next token in the input.
     */
    lex() {
        var token;
        while (!token && !this.isPaused()) {
            let match;
            if (this.index === this.input.length) {
                token = 'EOF';
                break;
            }
            var rules = this.rules.map(r => {
                r.regex.lastIndex = this.index;
                return Object.assign({ match: r.regex.exec(this.input) }, r)
            }).filter(r => r.match && r.match.index === this.index)
                .sort((a, b) => b.match[0].length - a.match[0].length);
            if (rules.some(r => {
                match = r.match;
                token = r.handler.apply(this, match);
                return token !== 'REJECT';
            })) {
                this.index += match[0].length;
                this.yyloc.push(match[0]);
            } else if (token === 'REJECT') {
                this.index++;
                this.yyloc.push(match[0][0]);
                token = null;
            } else {
                this.emit('error', new Error(`Unmatched symbol: '${this.input[this.index]}' at ${this.index}`));
                return;
            }
        }
        this.emit('token', token);
        return token;
    }
}

Jalex.Location = Location;
