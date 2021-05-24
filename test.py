from datetime import datetime

#現在の日付
today = datetime.today()
#生年月日の入力
birthday = datetime(2020,1,1)

#経過日数計算
ans = today - birthday
print(ans.days)
