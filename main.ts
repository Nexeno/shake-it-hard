basic.forever(function () {
    if (false) {
        music.playTone(330, music.beat(BeatFraction.Whole))
        music.playTone(311, music.beat(BeatFraction.Whole))
        music.playTone(330, music.beat(BeatFraction.Whole))
        music.playTone(311, music.beat(BeatFraction.Whole))
        music.playTone(330, music.beat(BeatFraction.Whole))
        music.playTone(247, music.beat(BeatFraction.Whole))
        music.playTone(294, music.beat(BeatFraction.Whole))
        music.playTone(262, music.beat(BeatFraction.Whole))
        music.playTone(220, music.beat(BeatFraction.Double))
        music.rest(music.beat(BeatFraction.Whole))
        music.playTone(131, music.beat(BeatFraction.Whole))
        music.playTone(165, music.beat(BeatFraction.Whole))
        music.playTone(220, music.beat(BeatFraction.Whole))
        music.playTone(247, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Whole))
        music.playTone(165, music.beat(BeatFraction.Whole))
        music.playTone(208, music.beat(BeatFraction.Whole))
        music.playTone(247, music.beat(BeatFraction.Whole))
        music.playTone(262, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Whole))
    } else {
        music.stopMelody(MelodyStopOptions.All)
    }
})
