# 配列の定義と入力
N=int(input("数字の数は？"))
nums=[]
for i in range(0,N,1):
  nums.append(int(input()))

# ソート
flag=0
while(flag==0):
  flag=1
  for i in range(0,len(nums)-1,1):
    if(nums[i]>nums[i+1]):

      # 入れ替え部分
      box=nums[i]
      nums[i]=nums[i+1]
      nums[i+1]=box

      flag=0
      
print(nums)
