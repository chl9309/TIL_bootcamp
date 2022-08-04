# HomeWork


## 1. Button 만들기
아래 Button을 만들기 위해 (a), (b)에 들어갈 알맞은 Components를 작성하시오.

```html
<button type="submit" class="bnt bnt-primary">Submit</button>
```



## 2. Navbar 만들기
아래 Navbar을 만들기 위해 (a), (b), (c)에 들어갈 알맞은 Components를 작성하시오.


```html
<nav class="navbar navbar-expand-lg navbar-expend bg-light ">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">
      <img src="#" alt="ssafy" width="70" height="30" class="d-inline-block align-top">
    </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDarkDropdown"
      aria-controls="navbarNavDarkDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarNavDropdown" role="button" data-bs-toggle="dropdown"
            aria-expanded="false">아침
          </a>
          <ul class="dropdown-menu dropdown-menu-light" aria-labelledby="navbarBreakfast">
            <li><a class="dropdown-item" href="#">오믈렛</a></li>
            <li><a class="dropdown-item" href="#">샌드위치</a></li>
            <li><a class="dropdown-item" href="#">팬케이크</a></li>
            <li><a class="dropdown-item" href="#">김밥</a></li>
            <li><a class="dropdown-item" href="#">주먹밥</a></li>
          </ul>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarLunch" role="button" data-bs-toggle="dropdown"
            aria-expanded="false">점심
          </a>
          <ul class="dropdown-menu dropdown-menu-light" aria-labelledby="navbarLunch">
            <li><a class="dropdown-item" href="#">샐러드</a></li>
            <li><a class="dropdown-item" href="#">떡볶이</a></li>
            <li><a class="dropdown-item" href="#">햄버거</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link active" href="#">저녁</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disable" href="#">야식</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
```
> (a) expand-lg light
> (b) navbar-nav me-auto mb-2 mb-lg-0
> (c) navbarNavDropdown




## 3. Pagination 만들기
아래 Pagination을 만들기 위해 (a), (b), (c)에 들어갈 알맞은 Components를 작성하시오.

```html
<nav aria-label="...">
  <ul class="pagination">
    <li class="page-item disabled">
      <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Prev</a>
    </li>
    <li class="page-item active" aria-current="page">
      <a class="page-link" href="#">1</a>
    </li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item">
      <a class="page-link" href="#">Next</a>
    </li>
  </ul>
</nav>
```
> (a) pagination
> (b) disabled
> (c) active