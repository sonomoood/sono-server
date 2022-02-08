import { model, Schema } from "mongoose";

var musicSchema = new Schema({
    title: {
        type: String,
        required: true
    },
    mood: {
        type: String,
        required: true
    },
    lyrics: {
        type: String,
        required: true
    }
});

export const musicModel = model("music", musicSchema)