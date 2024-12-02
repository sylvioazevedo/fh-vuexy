from fh_vuexy import *

def NotFoundPage(req, exc):    
    return Titled('404', 'Page not found', 'The page you are looking for is not found')