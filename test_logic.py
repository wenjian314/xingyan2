"""测试核心编解码逻辑"""
import sys
sys.path.insert(0, '/data/workspace')

# 从 main.py 中提取核心逻辑进行测试
import re
from pypinyin import pinyin, Style

# 默认对照表
DEFAULT_TABLE = {
    "A": "迷~", "B": "~迷迷迷", "C": "~迷~迷", "D": "~迷迷", "E": "迷",
    "F": "迷迷~迷", "G": "~~迷", "H": "迷迷迷迷", "I": "迷迷", "J": "迷~~~",
    "K": "~迷~", "L": "迷~迷迷", "M": "~~", "N": "~迷", "O": "~~~",
    "P": "迷~~迷", "Q": "~~迷~", "R": "迷~迷", "S": "迷迷迷", "T": "~",
    "U": "迷迷~", "V": "迷迷迷~", "W": "迷~~", "X": "~迷迷~", "Y": "~迷~~",
    "Z": "~~迷迷",
    "0": "~~~~~", "1": "迷~~~~", "2": "迷迷~~~", "3": "迷迷迷~~",
    "4": "迷迷迷迷~", "5": "迷迷迷迷迷", "6": "~迷迷迷迷", "7": "~~迷迷迷",
    "8": "~~~迷迷", "9": "~~~~迷",
}


class MorseCodec:
    def __init__(self, mapping=None):
        self.set_mapping(DEFAULT_TABLE if mapping is None else mapping)

    def set_mapping(self, mapping):
        self._fwd = {k.upper(): v for k, v in mapping.items()}
        self._rev = {}
        for ch, code in self._fwd.items():
            self._rev[code] = ch

    def to_morse(self, text):
        text = text.upper()
        words = re.split(r"\s+", text)
        out_words = []
        for word in words:
            if not word:
                continue
            codes = []
            for ch in word:
                if ch in self._fwd:
                    codes.append(self._fwd[ch])
                else:
                    codes.append("?")
            out_words.append(" ".join(codes))
        return "  ".join(out_words)

    def from_morse(self, morse):
        morse = morse.strip()
        raw_words = re.split(r"\s{2,}", morse)
        result = []
        for raw in raw_words:
            raw = raw.strip()
            if not raw:
                continue
            chars = raw.split(" ")
            word = "".join(self._rev.get(c.strip(), "?") for c in chars if c.strip())
            result.append(word)
        return " ".join(result)

    def text_to_morse_via_pinyin(self, chinese_text):
        py_list = pinyin(chinese_text, style=Style.NORMAL)
        pinyin_str = " ".join([p[0] for p in py_list])
        return self.to_morse(pinyin_str)


codec = MorseCodec()

# 测试1：LOVE YOU 示例
print("=" * 50)
print("测试1: LOVE YOU → 迷语")
result = codec.to_morse("LOVE YOU")
print(f"输入: LOVE YOU")
print(f"输出: {result}")
expected = "迷~迷迷 ~~~ 迷迷迷~ 迷  ~迷~~ ~~~ 迷迷~"
print(f"期望: {expected}")
print(f"✅ 通过" if result == expected else f"❌ 不匹配")
print()

# 测试2：迷语 → LOVE YOU
print("=" * 50)
print("测试2: 迷语 → LOVE YOU")
result = codec.from_morse("迷~迷迷 ~~~ 迷迷迷~ 迷  ~迷~~ ~~~ 迷迷~")
print(f"输出: {result}")
print(f"期望: LOVE YOU")
print(f"✅ 通过" if result == "LOVE YOU" else f"❌ 不匹配")
print()

# 测试3：中文 → 拼音 → 迷语
print("=" * 50)
print("测试3: 中文 → 拼音 → 迷语")
result = codec.text_to_morse_via_pinyin("你好世界")
print(f"输入: 你好世界")
print(f"拼音: ni hao shi jie")
print(f"输出: {result}")
print()

# 测试4：完整字母表
print("=" * 50)
print("测试4: 完整字母表 A-Z → 迷语 → A-Z")
text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
morse = codec.to_morse(text)
back = codec.from_morse(morse)
print(f"原文: {text}")
print(f"迷语: {morse}")
print(f"回译: {back}")
print(f"✅ 通过" if back == text else f"❌ 不匹配")
print()

# 测试5：数字
print("=" * 50)
print("测试5: 数字 0-9")
text = "0123456789"
morse = codec.to_morse(text)
back = codec.from_morse(morse)
print(f"原文: {text}")
print(f"迷语: {morse}")
print(f"回译: {back}")
print(f"✅ 通过" if back == text else f"❌ 不匹配")
