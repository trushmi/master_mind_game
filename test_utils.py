import unittest

from utils import(
    is_guess_number_valid,
    is_user_difficulty_level_valid,
    is_numbers_the_same,
    get_correct_location_count,
    get_correct_number_count,
)

class TestUtils(unittest.TestCase):
    
    def test_is_guess_number_valid_success(self):
        self.assertTrue(is_guess_number_valid("1234", 4))
        self.assertTrue(is_guess_number_valid("34343", 5))

    def test_is_guess_number_valid_success_failure(self): 
        self.assertFalse(is_guess_number_valid("1234", 6)) 
        self.assertFalse(is_guess_number_valid("14", 4))
        self.assertFalse(is_guess_number_valid("0", 4))
        self.assertFalse(is_guess_number_valid("141b", 4))  

    def test_is_user_difficulty_level_valid_success(self):
        self.assertTrue(is_user_difficulty_level_valid("easy"))  
        self.assertTrue(is_user_difficulty_level_valid("medium"))  
        self.assertTrue(is_user_difficulty_level_valid("hard"))  

    def test_is_user_difficulty_level_valid_failure(self):
        self.assertFalse(is_user_difficulty_level_valid("MEDIUM"))
        self.assertFalse(is_user_difficulty_level_valid("Hard"))
        self.assertFalse(is_user_difficulty_level_valid("eas"))
        self.assertFalse(is_user_difficulty_level_valid("har"))
        self.assertFalse(is_user_difficulty_level_valid("difficult"))

    def test_is_numbers_the_same(self):
        self.assertTrue(is_numbers_the_same("6666", "6666")) 
        self.assertFalse(is_numbers_the_same("6666","6665")) 
        
    def test_get_correct_location_count_success(self):
        result = get_correct_location_count("6543", "6543")  
        self.assertEqual(result, 4)
        
    def test_get_correct_location_count_failure(self):
        result = get_correct_location_count("2010", "1233")  
        self.assertEqual(result, 0) 

    def test_get_correct_number_count_success(self):
        result = get_correct_number_count("7654", "7654")  
        self.assertEqual(result, 4) 
    
    def test_get_correct_number_count_failure(self):
        result = get_correct_number_count("4376", "1111")  
        self.assertEqual(result, 0)



if __name__ == '__main__':
    unittest.main()