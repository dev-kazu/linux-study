FILE_NAME = "memo.txt"

while True:
    print("\n=== Memo File App ===")
    print("1: メモ追加")
    print("2: メモ表示")
    print("3: 終了")

    command = input("選択してください: ")

    if command == "1":
        memo = input("メモ内容: ")

        with open(FILE_NAME, "a") as file:
            file.write(memo + "\n")

        print("保存しました")

    elif command == "2":
        print("\n--- メモ一覧 ---")

        try:
            with open(FILE_NAME, "r") as file:
                content = file.read()

                if content == "":
                    print("メモがありません")
                else:
                    print(content)

        except FileNotFoundError:
            print("まだメモがありません")

    elif command == "3":
        print("終了します")
        break

    else:
        print("無効な入力です")