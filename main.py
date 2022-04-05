def on_forever():
    while input.is_gesture(Gesture.SHAKE):
        if False:
            music.stop_melody(MelodyStopOptions.ALL)
basic.forever(on_forever)

def on_forever2():
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(311, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(311, music.beat(BeatFraction.WHOLE))
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    music.play_tone(247, music.beat(BeatFraction.WHOLE))
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.play_tone(220, music.beat(BeatFraction.DOUBLE))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(131, music.beat(BeatFraction.WHOLE))
    music.play_tone(165, music.beat(BeatFraction.WHOLE))
    music.play_tone(220, music.beat(BeatFraction.WHOLE))
    music.play_tone(247, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.WHOLE))
    music.play_tone(165, music.beat(BeatFraction.WHOLE))
    music.play_tone(208, music.beat(BeatFraction.WHOLE))
    music.play_tone(247, music.beat(BeatFraction.WHOLE))
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    music.rest(music.beat(BeatFraction.WHOLE))
    if True:
        pass
    while input.is_gesture(Gesture.SHAKE):
        pass
basic.forever(on_forever2)
