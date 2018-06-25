def onShow(widget_show_function):
    def wrapper():
        print("Do shit")
        widget_show_function()

    return wrapper


@onShow
def show():
    print("Show this widget")

show()