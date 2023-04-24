%{
    char name[50];
%}
%%
\n printf("Hello %s", name);
%%
int yywrap() {}
int main() {
    printf("Please enter your name: ");
    scanf("%s", name);
    yylex();
    return 0;
}