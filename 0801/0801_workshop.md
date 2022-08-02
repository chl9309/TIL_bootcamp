# Work Shop

## 1. <img> tag

<그림1>과 같은 폴더 구조가 있다. index.html에서 코드를 작성 중일 때, 
image 폴더 안의 my_ssafy.png를 보여주는 <img> tag를 작성하시오. 
단, 이미지가 제대로 출력되지 않을 때는 ssafy 문자열이 출력 되도록 작성하시오.





## 2. 파일 경로

위와 같이 경로를 (a)로 작성 할 시, github에 업로드 하거나 전체 폴더의 위치가
변경 되었을 때 이미지를 불러 올 수 없게 된다. 
이를 해결 하려면 이미지 경로를 (b)로 바꾸어 작성하면 된다. 
(a)와 (b)에 들어갈 경로를 작성하시오.



## 3. Hyper Link (1, 2번 문제 연계)

출력된 my_ssafy.png 이미지를 클릭하면 ssafy.com으로 이동하도록 코드를 수정하시오. 



## 4. 선택자

1. 아래의 코드를 작성하고 결과를 확인 하시오.

```html
<div id="ssafy">
<h2>어떻게 선택 될까?</h2>
<p>첫번째 단락</p>
<p>두번째 단락</p>
<p>세번째 단락</p>
<p>네번째 단락</p>
</div>
```

```html
#ssafy > p:nth-child(2) {
color: red;
}
```

2. nth-child를 nth-of-type으로 변경하고 결과를 확인 하시오.
```html
#ssafy > p:nth-of-type(2) {
color: blue;
}
```

3. 작성한 코드를 참고하여 nth-child()와 nth-of-type()의 차이점을 작성하시오