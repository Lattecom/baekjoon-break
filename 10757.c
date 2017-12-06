// 10757
#include <stdio.h>

int main(int argc, char const *argv[])
{
	char a[10001], b[10001];
	char c[10001] = {0};
	int t1, t2;
	int i,j,k;
	int temp, m, n;
	scanf("%s %s",a, b);

	t1=t2=1;
	i=j=0;
	k=0;
	while(t1 || t2){
		if(t1 && a[k] == 0){
			i = k;
			t1 = 0;
		}
		if(t2 && b[k] == 0){
			j = k;
			t2 = 0;
		}
		k++;
	}
	i--;
	j--;
	k = 0;
	while(!(i < 0 && j < 0 && c[k] == 0)){
		m = i >= 0 ? a[i] - 48 : 0;
		n = j >= 0 ? b[j] - 48 : 0;
		
		temp = c[k] + m + n;
		c[k] = temp % 10;
		c[k+1] = temp / 10;
		
		c[k] += 48;
		
		k++; i--; j--;
	}
	while(k>0){
		printf("%c", c[--k]);
	}
	return 0;
}