char stack[10000];
int top=-1;
void push(char ch){
    stack[top+1]=ch;
    top++;
}
char  pop(){
    if (top==-1) {
        return '#';
    }

        char ch=stack[top];
        top--;
        return ch;
    
}
int match(char o,char c ){
    if (o=='(' && c==')') return 1;
    if(o=='{' && c=='}') return 1;
    if(o=='[' && c==']') return 1;
    return 0;
}
bool isValid(char* s) {
    top=-1;
    for(int i=0;s[i]!='\0';i++){
        if(s[i]=='(' || s[i]=='{' || s[i]=='['){
            push(s[i]);
        }
        else{
            char st=pop();
           if(st=='#' || match(st,s[i])==0 ) return 0;
        }
        
    }
   if(top==-1)  return 1;
   return 0;
}