from random import randint
print("Instructions>>\n*Choose a Number Between One to Hundred.\n*If chosen number is close to the number 'WARM' will be printed else 'COLD' will be printed.\n*If the subsequent number entered is even more closer compared to previous number 'WARMER' will be printed else 'COLDER'.")
ans=randint(1,100)
lst_inputs=[0]
while True:
  n=int(input("Please Enter a number"))
  if n>100 or n<0:
    print("OUT OF BOUNDS,PLEASE TRY AGAIN!!")
    continue
  if n==ans:
    break
  lst_inputs.append(n)
  if lst_inputs[-2]:
    if abs(n-ans)<abs(lst_inputs[-2]-ans):
      print("WARMER")
    else:
      print("COLDER")
     
  else:
     if abs(n-ans)<10:
        print("WARM")
     else:
       print("Cold") 
print("Hooray!! You found the number {} and the no of tries you took were {}".format(ans,len(lst_inputs)))