
from email.quoprimime import quote
import os


c.url.default_page = 'https://google.com/'
c.url.searchengines = {"DEFAULT": "https://google.com/search?hl=en&q={}"}

# check if unix or windows


dir = '/run/user/1000/gvfs/smb-share:server=joris_nas.local,share=common_files/qutebrowser/index.html' 
if os.name == 'nt':
    dir = '//joris_nas/common_files/qutebrowser/index.html'
    config.load_autoconfig(False)
    



c.url.start_pages = dir
c.colors.hints.bg = 'rgba(0,0,0,0.5)'
c.colors.hints.fg = 'white'
