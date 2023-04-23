%{   
%}
%%
[0-9]+ printf("The string entered is a number.\n");
[a-zA-z]+ printf("The string entered is a word.\n");
[a-zA-z0-9]+ printf("The string entered is a combination of word and number.\n");
%%
int yywrap() {}
int main() {
    yylex();
    return 0;
}
