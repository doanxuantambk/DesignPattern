from abc import abstractmethod
class MediaPlayer:
    @abstractmethod
    def play(self, audioType, fileName):
        pass

class AdvancedMediaPlayer:
    @abstractmethod
    def playVlc(self, fileName):
        pass

    @abstractmethod
    def playMp4(self, fileName):
        pass

class Mp4Player(AdvancedMediaPlayer):
    def playVlc(self, fileName):
        pass

    def playMp4(self, fileName):
        print("Playing mp4 file. Name %s" %(fileName))

class VlcPlayer(AdvancedMediaPlayer):
    def playVlc(self, fileName):
        print("Playing vlc file. Name: %s "%(fileName))

    def playMp4(self, fileName):
        pass

class MediaAdapter(MediaPlayer):
    def __init__(self, audioType):
        if audioType == "vlc":
            self.__advancedMusicPlay = VlcPlayer()
        elif audioType == "mp4":
            self.__advancedMusicPlay = Mp4Player()

    def play(self, audioType, fileName):
        if audioType == "vlc":
            self.__advancedMusicPlay.playVlc(fileName)
        elif audioType == "mp4":
            self.__advancedMusicPlay.playMp4(fileName)

class AudioPlayer(MediaPlayer):
    def play(self, audioType, fileName):
        if audioType == "mp3":
            print("Playing mp3 file. Name: %s" %(fileName))
        elif audioType == "vlc" or audioType == "mp4":
            self.__mediaAdapter = MediaAdapter(audioType)
            self.__mediaAdapter.play(audioType, fileName)
        else:
            print("Invalid media. %s format not supported" % (audioType))


if __name__ == "__main__":
    audioPlayer = AudioPlayer()
    audioPlayer.play("mp3", "beyond the horizon.mp3")
    audioPlayer.play("mp4", "alone.mp4")
    audioPlayer.play("vlc", "far far away.vlc")
    audioPlayer.play("avi", "mind me.avi")