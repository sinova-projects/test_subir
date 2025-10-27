{
    'name': 'AppStore Test Module',
    'version': '17.0.1.0.0',
    'summary': 'Módulo de prueba para publicación en Odoo App Store',
    'sequence': 10,
    'description': """
        Este módulo es una prueba de publicación en el Odoo App Store.
        No agrega funcionalidad real, solo sirve como ejemplo.
    """,
    'author': 'Sinova',
    'website': 'https://tuempresa.com',
    'category': 'Tools',
    'license': 'OPL-1',
    'price': 0.00,  # Puedes dejarlo gratis o ponerle un valor de prueba
    'currency': 'USD',
    'depends': ['base'],
    'data': [
        'views/test_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
