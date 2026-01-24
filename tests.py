#import all needed modules here
import unittest
from app import add 

class TestHabitTracker(unittest.TestCase): 

#write all your tests below this line
    def test_interpret_score_high(self):
        from app import interpret_score
        self.assertEqual(interpret_score(12), "High" )

    def test_interpret_score_moderate(self):
        from app import interpret_score 
        self.assertEqual(interpret_score(11), "Moderate")
    
    def test_interpret_score_low(self):
        from app import interpret_score 
        self.assertEqual(interpret_score(2), "Low") 

#write your test suite here, in the main() function 
def main():
    #call all your tets here, one on each line
    print("Starting tests suite...")

    suite = unittest.TestLoader().loadTestsFromTestCase(TestHabitTracker)
    unittest.TextTestRunner().run(suite) 
#please do not change the lines below
if __name__ == "__main__":
    main() 
