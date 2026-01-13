#import all needed modules here
import unittest

#write all your tests below this line

class TestHabitTracker(unittest.TestCase):
    def test_interpret_score_high(self):
        from app import interpret_score
        self.assertEqual(interpret_score(5), "High adherence")

    def test_interpret_score_moderate(self):
        from app import interpret_score
        self.assertEqual(interpret_score(3), "Moderate adherence")

    def test_interpret_score_low(self):
        from app import interpret_score
        self.assertEqual(interpret_score(2), "Low adherence")

#write your test suite here, in the main() function
def main():
    #call all your tets here, one on each line
    print("Starting tests suite...")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHabitTracker)
    unittest.TextTestRunner().run(suite)
    
#please do not change the lines below
if __name__ == "__main__":
    main()
