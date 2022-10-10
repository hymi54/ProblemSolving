class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        lowered = []
        symbol = ["!", "?", "'", ",", ";", ".", " "]
        # lowered 리스트에 특수문자 제거 후 소문자로 변환한 단어 append
        for s in symbol:
            while s in paragraph:
                paragraph = paragraph.replace(s, '*')
        for word in paragraph.split('*'):
            lowered.append(word.lower())

        # 단어 빈도수 높은 순으로 정렬
        while "" in lowered:
            lowered.remove("")
        result = sorted(lowered, key=lowered.count, reverse=True)

        # 빈도수 높은 단어부터 banned에 없는지 확인해 반환
        for lowered_word in result:
            if lowered_word not in banned:
                return lowered_word