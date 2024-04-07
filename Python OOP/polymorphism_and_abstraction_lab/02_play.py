class Children:
    def play(self):
        return "Children are playing"


def start_playing(instance):
    return instance.play()


children = Children()
print(start_playing(children))