import unittest
import youtube


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.video = youtube.Video('https://www.youtube.com/watch?v=nKIu9yen5nc')

    def test_title(self):
        self.assertEqual(self.video.title, '''What Most Schools Don't Teach''')

    def test_duration(self):
        self.assertEqual(self.video.duration, '05:44')

    def test_date(self):
        self.assertEqual(self.video.date, '2013-02-26')

    def test_description(self):
        description = 'Learn about a new "superpower" that isn\'t being taught in 90% ' \
                      'of US schools. \n\nStarring Bill Gates, Mark Zuckerberg, will.i.am, ' \
                      'Chris Bosh, Jack Dorsey, Tony Hsieh, Drew Houston, Gabe Newell, ' \
                      'Ruchi Sanghvi, Elena Silenok, Vanessa Hurst, and Hadi Partovi. ' \
                      'Directed by Lesley Chilcott, executive producers Hadi and Ali Partovi.' \
                      '\n\nCode.org owes special thanks to all the cast and the film crew, ' \
                      'and also Microsoft, Google/YouTube, Facebook, Amazon, ' \
                      'and Twitter for helping us spread the word\n\n' \
                      '(If you want to help translate to other languages, ' \
                      'visit http://www.code.org/translate)\n\n' \
                      'Help us caption & translate this video!\n\nhttps://amara.org/v/BeyV/'
        self.assertEqual(repr(self.video.description), repr(description))

    def test_category(self):
        self.assertIsNotNone(self.video.category)

    def test_license(self):
        self.assertIsNotNone(self.video.license)

    def test_keywords(self):
        self.assertIsNotNone(self.video.keywords)

    def test_statistics(self):
        self.assertIsNotNone(self.video.statistics['likes'])
        self.assertIsNotNone(self.video.statistics['dislikes'])
        self.assertIsNotNone(self.video.statistics['rating'])
        self.assertIsNotNone(self.video.statistics['views'])

    def test_channel(self):
        self.assertIsNotNone(self.video.channel['title'])
        self.assertIsNotNone(self.video.channel['subscribers'])
        self.assertIsNotNone(self.video.channel['id'])
        self.assertIsNotNone(self.video.channel['url'])

    def test_player(self):
        self.assertIsNotNone(self.video.player['sts'])
        self.assertIsNotNone(self.video.player['url'])

    def test_streams(self):
        self.assertTrue(len(self.video.streams['adaptive']['audio']) > 0)
        self.assertTrue(len(self.video.streams['adaptive']['video']) > 0)
        self.assertTrue(len(self.video.streams['multiplexed']) > 0)

        self.assertEqual(self.video.best_adaptive()['audio']['bitrate'], '128056')
        self.assertEqual(self.video.best_adaptive()['video']['bitrate'], '4276030')
        self.assertEqual(self.video.best_multiplexed()['quality'], 'hd720')

    def test_captions(self):
        self.assertTrue(len(self.video.captions) > 0)


if __name__ == "__main__":
    unittest.main()
