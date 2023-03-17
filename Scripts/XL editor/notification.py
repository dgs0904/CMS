# # import win10toast 
# from win10toast import ToastNotifier
  
# # create an object to ToastNotifier class
# n = ToastNotifier()
# toast = ToastNotifier()

# def test():
#     print("nice")
  
# # n.show_toast("GEEKSFORGEEKS", "Notification body", duration = 20,
# #   icon_path ="https://media.geeksforgeeks.org/wp-content/uploads/geeks.ico")
# toast.show_toast(title="Notification", msg="Hello, there!", callback_on_click=test)
import webbrowser
from win10toast_click import ToastNotifier 

# function 
page_url = 'http://google.com/'

def open_url():
    try: 
        webbrowser.open_new(page_url)
        print('Opening URL...')  
    except: 
        print('Failed to open URL. Unsupported variable type.')

# initialize 
toaster = ToastNotifier()
toaster1 = ToastNotifier()

# showcase
toaster.show_toast(
    "Example one", # title
    "Click to open URL! >>", # message 
    icon_path=None, # 'icon_path' 
    duration=None, # for how many seconds toast should be visible; None = leave notification in Notification Center
    threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears 
    callback_on_click=open_url # click notification to run function 
    )
toaster1.show_toast(
    "Example two", # title
    "Click to open URL! >>", # message 
    icon_path=None, # 'icon_path' 
    duration=None, # for how many seconds toast should be visible; None = leave notification in Notification Center
    threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears 
    callback_on_click=open_url # click notification to run function 
    )