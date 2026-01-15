#import all needed modules here
import unittest
from app import add 

class TestHabitTracker(unittest.TestCase): 

#write all your tests below this line
    def test_interpret_score_high(self):
        self.assertEqual(interpret_score(12), "High" )
#write your test suite here, in the main() function 
def main():
    #call all your tets here, one on each line
    print("Starting tests suite...")

#please do not change the lines below
if __name__ == "__main__":
    main() 
