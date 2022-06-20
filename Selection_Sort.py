# 配列の定義と入力
N=int(input('数字の数は？'))
nums=[]
for i in range(0,N,1):
  nums.append(int(input()))

# ソート
idx=0
while(idx<len(nums)):
  min=nums[idx]
  min_idx=idx
  for i in range(idx,len(nums),1):
    if(min>nums[i]):
      min=nums[i]
      min_idx=i

  # 入れ替え部分
  box=nums[idx]
  nums[idx]=min
  nums[min_idx]=box

  idx+=1

print(nums)
