VOWELS=('a,e,i,o,u')
consonant=('b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z')
a=input("Enter the word:")
if a in VOWELS:
	print("Vowel")
elif a in consonant:
	print("Consonant")
else:
	print("invalid")
