def rec(n):
	if n==0:
		return 3
	print("printing value of", n)
	n-=1
	rec(n)
