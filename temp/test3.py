import requests

url = 'https://app.lms.unimelb.edu.au/'
payload = {'user_id': 'caelana', 'password': 'cael1998'}

with requests.Session() as s:
    p = s.post(url, data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    print (p.text)

    # An authorised request.
    r = s.get('https://app.lms.unimelb.edu.au/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_115_1')
    print (r.content)

    