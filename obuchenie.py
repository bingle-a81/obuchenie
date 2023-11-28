class RenderList:
    def __init__(self,type_list,):
        if type_list =='ol':
            self.type_list = 'ol'
        else:
            self.type_list='ul'

    def __call__(self, lst:list) -> str:
        return f'<{self.type_list}>'+'\n'+'\n'.join('<li>'+x+'</li>' for x in lst )+f'\n</{self.type_list}>'
    
lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)    
print(html)
                

