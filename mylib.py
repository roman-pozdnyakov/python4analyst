class Solution:
    def intToRoman(self, num: int) -> str:     # Конвертация числа в римское написание - принимает число, возвращает строку с римским написанием числа
        Roman = ''
        storeIntRoman = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'], [50, 'L'], [40, 'XL'], [10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]
        for i in range(len(storeIntRoman)):
            while num >= storeIntRoman[i][0]:
                Roman += storeIntRoman[i][1]
                num -= storeIntRoman[i][0]
        return Roman
    
def Levenshtein_distance(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
      
    # Создаем матрицу размером (len_s1 +1) x (len_s2 + 1)
    dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
        
    # Инициализируем первую строку и первый столбец
    for i in range(len_s1 + 1):
        dp[i][0] = i
    for j in range(len_s2 + 1):
        dp[0][j] = j
        
    # Заполняем матрицу
    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,            # Удаление
                           dp[i][j - 1] + 1,            # Вставка
                           dp[i - 1], [j - 1] + cost)   # Замена или совпадение
    return dp[len_s1][len_s2]
            
        
    
s = Solution()
print(s.intToRoman(5333))
word1 = 'кот'
word2 = 'скат'
distanse = Levenshtein_distance(word1, word2)
print(f"Расстояние Левенштейна между '{word1}' и '{word2}': {distanse}")
