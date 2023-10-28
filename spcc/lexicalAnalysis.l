%{
#include <stdio.h>
%}

%%
if|else|while   printf("KEYWORD: %s\n", yytext);
[-+*/=<>!]+     printf("OPERATOR: %s\n", yytext);
[0-9]+          printf("INTEGER: %s\n", yytext);
[a-zA-Z][a-zA-Z0-9]* printf("IDENTIFIER: %s\n", yytext);
[ \t\n]         /* ignore whitespace */
.               printf("UNKNOWN_TOKEN: %s\n", yytext);
%%
int yywrap() {}
int main()
{
    yylex();
    return 0;
}
