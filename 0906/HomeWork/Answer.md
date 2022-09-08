# 04_HomeWork

### T/F

1. ModelForm을 사용할 때 Meta 클래스의 model 변수는 반드시 작성해야 한다.
2. ModelForm을 사용할 때 사용자의 입력을 위해 페이지에 렌더링 되는 input element의 속성은 Django에서 제공 해주는 대로만 사용해야 한다.
3. 화면에 나타나는 각 element 위치는 html에서 form.as_p()를 사용하지 않고, 직접 위치시킬 수 있다.
4. 다음 빈칸 (a) ~ (d) 에 적합한 코드를 작성하시오.



### Form

```python
from django import __(a)__
from .models import Article


class ArticleForm(__(b)__):
    
    class Meta:
        model = __(c)__
        __(d)__ = '__all__'
```

