from time import *
import random as r
def mis(test,ui):
  error=0
  for i in range(len(test)):
    try:
      if test[i]!=ui[i]:
        error+=1
    except:
        error+=1
  return error
def speed(ts,te,ui):
  td=te-ts
  tr=round(td,2)
  speeed=len(ui)/tr
  return round(speeed,2)
while True:
  print("*********** TYPING SPEED CALCULATOR ***************")
  c=int(input('''
  ARE YOU READY?
  1. YES
  2. NO
  ENTER YOUR CHOICE :'''))
  if c==1:
    print("\n\nWRITE THE GIVEN PARAGRAPH AND TRY TO MAKE ERRORS AS LESS AS POSSIBLE \n\n")
    test=["Paragraphs are the group of sentences combined together, about a certain topic.",
      " It is a very important form of writing as we write almost everything in paragraphs, be it an answer, essay, story, emails, etc.",
      "The purposes of the paragraph are to give information, to explain something, to tell a story, and to convince someone that our idea is right."
      ,"Paragraphs are blocks of textual content that segment out a larger piece of writing like stories, novels, articles, creative writing, or professional writing portions"]
    a=r.choice(test)

    print(a)
    t1=time()
    ui=input("\n\nENTER FROM HERE :")
    t2=time()
    print("TYPING SPEED :",speed(t1,t2,ui))
    print("ERRORS :",mis(a,ui))
  elif c==2:
    print("THANK YOU")
    break
  else:
    print("INVALID INPUT")
