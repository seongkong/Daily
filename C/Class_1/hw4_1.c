#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX(X, Y) ((X) > (Y) ? (X) : (Y))
#define MAX_LEN 256

void AddBinaryString(char bin1[], char bin2[], char sum[]);
void ReverseString(char str[]);
int char2int(char c);
char int2char(int i);

int main() {
    char bin1[MAX_LEN];
    char bin2[MAX_LEN];
    char sum[MAX_LEN];
    
    printf("Input two binary numbers: ");
    scanf("%s %s", bin1, bin2);

    AddBinaryString(bin1, bin2, sum);
    
    printf("%s + %s = %s\n", bin1, bin2, sum);
    return 0;
}

void AddBinaryString(char bin1[], char bin2[], char sum[]) {
    // 자리 수 초기화
    int len1 = strlen(bin1);
    int len2 = strlen(bin2);
    int carry = 0, i, j, k = 0;

    // 이진수 뒤집기 (오른쪽에서 왼쪽으로 더하며 계산)
    ReverseString(bin1);
    ReverseString(bin2);

    // 이진수 덧셈 수행
    for (i = 0; i < MAX(len1, len2); i++) {
        int d1, d2;

        // i가 len1보다 작으면 d1을 bin1[i]로 설정하고, 아니면 0으로 설정
        if (i < len1) {
            d1 = char2int(bin1[i]);
        } else {
            d1 = 0;
        }

        // i가 len2보다 작으면 d2를 bin2[i]로 설정하고, 아니면 0으로 설정
        if (i < len2) {
            d2 = char2int(bin2[i]);
        } else {
            d2 = 0;
        }
        
        int s = d1 + d2 + carry;
        sum[k++] = int2char(s % 2); 
        carry = s / 2; 
    }
    
    sum[k] = '\0'; // 문자열의 끝

    // 원래대로 돌려놓기
    ReverseString(sum);
    ReverseString(bin1);
    ReverseString(bin2); 
}

void ReverseString(char str[]) {
    int len = strlen(str);
    for (int i = 0; i < len / 2; i++) {
        char temp = str[i];
        str[i] = str[len - i - 1];
        str[len - i - 1] = temp;
    }
}

int char2int(char c) {
    return c - '0';
}

char int2char(int i) {
    return '0' + i;
}
