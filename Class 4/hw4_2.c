#include <stdio.h>
#include <string.h>

void stringInsert(char str[], int p, char substr[]);
void stringDelete(char str[], int p, int n);

int main() {
    char text[256] = "abcdefg";

    // 초기 문자열 출력
    printf("text = \"%s\"\n", text);

    // 문자열 삽입 및 삭제 테스트
    stringInsert(text, 4, "123");
    printf("after stringInsert(text, 4, \"123\"), text = %s\n", text);

    stringDelete(text, 2, 2);
    printf("after stringDelete(text, 2, 2), text = %s\n", text);

    stringDelete(text, 5, 3);
    printf("after stringDelete(text, 5, 3), text = %s\n", text);

    stringInsert(text, 0, "ABCDE");
    printf("after stringInsert(text, 0, \"ABCDE\"), text = %s\n", text);

    stringDelete(text, 7, 4);
    printf("after stringDelete(text, 7, 4), text = %s\n", text);

    return 0;
}

// 문자열 삽입 함수
void stringInsert(char str[], int p, char substr[]) {
    int len1 = strlen(str);    // 원래 문자열의 길이
    int len2 = strlen(substr); // 삽입할 문자열의 길이

    // p가 원래 문자열의 길이보다 크면 p를 len1으로 설정
    if (p > len1) {
        p = len1;
    }

    // 뒤쪽 문자열을 이동하여 공간 확보
    for (int i = len1 - 1; i >= p; i--) {
        str[i + len2] = str[i];
    }

    // 삽입할 문자열 복사
    for (int i = 0; i < len2; i++) {
        str[p + i] = substr[i];
    }

    // 새로운 문자열의 끝에 NULL 문자 추가
    str[len1 + len2] = '\0';
}

// 문자열 삭제 함수
void stringDelete(char str[], int p, int n) {
    int len = strlen(str); // 원래 문자열의 길이

    // p + n이 문자열의 길이보다 크거나 같으면, p 위치부터 끝까지 삭제
    if (p + n >= len) {
        str[p] = '\0';
    } else {
        // p 위치부터 n만큼 문자열을 삭제하고 뒤쪽 문자열을 앞으로 이동
        for (int i = p; i + n < len; i++) {
            str[i] = str[i + n];
        }
        // 이동 후 남는 부분에 NULL 문자 추가
        str[len - n] = '\0';
    }
}
