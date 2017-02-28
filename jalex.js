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

module.exports = class JaLex extends Transform {
    constructor(options) {
        super(options);
        this.rules = [];
        this.input = "";
        this.index = 0;
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
    addRule(regex, handler) {
        this.rules.push({
            regex: new RegExp(regex.source, regex.flags + "y"),
            handler: handler
        });
    }
    setInput(input) {
        this.input = input.toString();
        this.index = 0;
    }
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
            } else if (token === 'REJECT') {
                this.index++;
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
