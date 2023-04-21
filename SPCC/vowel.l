%{    
%}
%%
[aeiouAEIOU] printf("Vowel\n");
. printf("Constant\n");
%%
int yywrap() {}
int main() {
    yylex();
    return 0;
}