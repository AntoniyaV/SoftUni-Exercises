def play_instrument(instrument):
    return instrument.play()


# Test code:
class Guitar:
    def play(self):
        print("playing the guitar")


guitar = Guitar()
play_instrument(guitar)


class Piano:
    def play(self):
        print("playing the piano")


piano = Piano()
play_instrument(piano)
