import unittest
import src.audio_loader as audio_loader

class TestMixerInit(unittest.TestCase):
    def testInit(self):
        audio_loader.initMixer()
        self.assertEqual(audio_loader.mixer.get_init(), (22050, -16, 2))

class TestMixer(unittest.TestCase):
    def setUp(self):
        audio_loader.initMixer()

    def testQuit(self):
        audio_loader.quitMixer()
        self.assertEqual(audio_loader.mixer.get_init(), None)

    def testNumberOfChannels(self):
        audio_loader.eightChannels()
        self.assertEqual(audio_loader.mixer.get_num_channels(), 8)

    def testSoundObjectFromFile(self):
        track = audio_loader.createSoundObject("o_nata_lux.wav")
        self.assertTrue(track)

if __name__ == "__main__":
    unittest.main()