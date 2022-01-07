from app.infrastructure.database.orm import db, UserModel, ProductModel

if __name__ == "__main__":
    db.init(database="database.db")
    db.connect()

    # 초기화
    UserModel.create_table()
    ProductModel.create_table()
    ProductModel.bulk_create([
        ProductModel(id=1, name="키보드", price=10000),
        ProductModel(id=2, name="모니터", price=20000),
        ProductModel(id=3, name="마우스", price=30000)
    ])

    p1 = ProductModel(id=1, name="키보드", price=10000)
    p2 = ProductModel(id=2, name="모니터", price=20000)
    p3 = ProductModel(id=3, name="마우스", price=30000)

    ProductModel.save(p1)
    ProductModel.save(p2)
    ProductModel.save(p3)

    print("Product 생성이 완료")
