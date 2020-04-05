def findDuplicite(arr):
  tortoise = arr[0]
  hare = arr[0]
  while True:
    tortoise = arr[tortoise]
    hare = arr[arr[hare]]

    if hare == tortoise:
      if arr[0] == hare:
        count = 0
        for n in arr:
          if n == arr[0]:
            count += 1
            if count > 1:
              break
        if count == 1:
          return;
      break
  
  p1 = arr[0]
  p2 = tortoise

  while p1 != p2:
    p1 = arr[p1]
    p2 = arr[p2]
  
  print("Result: ", p1)


findDuplicite([5, 1, 2, 3, 4 ,5,6,7])