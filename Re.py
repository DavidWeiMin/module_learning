import re 
class re_grammar():
    '''学习正则表达式'''
    
    def __init__(self,pattern,str):
        self.str = str
        self.set_pattern(pattern)
        self.re_function()

    def set_pattern(self,new_pattern):
        self.pattern = new_pattern
        
    def re_function(self):
        # print(re.match(self.pattern,self.str).group())    
        # print(self.r.search(self.str)+'\n')
        print(re.findall(self.pattern,self.str))
        # print(self.r.finditer(self.str)+'\n')
        # print(self.r.sub('戴',self.str)+'\n')
        # print(self.r.subn('戴',self.str)+'\n')

if __name__=='__main__':
    # 普通字符串与 raw 字符串的区别
    print('hello\nworld')
    print(r'hello\nworld')
    s = 'I am learning how to use regular expresion.\
    It\'s a little difficult for my first time to memorize all the grammars. \
    I have spent at least 2 hours. \
    123 23243 99549 7897dgjdg778 真的有点难记，什么.啊?啊[]啊aaaaaaa. \
    hhhhh asssx,dhjkashdkf dwadhh32urhfnkshdahflasfwghuwigh'
    r = re_grammar('aa+',s)
    re.match
