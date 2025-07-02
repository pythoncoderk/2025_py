import re

def greet(name):
    message = f"こんにちは、{name}さん！"
    return message

def main():
    text = "My email is example@example.com"
    result = re.search(r"\w+@\w+\.\w+", text)  # ← ブレイクポイント①（標準ライブラリ）
    message = greet("太郎")                   # ← ブレイクポイント②（自作関数）
    print(result.group())
    print(message)

main()