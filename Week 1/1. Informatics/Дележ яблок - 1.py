n = int(input())
k = int(input())

g = k/n;
   s = k - (g*n);
t = (k - s)/n;

if k % n == 0:
	return g
elif k % n != 0:
	return t 