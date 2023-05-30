## CRUD 과제 코드리뷰

리뷰어 : 김경민 님

[리뷰 notion](https://www.notion.so/Task3_-2e5b4ec5b8fe42128ccb3f168faf2761)

> 요약
> 1. Forms.py 파일에서 fields 작성 시 단일 원소를 가질 때에도 쉼표를 붙여주어야 한다.
> 2. urls.py 파일에서 오타
> 3. views.py 파일에서
>  * 필요한 import를 추가하지 않음
>  * request.method 오류. 올바른 HTTP 메소드를 사용하지 않음
>  * request.BLOG와 request.CATEGORY가 아니라 request.POST를 사용해야 form 데이터에 접근 할 수 있을 것이라고 생각됨.
>  * 일부 함수의 이름에 오타.


---


#### 리뷰 받기 전 회고
 - comment CRUD 빼먹음...😨
 - views.py에서 Tag에 대한 CRUD 빼먹음.
   그럼에도 불구하고 Tag에 대한 CRUD가 가능했던 이유?
   
    > Django의 Admin 기능을 통해 생성한 경우, Tag 모델에 대한 CURD 작업을 수행할 수 있었던 것 같습니다. Django의 Admin은 관리자용 인터페이스를 제공하며, 기본적으로 모든 모델에 대한 CURD 작업을 수행할 수 있도록 설정되어 있습니다.
    > Django의 Admin은 admin.py 파일을 통해 구성됩니다. admin.py 파일에서 Tag 모델에 대한 등록이 이루어져 있을 것으로 예상됩니다. 이렇게 등록된 모델은 관리자 인터페이스에서 해당 모델에 대한 CURD 작업을 수행할 수 있게 됩니다.
    > 아마도 Tag 모델에 대한 CURD 작업을 수행할 수 있었던 이유는 admin.py 파일에 Tag 모델을 등록한 것일 가능성이 큽니다. 이로 인해 Django의 Admin 기능을 통해 해당 모델을 관리할 수 있게 되었던 것입니다. -chat GPT
