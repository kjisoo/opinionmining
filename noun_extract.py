# -*- coding: utf-8 -*-

from collections import Counter
from konlpy.tag import Hannanum, Kkma, Komoran, Twitter

example_text = '''
애플 아이폰7·7+ 공개···韓 1차 출시국서 제외

美등 1차 출시국서 9일 예약주문···16일 출시
방수·방진 아이폰 시리즈 최초 탑재
카메라 기능 강화···홈버튼은 사라져


애플이 7일(현지시간) 미국 샌프란시스코 빌 그레이엄 시빅 오디토리엄에서 공개한 아이폰7./사진=애플 홈페이지
애플의 신제품 스마트폰 아이폰7과 아이폰7플러스가 7일(현지시간) 샌프란시스코 빌 그레이엄 시빅 오디토리엄에서 공개됐다.

미국을 포함한 1차 출시국에서 9일부터 예약판매를 시작, 오는 16일 시판된다. 한국은 이번에도 1~3차 출시국에서 제외 돼 오는 10월 초에나 사용할 수 있을 것으로 보인다.

이날 공개된 아이폰의 가장 큰 특징은 카메라 성능을 대폭 높였다는 점이다. 두 제품의 카메라 화소 수는 1,200만으로, 렌즈가 f/1.8로 더 밝고 LED가 4개 달린 트루톤 플래시가 포함됐다. 전면카메라로는 700만 화소급 새 모듈이 들어갔다. 화면 크기가 4.7인치인 아이폰 7의 카메라에는 지난해까지 대화면(5.5인치) 모델에만 탑재됐던 ‘광학적 이미지 안정화’(OIS) 기능이 추가됐다. 새 대화면 모델인 아이폰 7 플러스는 표준적 와이드 렌즈와 56mm 텔레포토 렌즈가 함께 달린 듀얼 카메라가 탑재됐다. 이를 통해 초점거리를 조절하며, 최대 2배까지 광학줌도 가능하다. 아이폰 시리즈 최초로 방수·방진 기능을 갖춘 점도 눈에 띈다. 최근 출시된 삼성전자의 갤럭시노트7와 같이 이제 물울 쏟거나 먼지가 많은 곳에서도 견뎌낼 수 있다. 

저장 용량은 지난해 출시된 아이폰 6s·6s 플러스의 2배인 32GB, 128GB, 256GB로 늘었다. 가격은 최저용량(32GB) 모델 기준으로 아이폰 7은 649달러(약 70만원), 아이폰 7 플러스는 769달러(약 84만원)로 작년과 동일하다. 색깔은 실버, 골드, 로즈골드, 블랙(무광 검정), 제트블랙(유광 검정) 등 5종류다. 제트블랙의 경우 32GB는 선택할 수 없다. 디자인 측면에서는 ‘홈 버튼’과 3.5mm 이어폰 잭이 처음으로 없어지고 각각 지문인식 센서와 라이트닝 커넥터로 대체됐다. 이에 따라 아이폰에 기본으로 포함되는 이어폰인 ‘애플 이어팟’은 연결 단자가 기존의 3.5mm에서 라이트닝 커넥터로 바뀐다. 

1차 출시국은 호주와 오스트리아, 벨기에, 캐나다, 중국, 덴마크, 핀란드, 프랑스, 독일, 홍콩, 아일랜드, 이탈리아, 일본, 룩셈부르크, 멕시코, 네덜란드, 뉴질랜드, 노르웨이, 포르투갈, 푸에르토리코, 싱가포르, 스페인, 스웨덴, 스위스, 대만, 아랍에미리트연합(UAE), 영국, 미국령버진제도, 미국이다. 23일부터는 2차 출시국인 안도라와 바레인, 보스니아헤르체고비나, 불가리아, 크로아티아, 키프로스, 체코, 에스토니아, 라트비아, 리히텐슈타인, 리투아니아, 몰디브, 몰타, 모나코, 폴란드, 카타르, 루마니아, 러시아, 사우디아라비아, 슬로바키아, 슬로베니아에 판매된다. 한국 출시 계획은 아직 알려지지 않았다.

'''

#
#   By default:
#       maximum number of tags is set as 100
#       library type is set as 1
#           1 : Hannanum
#           2 : Kkma
#           3 : Komoran
#           4 : Twitter
#       returns in format [{'noun':n, 'count':c}] in descending order of size.
#
#   TODO:
#       - filter out words from custom defined library, such as '것', '수', etc.
#       - detect language and use corresponding noun-extracting technology.
#           - currently only supports Korean.
#
def getNouns(text = example_text, numOfTags=100, libType=1):
    if libType == 1:
        koreanLibrary = Hannanum()
    elif libType == 2:
        koreanLibrary = Kkma()
    elif libType == 3:
        koreanLibrary = Komoran()
    else:
        koreanLibrary = Twitter()
    nouns = koreanLibrary.nouns(text)
    countedNouns = Counter(nouns)
    return [{'noun':n, 'count':c} for n, c in countedNouns.most_common(numOfTags)]