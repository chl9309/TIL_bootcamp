# 브랜치로 분업하기!! (분업 방법)
1. gitlab에 새 프로젝트를 만들어서 내용물 커밋
2. git 
 하는법 써주세요

# axios로 API 받아오기!!!

1. `.env.local` 파일 만들기
2. `VUE_APP_API_KEY=2a5c5c8d29f6223b7278c7de5b7116b1` 등록!
3. axios 요청을 할 vue의 script 태그 안에 import 받아오기 `import axios from 'axios'`
4. axios 요청 보내기 (method, url, params)
5. 이 때, params에 사용할 key는 api 문서에 이름이 제시되어 있습니다.
6. 각 vue마다 받아오기 위해 다른 방법도 있는데 잘 모르겠어서 그냥 vue마다 axios 요청 했습니다.
``` vue
<script>
import axios from 'axios'
import MovieCard from '@/components/MovieCard.vue'
const API_KEY = process.env.VUE_APP_API_KEY

export default {
  name:'MovieView',
  components:{
    MovieCard,
  },
  data() {
    return {
      movies : []
    }
  },
  methods: {
    get_top_reated_movies() {
      const params = {
        api_key: API_KEY,
        language: 'ko-KR',
        page: 1,
      }
      axios({
        method: 'get',
        url: 'https://api.themoviedb.org/3/movie/top_rated',
        params
      })
      .then(res => {
        console.log(res)
        this.movies = res.data.results
      })
      .catch(err => console.log(err))
      },
  },
  created(){
    this.get_top_reated_movies()
  }
}

</script>
```

# 머지 관련 (홍준)







# 리뷰 만들고 삭제하기 (홍준)

어쩌구~


# 디자인 구성 (보라)
어저ㅏ구~

# 랜덤 추천 알고리즘 (수민)
어쩌구~

# 느낀점
어쩌구~

