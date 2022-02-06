import { model, Schema } from "mongoose";

var music = new Schema({
    track: {
        type: String,
        required: true
    },
    seed: {
        type: String,
        required: true
    },
    Lyrics: {
        type: String,
        required: true
    }
});

export const musicModel = model("music", music)