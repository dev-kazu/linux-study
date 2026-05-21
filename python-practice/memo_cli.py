memos = []

while True:
    print("\n=== Memo App ===")
    print("1: メモ追加")
    print("2: メモ表示")
    print("3: 終了")

    command = input("選択してください: ")

    if command == "1":
        memo = input("メモ内容: ")
        memos.append(memo)
        print("メモを追加しました")

    elif command == "2":
        print("\n--- メモ一覧 ---")

        if len(memos) == 0:
            print("メモがありません")
        else:
            for memo in memos:
                print(f"- {memo}")

    elif command == "3":
        print("終了します")
        break

    else:
        print("無効な入力です")