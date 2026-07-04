'''
    某社区图书馆需要开发一个简单的图书管理系统。
    系统需要支持会员登录、图书借阅、图书归还等功能。
    系统中有两种类型的会员︰
    普通会员和VIP会员，他们的借书权限不同。
    你需要使用面向对象编程的思想，
    设计并实现这个图书管理系统。
    ==> 核心功能:
        1. 会员登录:会员通过卡号和密码登录系统
        2. 借书:会员可以借阅库存中有余量的图书
        3. 还书:会员可以归还借阅的图书
        4. 查看我的借阅:展示当前会员已经借阅的图书列表5．退出系统
    ==> 借阅规则:
        1. 普通会员最多可借3本
        2. VIP会员最多可借6+VIP等级本(VIP等级，默认为1)
    ==> 注意:
        1. 登录成功（卡号和密码均正确)后，才可以访问该系统
        2. 图书库存不足，或当前会员借书数量达到最大借书数量，不能再借新书

'''

# def show_menu():
#     print('-'*30)
#     print('-----图书管理系统启动成功-----')
#     if not L.login_status:
#         print('当前未登录')
#         print('请选择要进行的操作：')
#         print('     1. 注册:')
#         print('     2. 登录:')
#         print('     3. 退出系统:')
#     else:
#         level = L.user.level
#         if level == 0:
#             member_type = '普通'
#             count = 3
#         else:
#             member_type = f'VIP:{level}'
#             count = level + 6
#         print(f'用户({member_type})已登录:    已借阅/最大借阅({L.user.borrowed_books_count}/{count})')
#         print('请选择要进行的操作：')
#         print('     0. 借书:')
#         print('     1. 还书:')
#         print('     2. 查看我的借阅:')
#         print('     3. 退出系统:')
#         print('     4. 登出:')
#         print('     5. 查看图书库存:')
#
#
# def register():
#     register_active = True
#     while (register_active):
#         print('--------会员注册--------')
#         print('注册成功自动登录')
#         input_card = input('请输入会员号：')
#         input_password = input('请输入密码：')
#         if input_card in L.user_account:
#             cmd = input('会员号已存在，返回登陆界面输入:1,其他键继续注册')
#             if cmd == '1':
#                 register_active = False
#         else:
#             L.user_account[input_card] = Member(input_card, input_password)
#             print('注册成功')
#             L.login_status = True
#             L.user = L.user_account[input_card]
#             register_active = False
#             print('已登录')
#
#
# def login():
#     print('--------会员登录--------')
#     input_card = input('请输入会员号：')
#     input_password = input('请输入密码：')
#     if input_card in L.user_account and L.user_account[input_card].password == input_password:
#         L.login_status = True
#         L.user = L.user_account[input_card]
#         print('登录成功')
#     else:
#         L.login_status = False
#         print('登录失败')
#
#
# def borrow_book():
#     borrow_active = True
#     while (borrow_active):
#         print('--------借阅图书--------')
#         if L.user.level == 0:
#             max_borrow = 3
#         else:
#             max_borrow = 6 + L.user.level
#         user_borrowed = L.user.borrowed_books_count
#         print(f'您的最大借阅数量为{max_borrow}, 已借阅{user_borrowed}本')
#         if user_borrowed >= max_borrow:
#             print('已借阅数量已达最大借阅数量,请还书后再借阅')
#             return
#         print(f'您还可以借阅{max_borrow - user_borrowed}本')
#         # 借阅图书
#         book_name = input('请输入图书名称：')
#         book_count = int(input('请输入借阅数量：'))
#
#         if book_name not in L.books:
#             print('图书不存在')
#             return
#         elif L.books[book_name] < book_count:
#             print(f'图书库存不足,当前库存为{L.books[book_name]}本')
#             return
#         elif book_count > max_borrow - user_borrowed:
#             print(f'您只能借阅{max_borrow - user_borrowed}本')
#             return
#         else:
#             L.user.borrowed_books_count += book_count
#             if book_name not in L.user.borrowed_books:
#                 L.user.borrowed_books[book_name] = book_count
#             else:
#                 L.user.borrowed_books[book_name] += book_count
#             L.books[book_name] -= book_count
#             print('借阅成功')
#             print(f'您已借阅{book_count}本{book_name}')
#             borrow_active = False
#
#
# def return_book():
#     return_active = True
#     while (return_active):
#         print('--------归还图书--------')
#         if L.user.borrowed_books_count == 0:
#             print('您未借阅任何图书,无需还书')
#             return
#         # 还书图书
#         book_name = input('请输入图书名称：')
#         book_count = int(input('请输入还书数量：'))
#         if book_name not in L.user.borrowed_books or book_count > L.user.borrowed_books[book_name]:
#             print('还书信息错误或还书数量超出借阅数量')
#             return
#         else:
#             L.user.borrowed_books_count -= book_count
#             L.user.borrowed_books[book_name] -= book_count
#             L.books[book_name] += book_count
#             print('还书成功')
#             print(f'您已还书{book_count}本{book_name}')
#             print("继续还书请输入:1,其他键结束")
#             cmd = input('请输入您的选择：')
#             if cmd != '1':
#                 return_active = False
#
#
# def show_my_borrowed():
#     print('--------查看我的借阅--------')
#     if L.user.borrowed_books_count == 0:
#         print('您未借阅任何图书')
#         return
#
#     print(f'您已借阅图书如下：')
#     for x in L.user.borrowed_books:
#         if L.user.borrowed_books[x] > 0:
#             print(f'{x}: {L.user.borrowed_books[x]}本')
#             pass
#
#
# def logout():
#     L.login_status = False
#     L.user = None
#     print('已登出')
#
# def show_library():
#     for x in L.books:
#         print(f'{x}: {L.books[x]}本')
#     input('图书库存显示完成,输入任意键返回')


class Member:
    def __init__(self, card: str, password: str, level: int = 0):
        self.card = card
        self.password = password
        self.level = int(level)
        self.borrowed_books = {}
        self.borrowed_books_count = 0


class Library:
    def __init__(self, login_status: bool = False, user_account: dict = None, user: Member = None, books: dict = None, active: bool = True):
        self.login_status = login_status  # 登录状态
        self.user_account = {} if user_account is None else user_account  # 会员账号字典
        self.user = user  # 当前登录用户
        self.books = {} if not books is None else books  # 图书库存字典
        self.active = active  # 系统是否运行中

    def show_menu(self):
        print('-'*30)

        print('-----图书管理系统启动成功-----')

        if not self.login_status:

            print('当前未登录')

            print('请选择要进行的操作：')

            print('     1. 注册:')

            print('     2. 登录:')

            print('     3. 退出系统:')

        else:

            level = self.user.level

            if level == 0:

                member_type = '普通'

                count = 3

            else:

                member_type = f'VIP:{level}'

                count = level + 6

            print(
                f'用户({member_type})已登录:    已借阅/最大借阅({self.user.borrowed_books_count}/{count})')

            print('请选择要进行的操作：')

            print('     0. 借书:')

            print('     1. 还书:')

            print('     2. 查看我的借阅:')

            print('     3. 退出系统:')

            print('     4. 登出:')

            print('     5. 查看图书库存:')

    def register(self):

        register_active = True

        while (register_active):

            print('--------会员注册--------')

            print('注册成功自动登录')

            input_card = input('请输入会员号：')

            input_password = input('请输入密码：')

            if input_card in self.user_account:

                cmd = input('会员号已存在，返回登陆界面输入:1,其他键继续注册')

                if cmd == '1':

                    register_active = False

            else:

                self.user_account[input_card] = Member(
                    input_card, input_password)

                print('注册成功')

                self.login_status = True

                self.user = self.user_account[input_card]

                register_active = False

                print('已登录')

    def login(self):

        print('--------会员登录--------')

        input_card = input('请输入会员号：')

        input_password = input('请输入密码：')

        if input_card in self.user_account and self.user_account[input_card].password == input_password:

            self.login_status = True

            self.user = self.user_account[input_card]

            print('登录成功')

        else:

            self.login_status = False

            print('登录失败')

    def borrow_book(self):

        borrow_active = True

        while (borrow_active):

            print('--------借阅图书--------')

            if self.user.level == 0:

                max_borrow = 3

            else:

                max_borrow = 6 + self.user.level

            user_borrowed = self.user.borrowed_books_count

            print(f'您的最大借阅数量为{max_borrow}, 已借阅{user_borrowed}本')

            if user_borrowed >= max_borrow:

                print('已借阅数量已达最大借阅数量,请还书后再借阅')

                return

            print(f'您还可以借阅{max_borrow - user_borrowed}本')

            # 借阅图书

            book_name = input('请输入图书名称：')

            book_count = int(input('请输入借阅数量：'))

            if book_name not in self.books:

                print('图书不存在')

                return

            elif self.books[book_name] < book_count:

                print(f'图书库存不足,当前库存为{self.books[book_name]}本')

                return

            elif book_count > max_borrow - user_borrowed:

                print(f'您只能借阅{max_borrow - user_borrowed}本')

                return

            else:

                self.user.borrowed_books_count += book_count

                if book_name not in self.user.borrowed_books:

                    self.user.borrowed_books[book_name] = book_count

                else:

                    self.user.borrowed_books[book_name] += book_count

                self.books[book_name] -= book_count

                print('借阅成功')

                print(f'您已借阅{book_count}本{book_name}')

                borrow_active = False

    def return_book(self):

        return_active = True

        while (return_active):

            print('--------归还图书--------')

            if self.user.borrowed_books_count == 0:

                print('您未借阅任何图书,无需还书')

                return

            # 还书图书

            book_name = input('请输入图书名称：')

            book_count = int(input('请输入还书数量：'))

            if book_name not in self.user.borrowed_books or book_count > self.user.borrowed_books[book_name]:

                print('还书信息错误或还书数量超出借阅数量')

                return

            else:

                self.user.borrowed_books_count -= book_count

                self.user.borrowed_books[book_name] -= book_count

                self.books[book_name] += book_count

                print('还书成功')

                print(f'您已还书{book_count}本{book_name}')

                print("继续还书请输入:1,其他键结束")

                cmd = input('请输入您的选择：')

                if cmd != '1':

                    return_active = False

    def show_my_borrowed(self):

        print('--------查看我的借阅--------')

        if self.user.borrowed_books_count == 0:

            print('您未借阅任何图书')

            return

        print(f'您已借阅图书如下：')

        for x in self.user.borrowed_books:

            if self.user.borrowed_books[x] > 0:

                print(f'{x}: {self.user.borrowed_books[x]}本')

        pass

    def logout(self):

        self.login_status = False

        self.user = None

        print('已登出')

    def show_library(self):

        for x in self.books:

            print(f'{x}: {self.books[x]}本')

        input('图书库存显示完成,输入任意键返回')


if __name__ == '__main__':
    L = Library()
    L.books = {
        'Python': 10,
        'Java': 5,
        'C++': 8,
        'JavaScript': 12,
        'Shelock Holmes': 10,
        'The Great Gatsby': 15
    }
    L.user_account = {
        '123456': Member('123456', '123456'),
        'whisper': Member('whisper', 'whisper', 6)
    }
    while (L.active):
        L.show_menu()
        cmd = input('请输入您的选择：')
        if cmd == '3':
            L.active = False
            print('退出系统')
        elif not L.login_status and cmd == '1':
            L.register()
        elif not L.login_status and cmd == '2':
            L.login()
        elif L.login_status and cmd == '0':
            L.borrow_book()
        elif L.login_status and cmd == '1':
            L.return_book()
        elif L.login_status and cmd == '2':
            L.show_my_borrowed()
        elif L.login_status and cmd == '4':
            L.logout()
        elif L.login_status and cmd == '5':
            L.show_library()
        else:
            print('输入错误')
