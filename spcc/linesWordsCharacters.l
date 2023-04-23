%{
    #include<stdio.h>
    int lines = 0, words = 0, chars = 0, spaces = 0;
%}
%%
[\n] {lines++; chars += yyleng;}
[ \t] {spaces++; chars += yyleng;}
[^\t\n ]+ {words++; chars+= yyleng;}
%%
int main() {
    printf("Enter the text:\n");
    yylex();
    printf("\nNumber of words: %d\n", words);
    printf("Number of characters: %d\n", chars - lines - spaces);
    printf("Number of lines: %d\n", lines);
    printf("Number of spaces: %d\n", spaces);
}

int yywrap() {
    return 1;
}