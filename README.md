# README.md

## 프로젝트 구조

```
/clean-architecture(root)
|    +-- /app
|        +-- /application
|            +-- /interfaces
|                +-- reporitory.py	
|            +-- /services
|                +-- product.py
|                +-- user.py
|	
|			+-- /controller
|                +-- product.py
|                +-- user.py
|			
|			+-- /domain
|                +-- entity.py
|			
|			+-- /infrastructure
|                +-- /database
|                    +-- orm.py
|                    +-- /repository
|                        +-- product.py
|                        +-- user.py
|
|                    +-- /fastapi
|                        +-- main.py
|
+-- /tests
            +-- fakes.py
            +-- test_api.py
            +-- test_repository.py
            +-- test_service.py
```

## 의존성 다이어그램
![image]https://user-images.githubusercontent.com/55076919/149782245-ca930a25-fc71-4d65-b3ae-3b5ee893860b.png