import datetime, os

os.remove("{{Your place of xip}}")

target_cookie = "{{your place of pkl}}"

if target_cookie in os.listdir("{{your place of Instapy Folder}}"):
    time = os.path.getctime(target_cookie)
    target = datetime.datetime.fromtimestamp(time)
    now = datetime.datetime.today()# 現在の日付を取得
    if (now - target).days >= 2: # 2日以上経過している場合は削除
        os.remove(target_cookie)
        print("Cookie deleted.")
else: print("Can't find or still new cookie")
