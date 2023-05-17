## models.py 작성 과제 코드리뷰

리뷰어 : 서민지 님


1. 존재해야하는 모델들을 전부 잘 작성해주신 것 같아요!다만, Post와 Comment 모델이 이미 블로그의 게시물과 댓글을 나타내는 기능을 가지고 있기에, FreePost와 FreeComment 모델과 기능이 중복된다고 생각되어 제거를 하셔도 좋을 것 같습니다!
	-> 수정 완료
2. 몇가지 오타가 있는 부분들이 있어서 알려드려요!
  Post 모델에서 author 필드의 on_delete=models.CASECADE 에 오타가 있어서 on_delete=models.CASCADE 로 수정해주셔야할 것 같아요!그리고 Post 모델에서 category 필드의      on_delet=models.CASCADE 에도 오타가 있어서 on_delete=models.CASCADE 로 수정해주셔야할 것 같아요!
 ->수정완료
3. 게시글 모델에 image 필드를 추가하신게 참신한 것 같아요!
4. tag를 다대다 관계에 대한 연결테이블로 설정하기 위해 PostTag 모델을 추가하신 점도 참신한 것 같습니다!
다대다 관계에 대한 연결테이블로 설정하기 위해서 Post 모델안에서 ManyToManyField 를 사용하실 수 있는 것도 참고하시면 좋을 것 같아요! -> 확인 및 수정 완료


- 참고한 링크

다대다관계 : https://fmhelp.filemaker.com/help/16/fmp/ko/index.html#page/FMP_Help/many-to-many-relationships.html

https://nachwon.github.io/django-5-database/

https://ikkison.tistory.com/37
