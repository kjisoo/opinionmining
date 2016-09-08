# -*- coding: utf-8 -*-

import noun_extract as n

test_text = '''
아이폰 7은 터지지 않을 것입니다.  
오늘 날씨는 매우 좋지 않습니다. 
I have a meeting with the Wall Street Journal later today.
오늘은 외주를 뛰느라 많이 바쁠 것 같습니다.  
섬바디 헬프미.
외래어는 어떻게 취급하나요?  
노래나 들으면서 해야겠다.
'''

nouns = n.getNouns(test_text)
print(nouns)