from mvc.model import Model

import unittest


class Tests(unittest.TestCase):

    def setUp(self):
        self.model = Model()

    def test_load(self):
        try:
            self.model.loadCSV()
        except IOError as e:
            self.fail("Couldn't load CSV-file!\n%s" % e)

    def test_save(self):
        try:
            self.model.saveCSV("")
        except IOError as e:
            self.fail("Couldn't save CSV-file!\n%s" % e)

    def test_replaceText(self):
        try:
            self.model.saveCSV("some;text;")
            text = self.model.loadCSV()
            assert text == "some;text;\n", "Replacing old text with 'some;text;' in CSV file failed!"
        except IOError as e:
            self.fail("Couldn't load CSV-file!\n%s" % e)

    def test_addText(self):
        try:
            added_text = "some;text;"
            old_text = self.model.loadCSV()
            self.model.saveCSV(old_text+added_text)
            new_text = self.model.loadCSV()
            self.assertTrue(new_text == old_text+added_text+"\n", "Replacing old text with 'some;text;' in CSV file failed!")
        except IOError as e:
            self.fail("Couldn't load CSV-file!\n%s" % e)

    def test_linebreaks(self):
        try:
            asserted_text = "some;\ntext;"
            added_text = "some;\n\n\n\n\ntext;"
            old_text = self.model.loadCSV()
            self.model.saveCSV(old_text+added_text)
            new_text = self.model.loadCSV()
            self.assertFalse(new_text == old_text+added_text, "Blank lines shouldn't be saved!")
            self.assertTrue(new_text == old_text+asserted_text+"\n",   "Blank lines shouldn't be saved!")
        except IOError as e:
            self.fail("Couldn't load CSV-file!\n%s" % e)

    def tearDown(self):
        try:
            self.model.saveCSV("")
        except IOError as e:
            self.fail("Couldn't clean CSV-file!\n%s" % e)


if __name__ == '__main__':
      unittest.main()