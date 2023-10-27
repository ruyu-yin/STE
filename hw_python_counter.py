def jump_counter(func):
    # 创建一个闭包以保存调用次数
    counter = [0]

    def wrapper(*args, **kwargs):
        # 在每次调用函数时增加计数
        counter[0] += 1
        print(f"兔兔跳了{counter[0]}下， {func.__name__} 被调用了{counter[0]} 次")
        return func(*args, **kwargs)


    return wrapper

# 使用装饰器将计数器应用到特定函数
@jump_counter
def my_function1():
    print("rabbit jump")


# 调用函数
my_function1()
my_function1()
my_function1()
my_function1()
my_function1()

