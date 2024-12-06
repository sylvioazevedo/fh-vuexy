from fasthtml.common import *
from fasthtml.core import FT
from enum import Enum

def asset(s): return Path(__file__).parent/'assets'/s

bst_sz_d = {'576':'sm', '768':'md', '992':'lg', '1200':'xl', '1400':'xxl'}


vuexy_hdrs = ( 
    # Title('Dashboard - Analytics | Vuexy - Bootstrap Admin Template'),    
    # Meta(name='description', content=''),
    
    Link(rel='icon', type='image/x-icon', href='/img/favicon/favicon.ico'),
    Link(rel='preconnect', href='https://fonts.googleapis.com'),
    Link(rel='preconnect', href='https://fonts.gstatic.com', crossorigin=''),
    Link(href='https://fonts.googleapis.com/css2?family=Public+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&display=swap', rel='stylesheet'),

    Link(rel='stylesheet', href='/vendor/fonts/fontawesome.css'),
    Link(rel='stylesheet', href='/vendor/fonts/tabler-icons.css'),
    Link(rel='stylesheet', href='/vendor/fonts/flag-icons.css'),
    Link(rel='stylesheet', href='/vendor/css/rtl/core.css'),
    Link(rel='stylesheet', href='/vendor/css/rtl/theme-default.css'),

    Link(rel='stylesheet', href='/css/demo.css'),
    
    Link(rel='stylesheet', href='/vendor/libs/node-waves/node-waves.css'),
    Link(rel='stylesheet', href='/vendor/libs/perfect-scrollbar/perfect-scrollbar.css'),
    # Link(rel='stylesheet', href='vendor/libs/typeahead-js/typeahead.css'),
    # Link(rel='stylesheet', href='vendor/libs/apex-charts/apex-charts.css'),
    # Link(rel='stylesheet', href='vendor/libs/swiper/swiper.css'),
    # Link(rel='stylesheet', href='vendor/libs/datatables-bs5/datatables.bootstrap5.css'),
    # Link(rel='stylesheet', href='vendor/libs/datatables-responsive-bs5/responsive.bootstrap5.css'),
    # Link(rel='stylesheet', href='vendor/libs/datatables-checkboxes-jquery/datatables.checkboxes.css'),
    # Link(rel='stylesheet', href='vendor/css/pages/cards-advance.css'),
    
    Script(src='/vendor/js/helpers.js'),    
    Script(src='/js/config.js')
)

vuexy_ftrs = (    
    Script(src='/vendor/libs/jquery/jquery.js'),
    Script(src='/vendor/libs/popper/popper.js'),
    Script(src='/vendor/js/bootstrap.js'),
    Script(src='/vendor/libs/node-waves/node-waves.js'),
    Script(src='/vendor/libs/perfect-scrollbar/perfect-scrollbar.js'),
    Script(src='/vendor/libs/hammer/hammer.js'),
    Script(src='/vendor/js/menu.js'),
    Script(src='/js/main.js')
    # Script(src='vendor/libs/i18n/i18n.js'),
    # Script(src='vendor/libs/typeahead-js/typeahead.js'),    
    # Script(src='vendor/libs/apex-charts/apexcharts.js'),
    # Script(src='vendor/libs/swiper/swiper.js'),

    # Script(src='js/dashboards-analytics.js')
)

def placehold(x,y): return f'https://placehold.co/{x}x{y}'

class VEnum(Enum):
    def __str__(self): return self.value

class BSEnum(Enum):
    def __str__(self):
        r = self.value
        nm = self.__class__.__name__.rstrip('T').lower()
        if not r: return nm
        return f'{nm}-{r}'

class ContainerT(BSEnum):
    Basic = ''
    Fluid = 'fluid'
    Sm = 'sm'
    Md = 'md'
    Lg = 'lg'
    Xl = 'xl'
    Xxl = 'xxl'

class SizeT(VEnum):
    Default = ''
    Sm = 'sm'
    Md = 'md'
    Lg = 'lg'
    Xl = 'xl'
    Xxl = 'xxl'

def Container(*c, typ:ContainerT|str=ContainerT.Basic, cls='', **kw):
    return Div(*c, cls=f'{typ} {cls}', **kw)

class PlacementT(VEnum):
    Default = ''
    FixedTop = 'fixed-top'
    FixedBottom = 'fixed-bottom'
    StickyTop = 'sticky-top'
    StickyBottom = 'sticky-bottom'

class PositionT(BSEnum):
    Static = 'static'
    Relative = 'relative'
    Absolute = 'absolute'
    Fixed = 'fixed'
    Sticky = 'sticky'

def Divider(): return Li(Div(cls='dropdown-divider my-1 mx-n2'))

def NavBarDropDownButton(text, href, icon=None, cls='', **kw):
    return \
        Li(
            Div(
                A(
                    I(cls=f'{icon} me-2 ti-14px'),
                    Small(text, cls='align-middle'),
                    
                    href=href,
                    cls=f'btn d-flex {cls}'
                ),
                cls='d-grid px-2 pt-2 pb-1'
            )
        )

def NavBarLayout(*c, id=None, cls='', light=True, light_controls=True, **kw):
    return \
        Nav(
            Div(
                A(
                    I(cls='ti ti-menu-2 ti-md'),
                    href='javascript:void(0);',
                    cls='nav-item nav-link px-0 me-xl-4'
                ),
                cls='layout-menu-toggle navbar-nav align-items-xl-center me-3 me-xl-0 d-xl-none'
            ),
            Div(
                Div(
                    Div(
                        A(
                            I(cls=f'ti {'ti-sun' if light else 'ti-moon-stars'} ti-md'),
                            data_bs_toggle='dropdown',
                            href='javascript:void(0);',
                            cls='nav-link btn btn-text-secondary btn-icon rounded-pill dropdown-toggle hide-arrow'
                        ),
                        Ul(
                            Li(
                                A(
                                    Span(
                                        I(cls='ti ti-sun me-3'),
                                        'Light',
                                        cls='align-middle'
                                    ),
                                    href='javascript:void(0);',
                                    data_theme='light',
                                    cls='dropdown-item'
                                ),
                                A(
                                    Span(
                                        I(cls='ti ti-moon-stars me-3'),
                                        'Dark',
                                        cls='align-middle'
                                    ),
                                    href='javascript:void(0);',
                                    data_theme='dark',
                                    cls='dropdown-item'
                                ),
                                A(
                                    Span(
                                        I(cls='ti ti-device-desktop-analytics me-3'),
                                        'System',
                                        cls='align-middle'
                                    ),
                                    href='javascript:void(0);',
                                    data_theme='system',
                                    cls='dropdown-item'
                                ),
                            ),
                            cls='dropdown-menu dropdown-menu-start dropdown-styles'
                        ),
                        cls='nav-item dropdown-style-switcher dropdown'
                    ),
                    cls='navbar-nav align-items-center'
                ),
                cls='navbar-nav-right d-flex align-items-center'
            ) if light_controls else None,
            *c,
            cls=f'layout-navbar container-xxl navbar navbar-expand-xl navbar-detached align-items-center bg-navbar-theme {cls}',
            id=id,           
        )

def NavbarItem(text, href='#', current=False, disabled=False, cls='', **kw):
    acls = 'nav-link'
    if current:
        kw['aria_current'] = 'page'
        cls += ' active'
        acls += ' active'
    if disabled:
        kw['aria_disabled'] = 'true'
        acls += ' disabled'
    return Li(A(text, href=href, cls=acls, **kw), cls='nav-item '+cls)

def Navbar(id, selidx, items, ra_items=None, image=None, text=None, hdr_href='#', dark=False,
           cls='', itemcls='', expand:SizeT=SizeT.Lg, toggle_text='More', toggle_left=True,
           container:ContainerT=ContainerT.Fluid, placement:PlacementT=PlacementT.Default, **kw):
    
    image = Img(src=image, cls='d-inline-block align-text-bottom') if image else None
    
    if dark:
        kw['data-bs-theme'] = 'dark'
        cls += ' bg-dark' if cls else 'bg-dark'
    else:
        cls += ' bg-light' if cls else 'bg-light'

    def mk_navitem(i, o):
        if isinstance(o, FT): return o
        text, href, *kw = o
        kw = kw[0] if kw else {}
        return NavbarItem(text, href, i==selidx, cls=itemcls, **kw)
    
    items = [mk_navitem(i, o) for i,o in enumerate(items)]

    if not ra_items: ra_items = []
    if isinstance(ra_items, FT): ra_items = [ra_items]

    toggle = Button(
        Div(
            Span(cls='navbar-toggler-icon me-2'),
            Span(toggle_text, cls='small'),
            cls='d-flex align-items-center'),
        type='button', data_bs_toggle='collapse', data_bs_target=f'#{id}',
        aria_controls=id, aria_expanded='false', aria_label='Toggle navigation',
        cls='navbar-toggler p-2')
    brand = A(image, text, href=hdr_href, cls='navbar-brand')
    tb = [toggle,brand] if toggle_left else [brand,toggle]

    return Nav(
        Div(
            *tb,
            Div(
                Ul(*items, cls=f'navbar-nav me-auto mb-2 mb-{expand}-0'), 
                *ra_items,                
                id=id, cls='collapse navbar-collapse'),
            cls=container),
        cls=f'navbar navbar-expand-{expand} {placement} {cls}', **kw)

def NavText(text): return Span(text, cls='navbar-text')

def NavDropDownItem(text, href='#', disabled=False, **kw):
    acls = 'dropdown-item'
    if disabled:
        kw['aria_disabled'] = 'true'
        acls += ' disabled'
    return A(text, href=href, cls=acls, **kw)

def NavDropDown(id, items, text, cls='', **kw):
    items = [NavbarItem(*o) for o in items]
    return Div(
        Button(
            Span(text),
            cls='btn btn-secondary dropdown-toggle',
            data_bs_toggle='dropdown',
            aria_haspopup='true',
            aria_expanded='false'),
        Div(
            Ul(*items, cls='dropdown-menu', aria_labelledby=id),
            cls='dropdown'),
        cls=cls, **kw)

def NavBarAvatar(name, role, *items, img_src=None, initials=None,status=None, cls='', **kw):

    return \
        Ul(
            Li(
                A(
                    Div(
                        Img(src=img_src, cls='rounded-circle') if img_src else Span(initials, cls='avatar-initial rounded-circle bg-label-primary'),
                        cls=f'avatar{(f" avatar-{status}" if status else "")}'                        
                    ),                    
                    data_bs_toggle='dropdown',
                    href='javascript:void(0);',
                    cls='nav-link dropdown-toggle hide-arrow p-0'
                ),
                Ul(
                    Li(
                        A(
                            Div(
                                Div(
                                    Div(
                                        Img(src=img_src, cls='rounded-circle') if img_src else Span(initials, cls='avatar-initial rounded-circle bg-label-primary'),
                                        cls=f'avatar{(f" avatar-{status}" if status else "")}'                        
                                    ),                                    
                                    cls='flex-shrink-0 me-2'
                                ),
                                Div(
                                    H6(name, cls='mb-0'),
                                    Small(role, cls='text-muted'),
                                    cls='flex-grow-1',
                                ),
                                cls='d-flex align-items-center'
                            ),
                            cls='dropdown-item mt-0',
                            href='#'
                        )
                    ),
                    Divider() if items else None,
                    *items,
                    cls='dropdown-menu dropdown-menu-end'
                ),
                cls='nav-item navbar-dropdown dropdown-user dropdown'
            ),
            cls='navbar-nav flex-row align-items-center ms-auto'
        )

def NavBarAvatarItem(text, icon, href, cls='', **kw):
    return \
        Li(
            A(
                I(cls=icon) if icon else None,
                Span(text, cls='align-middle'),
                href=href, cls='dropdown-item', **kw
            ), 
        )

def NavBarAvatarNotifyItem(text, icon, href, notify, cls='', **kw):
    return \
        Li(
            A(
                Span(
                    I(cls=f'flex-shrink-0 {icon}') if icon else None,
                    Span(text, cls='flex-grow-1 align-middle'),
                    Span(notify, cls='flex-shrink-0 badge bg-danger d-flex align-items-center justify-content-center'),
                    href=href, 
                    cls='d-flex align-items-center align-middle'
                ),
                cls='dropdown-item', **kw,
            ), 
        )


def Image(src, alt=None, sz:SizeT=SizeT.Sm, caption=None, capcls='', pad=2, left=True, cls='', retina=True, **kw):
    place = 'start' if left else 'end'
    if retina: kw['srcset'] = f'{src} 2x'
    return Figure(
        Img(src=src, alt=alt, 
            cls=f'figure-img img-fluid {cls}', **kw),
        Figcaption(caption, cls=f'caption-{sz} {capcls} text-center'),
        cls=f'd-sm-table float-{sz}-{place} mx-{sz}-{pad+1} my-{sz}-{pad}')

def Icon(ico, dark=False, sz='', cls='', button=True, href='#', **kw):
    if dark: cls += ' btn-dark'
    if sz: cls += f' btn-{sz}'
    if button:
        kw['role'] = 'button'
        cls += ' btn'
    return A(I(cls=ico), href=href, cls=cls, **kw)

def Toc(*c, width=2):
    return Div(
        Div(
            Nav(id='toc', data_toggle='toc', cls='sticky-top toc'),
            cls=f'col-sm-{width}'),
        Div(*c, cls=f'col-sm-{12-width}'),
        cls='row')

def VuexyFooter(copy, img, img_href, cs, cls='', **kw):
    # From the bootstrap examples footers page
    return Container(
        Footer(
            P(copy, cls='col-md-4 mb-0 text-muted'),
            A(img, href=img_href,
                cls='col-md-4 d-flex align-items-center justify-content-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none'),
            Ul(*[Li(o, cls='nav-item') for o in cs], 
                cls='nav col-md-4 justify-content-end'),
            cls=f'{cls} d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top', **kw))


class AvatarSizeT(VEnum):
    Xs = 'xs'
    Sm = 'sm'
    Md = 'md'
    Lg = 'lg'
    Xl = 'xl'

class AvatarShapeT(VEnum):
    Circle = 'rounded-circle'
    Square = 'rounded'

class AvatarStatusT(VEnum):
    Online = 'online'
    Offline = 'offline'
    Busy = 'busy'
    Away = 'away'

def AvatarStatus(status:AvatarStatusT, cls='', *args, **kw):
    return Div(cls=f'avatar me-2 avatar-{status} {cls}', *args, **kw)

def Avatar(src, alt, shape: AvatarShapeT=AvatarShapeT.Circle, size: AvatarSizeT=None, cls='', **kw):
    return Div(
        Img(src=src, alt=alt, cls=f'{shape} {cls}', **kw),
        cls=f'avatar {f'avatar-{size}' if size else ''} me-2'
    )

def AvatarInitials(initials, shape: AvatarShapeT=AvatarShapeT.Circle, size: AvatarSizeT=None, cls='', **kw):
    return Div(
        Span(initials, cls=f'avatar-initial {shape} {cls}'),
        cls=f'avatar {f'avatar-{size}' if size else ''} me-2',
         **kw
    )
    
class CardLocationT(VEnum):
    Top = 'top'
    Bottom = 'bottom'    

def CardLink(text, href, cls='', **kw):
    return A(text, href=href, cls=f'card-link {cls}', **kw)

def BasicCard(title, body, footer=None, title_location: CardLocationT=CardLocationT.Bottom, links=None, cls='', **kw):

    if title_location==CardLocationT.Bottom:
        body = Div(H5(title, cls='card-title'), body, cls='card-body')

    if links:
        footer = Div(*[CardLink(*o) for o in links], cls='card-footer')

    return Div(
        Div(
            Div(
                Div(                    
                    H5(title, cls='card-title') if title_location==CardLocationT.Top else None,
                    body,
                    footer,
                    cls='card-body'),
                cls='card'),
            cls='col'),
        cls=f'{cls} row', **kw)

def ImageCard(title, body, img, img_alt, img_href, footer=None, title_location: CardLocationT=CardLocationT.Bottom, links=None, cls='', **kw):
    
        if title_location==CardLocationT.Bottom:
            body = Div(H5(title, cls='card-title'), body, cls='card-body')
    
        if links:
            footer = Div(*[CardLink(*o) for o in links], cls='card-footer')
    
        return Div(
            Div(
                Div(
                    Div(
                        Img(src=img, alt=img_alt, cls='card-img-top', href=img_href),
                        Div(
                            H5(title, cls='card-title') if title_location==CardLocationT.Top else None,
                            body,
                            footer,
                            cls='card-body'),
                    cls='card'),
                cls='col'),
            cls=f'{cls} row', **kw
            )
        )

def ImageOverlayCard(title, body, img, img_alt, img_href, footer=None, title_location: CardLocationT=CardLocationT.Bottom, links=None, cls='', **kw):
    
        if title_location==CardLocationT.Bottom:
            body = Div(H5(title, cls='card-title'), body, cls='card-body')
    
        if links:
            footer = Div(*[CardLink(*o) for o in links], cls='card-footer')
    
        return Div(
            Div(
                Div(
                    Div(
                        Img(src=img, alt=img_alt, cls='card-img-top', href=img_href),
                        Div(
                            H5(title, cls='card-title') if title_location==CardLocationT.Top else None,
                            body,
                            footer,
                            cls='card-body'),
                    cls='card'),
                cls='col'),
            cls=f'{cls} row', **kw
            )
        )


def ListGroupItem(text):
    return Li(text, cls='list-group-item')        
        

def ListGroupCard(title, items, footer=None, title_location: CardLocationT=CardLocationT.Bottom, links=None, cls='', **kw):
    
    if title_location==CardLocationT.Bottom:
        items = Ul(*[Li(o) for o in items], cls='list-group list-group-flush')
        body = Div(H5(title, cls='card-title'), items, cls='card-body')

    if links:
        footer = Div(*[CardLink(*o) for o in links], cls='card-footer')

    return Div(
        Div(
            Div(
                Div(
                    H5(title, cls='card-title') if title_location==CardLocationT.Top else None,
                    items,
                    footer,
                    cls='card-body'),
                cls='card'),
            cls='col'),
        cls=f'{cls} row', **kw)

def CardGroup(*cards, cls='', **kw):
    return Div(
        Div(*cards, cls='row g-2'),
        cls=f'{cls} row', **kw)

def CardDeck(*cards, cls='', **kw):
    return Div(
        Div(*cards, cls='col-md-4'),
        cls=f'{cls} row', **kw)

def CardColumns(*cards, cls='', **kw):
    return Div(
        Div(*cards, cls='col-md-4'),
        cls=f'{cls} row', **kw)

def CardCarousel(*cards, cls='', **kw):
    return Div(
        Div(*cards, cls='carousel-inner'),
        cls=f'{cls} carousel slide', **kw)

def CollapsibleCard(title, body, footer=None, title_location: CardLocationT=CardLocationT.Bottom, links=None, cls='', **kw):
    
    if title_location==CardLocationT.Bottom:
        body = Div(H5(title, cls='card-title'), body, cls='card-body')

    if links:
        footer = Div(*[CardLink(*o) for o in links], cls='card-footer')

    return Div(
        Div(
            Div(
                Div(
                    Div(
                        Button(
                            H5(title, cls='card-title'),
                            type='button',
                            data_bs_toggle='collapse',
                            data_bs_target='#collapseExample',
                            aria_expanded='false',
                            aria_controls='collapseExample',
                            cls='btn btn-link'),
                        Div(body, cls='collapse'),
                        footer,
                        cls='card-body'),
                    cls='card'),
                cls='col'),
            cls='row'),
        cls=f'{cls}', **kw)


def Layout(*c, cls='', **kw):
    return Div(
            Div(*c, cls='layout-container'),
            Div(cls='layout-overlay layout-menu-toggle'),
            Div(cls='drag-target'),
            cls=f'layout-wrapper layout-content-navbar {cls}',
            **kw
        )

def VerticalMenuItem(text, href, icon=None, active:bool = False, cls='', **kw):    
    return Li(
        A(
            I(cls=f'menu-icon tf-icons {icon}') if icon else None,
            Div(text, data_i18n=text),
            href=href,
            cls='menu-link',
            **kw
        ),
        cls=f'menu-item{(' active' if active else '')}',
    )

def VerticalMenu(id, *items, brand_logo, brand_text, cls='', **kw):

    return Aside(
                Div(
                    A(                        
                        Span(
                            brand_logo,
                            cls='app-brand-logo demo'
                        ),
                        Span(brand_text, cls='app-brand-text demo menu-text fw-bold'),                    
                        href='/',
                        cls='app-brand-link',
                    ),
                    A(
                        I(cls='ti menu-toggle-icon d-none d-xl-block align-middle'),
                        I(cls='ti ti-x d-block d-xl-none ti-md align-middle'),
                        href='javascript:void(0);',
                        cls='layout-menu-toggle menu-link text-large ms-auto',                        
                    ),
                    cls='app-brand demo'
                ),
                Div(cls='menu-inner-shadow'),               

                Ul(*items, cls='menu-inner py-1'),
                id=id,
                cls='layout-menu menu-vertical menu bg-menu-theme',
                **kw
            )
    
def LayoutPage(*c, cls='', **kw):
    return Div(*c, cls=f'layout-page {cls}', **kw)

def ContentWrapper(*c, cls='', **kw):
    return \
        Div(
            Div(*c, cls='container-xxl flex-grow-1 container-p-y'),
            Div(cls='content-backdrop fade'),
            cls=f'content-wrapper {cls}', **kw
        )

def FooterWrapper(*c, cls='', **kw):
    return \
        Footer(
            Div(
                Div(
                    *c,
                    cls='footer-container d-flex align-items-center justify-content-between py-4 flex-md-row flex-column'
                ),
                cls='container-xxl'
            ),
            cls=f'content-footer footer bg-footer-theme {cls}'
        )
    
        
def Page(title, *c, cls='', **kw):
    return \
        ContentWrapper(
            H4(title, cls='py-4 mb-0') if title else None,
            *c,
            cls=cls,
            **kw
        )

def FormPage(*c, cls='', **kw):
    return \
        ContentWrapper(            
            *c,
            cls=cls,
            **kw
        )

def TextBody(*c):
    return Div(*c, cls='text-body')

def InlineBlock(*c, cls='', **kw):
    return Div(*c, cls=f'd-none d-lg-inline-block {cls}', **kw)

class AlertTypeT(VEnum):
    Primary = 'primary'
    Secondary = 'secondary'
    Success = 'success'
    Danger = 'danger'
    Warning = 'warning'
    Info = 'info'
    Light = 'light'
    Dark = 'dark'

def Alert(*c, type:AlertTypeT=AlertTypeT.Primary, icon=None, dimissible=False, outline=False, cls='', **kw):
    return \
        Div(
            Span(I(cls=f'{icon} alert-icon rounded') if icon else None),
            *c,
            cls=f'alert alert{"-outline" if outline else ""}-{type}{' alert-dismissible' if dimissible else ''}{' d-flex align-items-center' if icon else ''} {cls}',
            role='alert',
            **kw
        )

def AlertText(title, text):
    return \
        H5(title, cls='alert-heading mb2'), \
        P(text, cls='mb-0')
    
def StyledButton(text, href, icon=None, type='button', cls='', **kw):
    return \
        A(
            I(cls=f'{icon} me-2') if icon else None,
            text,
            href=href,
            cls=f'btn d-flex {cls}',
            role=type,
            **kw
        )
def TableActionButton(icon=None, href='#', cls='', **kw):
    return \
        A(
            I(cls=f'{icon if icon else 'ti ti-pencil'} ti-md'),
            href=href,
            cls=f'btn btn-sm btn-text-secondary rounded-pill btn-icon waves-effect {cls}',
            **kw
        )

def paginate(total_items, page, per_page, max_pages=5):

    total_pages = (total_items + per_page - 1) // per_page    
    half_max_pages = max_pages // 2
    
    if total_pages <= max_pages:
        page_range = range(1, total_pages + 1)
    elif page <= half_max_pages:
        page_range = range(1, max_pages + 1)
    elif page > total_pages - half_max_pages:
        page_range = range(total_pages - max_pages + 1, total_pages + 1)
    else:
        page_range = range(page - half_max_pages, page + half_max_pages + 1)

    return page_range, total_pages

def TablePagination(base_url, page, page_range, total_pages, cls='', **kw):

    return \
        Nav(
            Ul(
                Li(
                    A(I(cls='tf-icon ti ti-chevrons-left ti-xs'), href=f'{base_url}?page={1}', tabindex='-1', cls='page-link') if page > 1 else None,
                    cls='page-item' if page > 1 else 'page-item disabled'
                ),                                
                Li(
                    A(I(cls='tf-icon ti ti-chevron-left ti-xs'), href=f'{base_url}?page={page-1}', tabindex='-1', cls='page-link') if page > 1 else None,
                    cls='page-item' if page > 1 else 'page-item disabled'
                ),
                Li(
                    A('...', href=f'#', cls='page-link') if page_range[0] > 1 else None,
                    cls='page-item' if page_range[0] > 1 else 'page-item disabled',
                ),
                *[Li(
                    A(str(p), href=f'{base_url}?page={p}', cls='page-link') if p != page else A(str(p), href='#', cls='page-link'),
                    cls=f'{'page-item' if p != page else 'page-item active'}'
                ) for p in page_range],                                
                Li(
                    A('...', href=f'#', cls='page-link') if page_range[-1] < total_pages else None,
                    cls='page-item' if page_range[-1] < total_pages else 'page-item disabled',
                ),
                Li(
                    A(I(cls='tf-icon ti ti-chevron-right ti-xs'), href=f'{base_url}?page={page+1}', cls='page-link') if page < total_pages else None,
                    cls='page-item' if page < total_pages else 'page-item disabled'
                ),
                Li(
                    A(I(cls='tf-icon ti ti-chevrons-right ti-xs'), href=f'{base_url}?page={total_pages}', cls='page-link') if page < total_pages else None,
                    cls='page-item me-2' if page < total_pages else 'page-item disabled'
                ),
                cls='pagination pagination-sm justify-content-end me-2'
            ),
            aria_label='...'
        ) if total_pages > 1 else None

def TableRow(*c, cls='', **kw):
    return Td(*c, cls=cls, **kw)

def SimpleTable(headers, rows, cls='', **kw):

    return \
        Table(
            Thead(
                Tr(
                    *[Th(h) for h in headers]
                )
            ),
            Tbody(
                *[Tr(
                    *[r for r in row],
                    cls='table-light' if i % 2 == 0 else '',
                ) for i, row in enumerate(rows)],
                cls='table-border-bottom-0'
            ),
            cls=f'table table-sm table-hover {cls}',
            **kw
        )
