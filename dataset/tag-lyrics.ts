import fs, { readFileSync } from 'fs';

import readline from 'readline';


//OR

const knownThemes = [
    "Pain", "confidence", "Fear",
    "Serenity", "Madness", "Passion",
    "Love", "Confusion", "Hope",
    "Anger", "happiness", "Sadness"
].map(t => t.toLowerCase());

// Represents a row from the csv data file content
class RowItem {
    constructor(
        public readonly title: string, 
        public readonly lyric: string, 
        public readonly idiom: string, 
        public readonly link: string
    ){
        
    }

    public themes: any = {};
    public tag: string = '';

    // update available themes occurences by analising lyric words
    public updateThemes(dico: Dico ) {
        this.themes = {}
        for (let word of knownThemes){this.themes[word.toLowerCase()] = 0; }

        this.lyric.toLowerCase() // convert all to lower case
            .replace(/\W/g, ' ') // replace all non words by white space
            .split(/\s+/g) // cut by white spaces
            .flatMap(word => dico.themes(word))
            .forEach(theme => { this.themes[theme]++; });
    } // end of updateThemes

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
} // end of RowItem

class DicoWord {
    constructor(
        public readonly word: string,
        public readonly themes: string[]
    ) {}

    public static parse(line: string): DicoWord {
        const fields = line.split(/;/g);
        return new DicoWord(fields[0], [... new Set(fields[2].split(/\s+/g))].filter(s => s.length > 0) );
    }
} // end of class DicoWord

class Dico {
    constructor(public readonly words: DicoWord[]){
        for (let w of words) {
            this.themesByWord[w.word] = w;
        }
    }
    private themesByWord: any = {}

    public themes(word: string): string[] {
        const entry = this.themesByWord[word];
        return (entry === undefined)? [] : entry.themes;
    }
} // end of class Dico

// ----------------------------------------------------------------
// parse CSV:


const words_csv_file = 'words_updated.csv';
const lyrics_csv_file = 'lyrics-dataV2.csv';
const classified_csv_file = 'Dataset_Classified.csv';

// charge dico
const dico = loadDico();
// count themes
const allThemes = countAllThemes(dico);
updateSongTag(allThemes);
// print table
printTheme(allThemes);


function loadDico(): Dico {
    const dico: DicoWord[] = [] ;

    readFileSync(words_csv_file, 'utf-8')
        .split(/\r?\n/g)
        .slice(1)
        .filter(line => line.length > 0)
        .forEach(line => {
            const entry = DicoWord.parse(line);
            if (entry.themes.length == 0) return; // skip not tagged entries
            const unknownThemes = entry.themes.filter(t => knownThemes.indexOf(t) < 0);
            if (unknownThemes.length > 0) throw new Error(`Found unknown themes: ${unknownThemes} in dico. Line: ${line}`);
            dico.push(entry);
        });
    return new Dico(dico);
} // end of loadDico

function countAllThemes(dico: Dico): RowItem[] {
    const rows: RowItem[] = [];
    readFileSync(lyrics_csv_file, 'utf-8')
        .split(/\r?\n/g)
        .filter(isValidIdiom)
        .map(line => RowItem.parse(line))
        .forEach(row => {
            row.updateThemes(dico);
            rows.push(row);
        });
    return rows;
    
} // end of countAllThemes


function updateSongTag(allThemes: RowItem[]) {
    readFileSync(classified_csv_file, 'utf-8')
        .split(/\r?\n/g)
        .slice(1)
        .filter(line => line.length > 0)
        .map(line => line.split(/;/g))
        .filter(fields => fields.length >= 2)
        .forEach(fields => {
            const title = fields[0].trim().toLowerCase();
            const r = allThemes.find(row => row.title.trim().toLowerCase() === title);
            if (r === undefined) return;
            r.tag = fields[fields.length - 1];
        });
} // End of updateSongTag


function isValidIdiom(line: string) {
    return  line.substring(line.lastIndexOf(',') + 1).toUpperCase() === 'ENGLISH';
}

function printDico(dico: Dico) {
    for (let e of dico.words) {
       console.log(`DICO => ${e.word}: ${e.themes}`);
    }   
}

function printTheme(allThemes: RowItem[]) {
    console.log('Title;'+knownThemes.map(s => s.substring(0, 1).toUpperCase() + s.substring(1).toLowerCase()).join(";")+';Tag');
    for (let e of allThemes) {
        console.log(e.title+';'+Object.values(e.themes).join(';')+';'+e.tag);
    }
}

