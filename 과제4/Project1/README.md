## CRUD 과제 코드리뷰

리뷰어 : 



### 리뷰 받기 전 회고
 - comment CRUD 빼먹음...😨
 - views.py에서 Tag에 대한 CRUD 빼먹음.
   그럼에도 불구하고 Tag에 대한 CRUD가 가능했던 이유?
   
    > Django의 Admin 기능을 통해 생성한 경우, Tag 모델에 대한 CURD 작업을 수행할 수 있었던 것 같습니다. Django의 Admin은 관리자용 인터페이스를 제공하며, 기본적으로 모든 모델에 대한 CURD 작업을 수행할 수 있도록 설정되어 있습니다.
    > Django의 Admin은 admin.py 파일을 통해 구성됩니다. admin.py 파일에서 Tag 모델에 대한 등록이 이루어져 있을 것으로 예상됩니다. 이렇게 등록된 모델은 관리자 인터페이스에서 해당 모델에 대한 CURD 작업을 수행할 수 있게 됩니다.
    > 아마도 Tag 모델에 대한 CURD 작업을 수행할 수 있었던 이유는 admin.py 파일에 Tag 모델을 등록한 것일 가능성이 큽니다. 이로 인해 Django의 Admin 기능을 통해 해당 모델을 관리할 수 있게 되었던 것입니다. -chat GPT
