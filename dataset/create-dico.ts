
import fs from 'fs';

import readline from 'readline';


//OR

// Represents a row from the csv data file content
class RowItem {
    constructor(
        public readonly title: string, 
        public readonly lyric: string, 
        public readonly idiom: string, 
        public readonly link: string
    ){}

    // returns the lyric as a map of words occurences
    // ex: [feel: 1, time: 2, sea: 1, the: 10, night: 1, ...]
    public words(): any {
       
        let response = this.lyric.toLowerCase() // convert all to lower case
            .replace(/\W/g, ' ') // replace all non words by white space
            .split(/\s+/g) // cut by white spaces
            .reduce((acc: any, v: string) => {
                let k = ""+v+"";
                if (acc[k] === undefined) acc[k] = 1;
                else acc[k] = acc[k] + 1;
                return acc;
            }, {}); // count occurences

        return response;
    } // end of words

    // Parse a line of CSV data and initialize a row item
    static parse(line: string): RowItem {
        let pos = 0;
        let nxtPos = 0;
        let fields = [];
        for (let i = 0; i < 3; i++) {
            nxtPos = line.indexOf(',', pos);
            fields.push(line.substring(pos, nxtPos));
            pos = nxtPos + 1;
        }
        nxtPos = line.lastIndexOf(',');

        fields.push(line.substring(pos, nxtPos));
        fields.push(line.substring(nxtPos + 1));
        return new RowItem(fields[1], fields[3], fields[4], fields[2]);
    } // end of parse
}

// ----------------------------------------------------------------
// parse CSV:

let allWords: any = {};
const rl = readline.createInterface({
    input: fs.createReadStream('../../lyrics-data.csv'),
    output: process.stdout,
    terminal: false
});


rl.on('line', (line: string) => {
    if (!isValidIdiom(line)) return;
    let row = RowItem.parse(line);
    feedAllWords(row);
    //printRow(row);

   // rl.close();
    
}).on('close', () => {
    filterWords();

    printAllWords();
    console.log('\n', "=== END OF FILE REACHED ===");
});

function feedAllWords(row: RowItem) {
    const W = row.words();
    for ( let k of Object.keys(W)) {
        if (allWords[k] === undefined) allWords[k] = W[k];
        else allWords[k] += W[k];
    }
}

function filterWords() {
    allWords = Object.keys(allWords)
        .filter(k => allWords[k] >= 1000) // keep words with at least 100 occurences
        .filter(k => k.length >= 4) // keep words with at least 4 letters length
        .sort() // sort words by alphabetical order
        .reduce((obj: any, key) => { obj[key] = allWords[key]; return obj; }, {});
}

function printRow(row: RowItem) {
    console.log("===> LINE::: ", row.title, "|", row.idiom, '|', row.link
        , '\n'
        , row.lyric.replace(/\.+/g, '.\n')
        , '\nWORDS: ', row.words()
        ,'\n---------');

}

function printAllWords() {
    console.log(
        "ALL WORDS: "
        ,"\nWord;Occurences;Themes");
    for (let [k, v] of Object.entries(allWords)) {
        console.log(k+';'+v+';'+'');
    }
}

function isValidIdiom(line: string) {
    return  line.substring(line.lastIndexOf(',') + 1).toUpperCase() === 'ENGLISH';
}




