from fasthtml.common import *
from enum import Enum

def asset(s): return Path(__file__).parent/'assets'/s


hdrs = ( 
    # Title('Dashboard - Analytics | Vuexy - Bootstrap Admin Template'),    
    # Meta(name='description', content=''),
    
    Link(rel='icon', type='image/x-icon', href=asset('assets/img/favicon/favicon.ico')),
    Link(rel='preconnect', href='https://fonts.googleapis.com'),
    Link(rel='preconnect', href='https://fonts.gstatic.com', crossorigin=''),
    Link(href='https://fonts.googleapis.com/css2?family=Public+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&display=swap', rel='stylesheet'),

    Link(rel='stylesheet', href=asset('vendor/fonts/fontawesome.css')),
    Link(rel='stylesheet', href=asset('assets/vendor/fonts/tabler-icons.css')),
    Link(rel='stylesheet', href=asset('assets/vendor/fonts/flag-icons.css')),
    Link(rel='stylesheet', href=asset('assets/vendor/css/rtl/core.css')),
    Link(rel='stylesheet', href=asset('assets/vendor/css/rtl/theme-default.css')),

    Link(rel='stylesheet', href=asset('assets/css/demo.css')),
    
    Link(rel='stylesheet', href=asset('assets/vendor/libs/node-waves/node-waves.css')),
    Link(rel='stylesheet', href=asset('assets/vendor/libs/perfect-scrollbar/perfect-scrollbar.css')),
    Link(rel='stylesheet', href=asset('assets/vendor/libs/typeahead-js/typeahead.css')),
    Link(rel='stylesheet', href=asset('assets/vendor/libs/apex-charts/apex-charts.css')),
    Link(rel='stylesheet', href=asset('assets/vendor/libs/swiper/swiper.css')),
    Link(rel='stylesheet', href=asset('assets/vendor/libs/datatables-bs5/datatables.bootstrap5.css')),
    Link(rel='stylesheet', href=asset('assets/vendor/libs/datatables-responsive-bs5/responsive.bootstrap5.css')),
    Link(rel='stylesheet', href=asset('assets/vendor/libs/datatables-checkboxes-jquery/datatables.checkboxes.css')),
    Link(rel='stylesheet', href=asset('assets/vendor/css/pages/cards-advance.css')),
    
    Script(src=asset('assets/vendor/js/helpers.js')),
    Script(src=asset('assets/js/config.js'))
)

ftrs = (    
    Script(src=asset('assets/vendor/libs/jquery/jquery.js')),
    Script(src=asset('assets/vendor/libs/popper/popper.js')),
    Script(src=asset('assets/vendor/js/bootstrap.js')),
    Script(src=asset('assets/vendor/libs/node-waves/node-waves.js')),
    Script(src=asset('assets/vendor/libs/perfect-scrollbar/perfect-scrollbar.js')),
    Script(src=asset('assets/vendor/libs/hammer/hammer.js')),
    Script(src=asset('assets/vendor/libs/i18n/i18n.js')),
    Script(src=asset('assets/vendor/libs/typeahead-js/typeahead.js')),
    Script(src=asset('assets/vendor/js/menu.js')),
    Script(src=asset('assets/vendor/libs/apex-charts/apexcharts.js')),
    Script(src=asset('assets/vendor/libs/swiper/swiper.js')),
    Script(src=asset('assets/vendor/libs/datatables-bs5/datatables-bootstrap5.js')),

    Script(src=asset('assets/js/main.js')),

    Script(src=asset('assets/js/dashboards-analytics.js'))
)