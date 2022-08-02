## 1. Semantic Tag

보기 중 콘텐츠의 의미를 명확히 하기 위해 HTML5에서 새롭게 추가된
시맨틱(semantic) 태그를 모두 고르시오.

> div,  header,  h1,  section,  footer,  a,  form,  span

- header, section,  footer


## 2. input Tag

아래 이미지와 같이 로그인 Form을 생성하는 HTML코드를 작성하시오. 
단, USERNAME 글자를 클릭하면 아이디를 입력하는 input에,
PWD 글자를 클릭하면 비밀번호를 입력하는 input에 focusing 되도록 하시오.


• USERNAME 글자 클릭시:

```html
<label for="username" class="form-label">USERNAME:</label>
<input type="text" name="username" id="username" autofocus>


```

• PWD 글자 클릭시:

```html
<label for="pwd" class="form-label">PWD:</label>
<input type="password" name="pwd" id="pwd">
```


## 3. 크기 단위

크기 단위 em은 요소에 지정된 상속된 사이즈나 기본 사이즈에 대해 상대적인 사이즈를
설정한다. 즉, 상속의 영향으로 사이즈가 의도치 않게 변경될 수 있는데 이를 예방하기
위해 HTML 최상위 요소의 사이즈를 기준으로 삼는 크기 단위는 무엇인가?

**rem**


## 4. 선택자

다음 예제를 통해 ‘자손 결합자’와 ‘자식 결합자’의 차이를 설명하시오.


```css
/* 자손 결합자 */
div p {
color: crimson;
}
/* 자식 결합자 */
div > p {
color: crimson;
}
```

- 자손 결합자는 자식, 손자 , 그 이후의 후손 모두를 선택하는 선택자이다.
- 자식 결합자는 자식만 선택하고 그 이후에 오는 후손들은 선택하지 않는 선택자이다.