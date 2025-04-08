class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        k = celsius + 273.15000
        m = celsius * 1.80 +32.0000
        return [k, m]
        