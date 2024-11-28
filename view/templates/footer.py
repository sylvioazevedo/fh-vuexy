from fh_vuexy import *

def AppFooter(session):
    return \
        FooterWrapper(
            TextBody(
                f'© ',
                Script('document.write(new Date().getFullYear());'),
                ' , made with ❤️ by ',
                A(
                    'Pixinvent',
                    href='https://www.pixinvent.com',
                    target='_blank'
                ),
                '. All rights reserved.'
            ),
            InlineBlock(
                A(
                    'Documentation',
                    href='https://demos.pixinvent.com/vuexy-html-admin-template/documentation/',
                    target='_blank',
                    cls='footer-link me-4'
                )
            )
        )                