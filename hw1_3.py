def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32
import unittest

class TestTemperatureConversion(unittest.TestCase):
    
    def test_celsius_to_fahrenheit(self):
        # 測試正常情況
        self.assertEqual(celsius_to_fahrenheit(0), 32)  # 0°C 應該轉為 32°F
        self.assertEqual(celsius_to_fahrenheit(100), 212)  # 100°C 應該轉為 212°F
        self.assertEqual(celsius_to_fahrenheit(-40), -40)  # -40°C 應該轉為 -40°F
        
        # 測試邊界情況
        self.assertEqual(celsius_to_fahrenheit(37), 98.6)  # 37°C 應該轉為 98.6°F
        
        # 測試小數
        self.assertAlmostEqual(celsius_to_fahrenheit(25.5), 77.9, places=1)  # 25.5°C 應該轉為約 77.9°F

if __name__ == '__main__':
    unittest.main()