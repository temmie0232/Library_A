

class Book:
    """本一冊の情報"""
    
    def __init__(self,title :str, author :str, isbn :int, status :bool = False):
        """本の状態を初期化

        Args:
            title (str): 本のタイトル
            author (str): 本の作者
            isbn (int): 本のisbnコード
            status (bool, optional): 本の貸出状態  True->貸出中  Fals->返却済み
            
            ////////
            Bookのインスタンスのisbnをキーとして、その他をバリューにするといい？
            ////////
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status


class Library:
    """図書館内の本を管理"""

    def __init__(self):
        """Bookのインスタンスを格納用のリスト初期化"""
        self.books = {}
    
    def find_book(self,isbn):
        """isbnから本を探す  (関数内のみで使用する)

        Args:
            isbn (bool): 本のisbn

        Returns:
            _type_: isbnが一致したBookのインスタンスを返す  (なければ None)
        """
        return self.books.get(isbn)

    def add_book(self,new_book :Book) -> None:
        """Bookのインスタンス名を受け取り、book_listに追加

        Args:
            new_book (Book): 蔵書リストに追加するBookクラスのインスタンス
        """
        if new_book.isbn not in self.books:
            self.books[new_book.isbn] = new_book
        else:
            print("この本(ISBN)はすでに登録されています。")    

    def lend_book(self,isbn :int) -> bool:
        """貸出 Bookのisbnを受け取り、Bookのstatusを変更

        Args:
            isbn (int): 貸出する本のisbn

        Returns:
            bool: 貸出<True>状態にし、処理成功を意味するTrueを返す。失敗したらFalseを返す。
        """
        book = self.find_book(isbn)
        if book and not book.status:    #もしBook(ISBN)が見つかり、貸し出されていない(False)なら
            book.status = True          #貸出状態に
            return True
        else:
            #if book -> find_bookからBookが見つかったら"貸出中"  見つからないなら"見つからない"
            print("この本は貸出中です。" if book else "この本(ISBN)は見つかりません")    
            return False
                
    def return_book(self,isbn :int) -> bool:
        """本の返却 isbnを受け取り、Bookのstatusを変更する。

        Args:
            isbn (int): 返却する本のisbn

        Returns:
            bool: 返却<False>状態にし、処理成功を意味するTrueを返す。失敗したらFalseを返す。
             
        """
        book = self.find_book(isbn)
        if book and book.status:    #もしBook(ISBN)が見つかり、貸し出されている(True)なら
            book.status = False          #返却済み状態に
            return True
        else:
            #if book -> find_bookからBookが見つかったら"貸出されていない"  見つからないなら"見つからない"
            print("この本は貸し出されていないです。" if book else "この本(ISBN)は見つかりません")    
            return False

    def search_book(self,isbn :int) -> Book | None:
        """本を検索  Bookのisbnを受け取り、Bookの情報を表示

        Args:
            isbn (int): 検索する本のisbn

        Returns:
            Book or None: 見つかったらそのBookのインスタンス、失敗したらNoneを返す。
        """
        book = self.find_book(isbn)
        if book:
            print("="*30)
            print(f"タイトル : {book.title}")
            print(f"著者     : {book.author}")
            print(f"isbn     : {book.isbn}")
            print(f"貸出状況  : {'貸出されている' if book.status else '貸出されていない'}")
            print("="*30)
            return book
        return None


# 以下は動作テスト用のプログム

if __name__ == "__main__":
     
    # Aという図書館を作成
    A = Library()

    # book1を登録
    book1 = Book("Python_code","Yuta",11110000)

    # Aという図書館にbook1という本を追加
    A.add_book(book1)

    # 貸出処理
    if A.lend_book(11110000):
        print("正常に処理しました")
    else:
        print("処理に失敗しました")

    # 返却処理
    if A.return_book(11110000):
        print("正常に処理しました")
    else:
        print("処理に失敗しました")

    # 本の検索
    A.search_book(11110000)